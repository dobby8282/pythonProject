# main.py
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

    def parse_log_and_combine_query(self, log_text):
        # 쿼리와 파라미터 부분 추출
        query_match = re.search(r'calling prepareStatement\((.*?)\)\.\.\.', log_text, re.DOTALL)
        params_match = re.search(r'Parameters: (.*?)$', log_text, re.DOTALL)

        if not query_match or not params_match:
            raise ValueError("로그 형식이 올바르지 않습니다.")

        query = query_match.group(1).strip()
        params_str = params_match.group(1).strip()

        # 파라미터 파싱
        params = []
        current_param = ''
        in_parentheses = False

        for char in params_str:
            if char == '(' and not in_parentheses:
                in_parentheses = True
                current_param += char
            elif char == ')' and in_parentheses:
                in_parentheses = False
                current_param += char
            elif char == ',' and not in_parentheses:
                params.append(current_param.strip())
                current_param = ''
            else:
                current_param += char

        if current_param:
            params.append(current_param.strip())

        # 파라미터 타입 처리
        processed_params = []
        for param in params:
            param_value = param.split('(')[0].strip()
            param_type = param.split('(')[1].rstrip(')') if '(' in param else None

            if param_value.lower() == 'null':
                processed_params.append('NULL')
            elif param_type == 'String':
                # SQL 문자열 내의 따옴표 처리
                param_value = param_value.replace("'", "''")
                processed_params.append(f"'{param_value}'")
            else:
                processed_params.append(param_value)

        # 쿼리에 파라미터 삽입
        final_query = query
        for param in processed_params:
            final_query = final_query.replace('?', param, 1)

        # 쿼리 포매팅
        formatted_query = self.format_sql_query(final_query)
        return formatted_query

    def format_sql_query(self, query):
        # 기본적인 SQL 키워드
        keywords = ['SELECT', 'FROM', 'WHERE', 'INSERT', 'INTO', 'VALUES',
                    'UPDATE', 'SET', 'DELETE', 'AND', 'OR', 'ORDER BY',
                    'GROUP BY', 'HAVING', 'JOIN', 'LEFT', 'RIGHT', 'INNER',
                    'OUTER', 'ON', 'AS']

        # 대소문자 구분없이 키워드 찾아서 줄바꿈 추가
        formatted = query
        for keyword in keywords:
            pattern = re.compile(rf'\b{keyword}\b', re.IGNORECASE)
            formatted = pattern.sub(f'\n{keyword}', formatted)

        # 들여쓰기 추가
        lines = formatted.split('\n')
        indent_level = 0
        formatted_lines = []

        for line in lines:
            stripped_line = line.strip()
            if not stripped_line:
                continue

            # 괄호에 따른 들여쓰기 조정
            if '(' in stripped_line:
                formatted_lines.append('    ' * indent_level + stripped_line)
                indent_level += 1
            elif ')' in stripped_line:
                indent_level = max(0, indent_level - 1)
                formatted_lines.append('    ' * indent_level + stripped_line)
            else:
                formatted_lines.append('    ' * indent_level + stripped_line)

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