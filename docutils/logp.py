import sys
import re
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QTextEdit, QLabel)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt


class SQLLogParser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 메인 윈도우 설정
        self.setWindowTitle('logp')
        self.setGeometry(100, 100, 1200, 800)

        # 중앙 위젯 생성
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 메인 레이아웃 설정
        main_layout = QVBoxLayout(central_widget)

        # 입력 영역
        input_label = QLabel('SQL 로그 입력:')
        input_label.setStyleSheet("font-weight: bold; color: #2c3e50;")
        self.input_text = QTextEdit()
        self.input_text.setFont(QFont('Consolas', 10))
        self.input_text.setStyleSheet("""
            QTextEdit {
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                padding: 5px;
                background-color: #ffffff;
            }
        """)
        main_layout.addWidget(input_label)
        main_layout.addWidget(self.input_text)

        # 버튼 영역
        button_layout = QHBoxLayout()

        button_style = """
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #2574a9;
            }
        """

        self.convert_button = QPushButton('변환', self)
        self.convert_button.setStyleSheet(button_style)
        self.convert_button.clicked.connect(self.convert_query)
        self.convert_button.setFixedSize(100, 30)

        self.clear_button = QPushButton('지우기', self)
        self.clear_button.setStyleSheet(button_style.replace('#3498db', '#e74c3c')
                                        .replace('#2980b9', '#c0392b')
                                        .replace('#2574a9', '#a93226'))
        self.clear_button.clicked.connect(self.clear_text)
        self.clear_button.setFixedSize(100, 30)

        button_layout.addWidget(self.convert_button)
        button_layout.addWidget(self.clear_button)
        button_layout.addStretch()

        main_layout.addLayout(button_layout)

        # 출력 영역
        output_label = QLabel('변환된 SQL 쿼리:')
        output_label.setStyleSheet("font-weight: bold; color: #2c3e50;")
        self.output_text = QTextEdit()
        self.output_text.setFont(QFont('Consolas', 10))
        self.output_text.setReadOnly(True)
        self.output_text.setStyleSheet("""
            QTextEdit {
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                padding: 5px;
                background-color: #f9f9f9;
            }
        """)
        main_layout.addWidget(output_label)
        main_layout.addWidget(self.output_text)

    def parse_parameters(self, params_text):
        if not params_text:
            return []

        params = []
        current_param = ''
        in_parentheses = 0
        in_quotes = False

        for char in params_text:
            if char == '(' and not in_quotes:
                in_parentheses += 1
                current_param += char
            elif char == ')' and not in_quotes:
                in_parentheses -= 1
                current_param += char
                if in_parentheses == 0:
                    params.append(current_param.strip())
                    current_param = ''
            elif char == "'" and current_param:
                in_quotes = not in_quotes
                current_param += char
            elif char == ',' and in_parentheses == 0 and not in_quotes:
                if current_param:
                    params.append(current_param.strip())
                current_param = ''
            else:
                current_param += char

        if current_param:
            params.append(current_param.strip())

        return [p for p in params if p]

    def process_parameter(self, param):
        # 파라미터 값과 타입 분리
        match = re.match(r'(.*?)(?:\((.*?)\))?$', param.strip())
        if not match:
            return 'NULL'

        value, param_type = match.groups()
        value = value.strip()
        param_type = (param_type or '').strip()

        # null 값 처리
        if value.lower() == 'null':
            return 'NULL'

        # 데이터 타입별 처리
        if param_type:
            param_type = param_type.lower()

            # 문자열 타입
            if param_type in ['string', 'varchar', 'char']:
                # 작은따옴표 이스케이프
                value = value.replace("'", "''")
                return f"'{value}'"

            # 날짜/시간 타입
            elif param_type in ['timestamp', 'date', 'datetime']:
                return f"'{value}'"

            # 숫자 타입
            elif param_type in ['integer', 'int', 'long', 'number', 'decimal', 'numeric']:
                try:
                    float(value)  # 숫자 형식 검증
                    return value
                except ValueError:
                    return '0'

            # Boolean 타입
            elif param_type in ['boolean', 'bool']:
                return '1' if value.lower() in ['true', '1', 't', 'y', 'yes'] else '0'

        # 타입이 명시되지 않은 경우 값을 보고 추측
        try:
            float(value)
            return value
        except ValueError:
            if value.lower() in ['true', 'false']:
                return '1' if value.lower() == 'true' else '0'
            # 기본적으로 문자열로 처리
            return f"'{value}'"

    def parse_log_and_combine_query(self, log_text):
        # 쿼리 추출
        query_match = re.search(r'calling prepareStatement\((.*?)\)\.\.\.', log_text, re.DOTALL)
        params_match = re.search(r'Parameters: (.*?)(?:\n|$)', log_text, re.DOTALL)

        if not query_match:
            # 직접 SQL 쿼리가 입력된 경우를 처리
            if 'SELECT' in log_text.upper():
                query = log_text.strip()
            else:
                raise ValueError("로그 형식이 올바르지 않습니다.")
        else:
            query = query_match.group(1).strip()

            # 파라미터가 있는 경우 처리
            if params_match:
                params_text = params_match.group(1).strip()
                if params_text:
                    params = self.parse_parameters(params_text)
                    processed_params = [self.process_parameter(param) for param in params]

                    # 파라미터 값을 쿼리의 ? 위치에 대체
                    for param in processed_params:
                        query = query.replace('?', param, 1)

        # 쿼리 포매팅
        formatted_query = self.format_sql_query(query)
        return formatted_query

    def format_sql_query(self, query):
        # 기본 전처리
        query = re.sub(r'\s+', ' ', query).strip()

        # SELECT 구문 분리 및 컬럼 포맷팅
        if query.upper().startswith('SELECT'):
            # FROM 위치 찾기
            from_pos = re.search(r'\sFROM\s', query, re.IGNORECASE)
            if from_pos:
                from_pos = from_pos.start()
                select_part = query[:from_pos]
                rest_part = query[from_pos:]

                # SELECT 절의 컬럼들 분리
                columns = select_part[6:].split(',')  # 'SELECT ' 제거 후 분리
                formatted_columns = ['SELECT ' + columns[0].strip()]
                formatted_columns.extend(['    ,' + col.strip() for col in columns[1:]])

                query = '\n'.join(formatted_columns) + rest_part

        # 주요 SQL 키워드에 대한 줄바꿈 및 들여쓰기 규칙
        formatting_rules = [
            (r'\sFROM\s', '\nFROM ', 0),
            (r'\sWHERE\s', '\nWHERE ', 0),
            (r'\sAND\s', '\n    AND ', 0),
            (r'\sOR\s', '\n    OR ', 0),
            (r'\sORDER\sSIBLINGS\sBY\s', '\nORDER SIBLINGS BY ', 0),
            (r'\sORDER\sBY\s', '\nORDER BY ', 0),
            (r'\sGROUP\sBY\s', '\nGROUP BY ', 0),
            (r'\sHAVING\s', '\nHAVING ', 0),
            (r'\sCONNECT\sBY\sPRIOR\s', '\nCONNECT BY PRIOR ', 0),
            (r'\sSTART\sWith\s', '\nSTART WITH ', 0),
            (r'\sUNION\s', '\nUNION\n', 0),
            (r'\sINTERSECT\s', '\nINTERSECT\n', 0),
            (r'\sEXCEPT\s', '\nEXCEPT\n', 0)
        ]

        # 포매팅 규칙 적용
        for pattern, replacement, _ in formatting_rules:
            query = re.sub(pattern, replacement, query, flags=re.IGNORECASE)

        # 최종 정리
        lines = query.split('\n')
        formatted_lines = []
        base_indent = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # 들여쓰기 레벨 결정
            indent = base_indent
            if line.startswith('SELECT') or line.startswith('FROM') or line.startswith('INSERT'):
                indent = 0
            elif line.startswith(','):
                indent = 1
            elif line.startswith('WHERE') or line.startswith('START WITH') or line.startswith('CONNECT BY'):
                indent = 0
            elif line.startswith('AND') or line.startswith('OR'):
                indent = 1
            elif line.startswith('ORDER') or line.startswith('GROUP'):
                indent = 0

            # 들여쓰기 적용
            formatted_lines.append('    ' * indent + line)

        return '\n'.join(formatted_lines)

    def convert_query(self):
        try:
            input_text = self.input_text.toPlainText()
            if not input_text.strip():
                self.output_text.setText("입력된 로그가 없습니다.")
                return

            result = self.parse_log_and_combine_query(input_text)
            self.output_text.setText(result)
        except Exception as e:
            self.output_text.setText(f"오류 발생: {str(e)}")

    def clear_text(self):
        self.input_text.clear()
        self.output_text.clear()


if __name__ == '__main__':
    # PyQt 예외 후킹 방지
    sys.excepthook = sys.__excepthook__

    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = SQLLogParser()
    window.show()
    sys.exit(app.exec_())