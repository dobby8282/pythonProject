import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QTextEdit, QPushButton, QFileDialog,
                             QLabel, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
import re


class DarkPalette(QPalette):
    def __init__(self):
        super().__init__()
        # 기본 색상 설정
        self.setColor(QPalette.Window, QColor(53, 53, 53))
        self.setColor(QPalette.WindowText, Qt.white)
        self.setColor(QPalette.Base, QColor(35, 35, 35))
        self.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        self.setColor(QPalette.ToolTipBase, QColor(25, 25, 25))
        self.setColor(QPalette.ToolTipText, Qt.white)
        self.setColor(QPalette.Text, Qt.white)
        self.setColor(QPalette.Button, QColor(53, 53, 53))
        self.setColor(QPalette.ButtonText, Qt.white)
        self.setColor(QPalette.BrightText, Qt.red)
        self.setColor(QPalette.Link, QColor(42, 130, 218))
        self.setColor(QPalette.Highlight, QColor(42, 130, 218))
        self.setColor(QPalette.HighlightedText, QColor(35, 35, 35))
        self.setColor(QPalette.Active, QPalette.Button, QColor(53, 53, 53))
        self.setColor(QPalette.Disabled, QPalette.ButtonText, Qt.darkGray)
        self.setColor(QPalette.Disabled, QPalette.WindowText, Qt.darkGray)
        self.setColor(QPalette.Disabled, QPalette.Text, Qt.darkGray)
        self.setColor(QPalette.Disabled, QPalette.Light, QColor(53, 53, 53))


class QueryCommentMatcher(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 메인 위젯과 레이아웃 설정
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        # 스타일 설정
        self.setStyleSheet("""
            QMainWindow {
                background-color: #353535;
            }
            QTextEdit {
                background-color: #232323;
                color: #ffffff;
                border: 1px solid #555555;
                padding: 5px;
                selection-background-color: #2a82da;
            }
            QPushButton {
                background-color: #2a82da;
                color: white;
                border: none;
                padding: 5px 15px;
                min-height: 30px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #3292ea;
            }
            QPushButton:pressed {
                background-color: #1a72ca;
            }
            QPushButton:disabled {
                background-color: #666666;
            }
            QLabel {
                color: #ffffff;
                font-weight: bold;
            }
        """)

        # 입력 영역 레이아웃
        input_layout = QHBoxLayout()

        # 쿼리 입력 영역
        query_layout = QVBoxLayout()
        self.query_edit = QTextEdit()
        self.query_edit.setPlaceholderText("여기에 쿼리를 붙여넣으세요...")
        query_label = QLabel("쿼리 입력:")
        query_layout.addWidget(query_label)
        query_layout.addWidget(self.query_edit)

        # 주석 입력 영역
        comment_layout = QVBoxLayout()
        self.comment_edit = QTextEdit()
        self.comment_edit.setPlaceholderText("여기에 주석을 붙여넣으세요...")
        comment_label = QLabel("주석 입력:")
        comment_layout.addWidget(comment_label)
        comment_layout.addWidget(self.comment_edit)

        # 입력 영역들을 수평 레이아웃에 추가
        input_layout.addLayout(query_layout)
        input_layout.addLayout(comment_layout)

        # 결과 출력 영역
        result_label = QLabel("결과:")
        self.result_edit = QTextEdit()
        self.result_edit.setReadOnly(True)

        # 버튼 영역
        button_layout = QHBoxLayout()

        self.process_btn = QPushButton('처리하기')
        self.process_btn.clicked.connect(self.process_queries)

        self.save_btn = QPushButton('저장하기')
        self.save_btn.clicked.connect(self.save_result)

        self.clear_btn = QPushButton('초기화')
        self.clear_btn.clicked.connect(self.clear_all)

        button_layout.addWidget(self.process_btn)
        button_layout.addWidget(self.save_btn)
        button_layout.addWidget(self.clear_btn)

        # 메인 레이아웃에 모든 요소 추가
        layout.addLayout(input_layout)
        layout.addWidget(result_label)
        layout.addWidget(self.result_edit)
        layout.addLayout(button_layout)

        # 윈도우 설정
        self.setGeometry(100, 100, 1200, 800)
        self.setWindowTitle('Query Comment Matcher - Dark Theme')
        self.show()

    def process_queries(self):
        query_text = self.query_text = self.query_edit.toPlainText()
        comment_text = self.comment_edit.toPlainText()

        if not query_text or not comment_text:
            QMessageBox.warning(self, '경고', '쿼리와 주석을 모두 입력해주세요.')
            return

        try:
            # 주석 파싱
            comments = {}
            for line in comment_text.split('\n'):
                if line.startswith('-- Query #'):
                    match = re.match(r'-- Query #(\d+): (.+)', line)
                    if match:
                        number, comment = match.groups()
                        comments[number] = comment

            # 쿼리 처리
            queries = query_text.split('--- Query #')
            result = []

            # 첫 번째 빈 부분 처리
            if queries[0].strip() == '':
                queries.pop(0)

            for query in queries:
                if not query.strip():
                    continue

                # 쿼리 번호 추출
                match = re.match(r'(\d+) ---', query)
                if match:
                    number = match.group(1)
                    # 해당하는 주석 찾기
                    if number in comments:
                        # 쿼리 시작 부분에 주석 삽입
                        query_parts = query.split('---', 1)
                        if len(query_parts) > 1:
                            commented_query = (f"{query_parts[0]}---\n"
                                               f"-- {comments[number]}\n"
                                               f"{query_parts[1]}")
                            result.append(f"--- Query #{commented_query}")
                    else:
                        result.append(f"--- Query #{query}")

            # 결과 표시
            self.result_edit.setPlainText(''.join(result))
            QMessageBox.information(self, '성공', '쿼리 처리가 완료되었습니다.')

        except Exception as e:
            QMessageBox.critical(self, '오류', f'처리 중 오류가 발생했습니다: {str(e)}')

    def save_result(self):
        if not self.result_edit.toPlainText():
            QMessageBox.warning(self, '경고', '저장할 결과가 없습니다.')
            return

        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "결과 저장",
            "",
            "Text Files (*.txt);;All Files (*)"
        )

        if file_name:
            try:
                with open(file_name, 'w', encoding='utf-8') as f:
                    f.write(self.result_edit.toPlainText())
                QMessageBox.information(self, '성공', '파일이 저장되었습니다.')
            except Exception as e:
                QMessageBox.critical(self, '오류', f'파일 저장 중 오류가 발생했습니다: {str(e)}')

    def clear_all(self):
        reply = QMessageBox.question(
            self, '확인',
            '모든 내용을 초기화하시겠습니까?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.query_edit.clear()
            self.comment_edit.clear()
            self.result_edit.clear()


def setup_dark_theme():
    # 다크 테마 설정을 위한 팔레트 생성 및 적용
    app = QApplication.instance()
    app.setStyle("Fusion")
    app.setPalette(DarkPalette())

    # 메시지 박스 스타일 설정
    app.setStyleSheet("""
        QMessageBox {
            background-color: #353535;
            color: #ffffff;
        }
        QMessageBox QLabel {
            color: #ffffff;
        }
        QMessageBox QPushButton {
            background-color: #2a82da;
            color: white;
            border: none;
            padding: 5px 15px;
            min-width: 65px;
            min-height: 25px;
            border-radius: 4px;
        }
        QMessageBox QPushButton:hover {
            background-color: #3292ea;
        }
        QFileDialog {
            background-color: #353535;
            color: #ffffff;
        }
        QFileDialog QLabel {
            color: #ffffff;
        }
        QFileDialog QComboBox {
            background-color: #232323;
            color: #ffffff;
            border: 1px solid #555555;
        }
        QFileDialog QListView {
            background-color: #232323;
            color: #ffffff;
            border: 1px solid #555555;
        }
    """)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    setup_dark_theme()
    ex = QueryCommentMatcher()
    sys.exit(app.exec_())