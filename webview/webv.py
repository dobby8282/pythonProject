import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QFileDialog
)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineProfile
from PyQt6.QtCore import QUrl, QLocale


class WebEnginePage(QWebEnginePage):
    def __init__(self, profile, parent=None):
        super().__init__(profile, parent)

    def createWindow(self, _type):
        # 팝업 창 생성
        new_window = PopupWindow(self.profile(), self.parent())
        new_window.show()
        return new_window.web_view.page()


class PopupWindow(QMainWindow):
    def __init__(self, profile, parent=None):
        super().__init__(parent)
        self.setWindowTitle('팝업 창')
        self.setGeometry(200, 200, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 팝업 창에도 URL 바
        nav_layout = QHBoxLayout()
        self.url_bar = QLineEdit()
        # 팝업창은 직접 주소창을 입력해서 이동하는 기능을 예제로 넣어도 되고,
        # 단순히 보기만 원하시면 returnPressed 연결은 제외하셔도 됩니다.
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav_layout.addWidget(self.url_bar)
        layout.addLayout(nav_layout)

        self.web_view = QWebEngineView()
        self.web_view.setPage(WebEnginePage(profile, self.web_view))

        # 팝업창의 URL이 바뀔 때마다 주소창도 갱신
        self.web_view.urlChanged.connect(self.update_url_bar)

        layout.addWidget(self.web_view)

    def update_url_bar(self, url):
        self.url_bar.setText(url.toString())

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        self.web_view.setUrl(QUrl(url))


class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('파이썬 웹 브라우저')
        self.setGeometry(100, 100, 1024, 768)

        # 시스템 로케일 설정 가져오기
        locale = QLocale.system()
        country_code = locale.name().split('_')[1].lower()  # 예: ko_KR -> kr
        self.home_url = f"https://www.google.com/?hl={locale.name()[:2]}&gl={country_code}"

        # 웹 엔진 프로필 설정
        self.profile = QWebEngineProfile.defaultProfile()
        self.profile.setPersistentCookiesPolicy(QWebEngineProfile.PersistentCookiesPolicy.AllowPersistentCookies)

        # 언어 설정
        self.profile.setHttpAcceptLanguage(locale.name().replace('_', '-'))

        # 파일 다운로드 시그널 연결
        self.profile.downloadRequested.connect(self.handle_download_requested)

        # 중앙 위젯 생성
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 메인 레이아웃
        layout = QVBoxLayout(central_widget)

        # 네비게이션 바 생성
        nav_layout = QHBoxLayout()

        # 홈 버튼
        self.home_button = QPushButton('홈')
        self.home_button.setToolTip('홈으로')
        self.home_button.clicked.connect(self.go_home)
        nav_layout.addWidget(self.home_button)

        # 뒤로가기 버튼
        self.back_button = QPushButton('←')
        self.back_button.clicked.connect(self.navigate_back)
        nav_layout.addWidget(self.back_button)

        # 앞으로가기 버튼
        self.forward_button = QPushButton('→')
        self.forward_button.clicked.connect(self.navigate_forward)
        nav_layout.addWidget(self.forward_button)

        # 새로고침 버튼
        self.reload_button = QPushButton('↻')
        self.reload_button.clicked.connect(self.reload_page)
        nav_layout.addWidget(self.reload_button)

        # URL 입력창
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav_layout.addWidget(self.url_bar)

        # 이동 버튼
        self.go_button = QPushButton('이동')
        self.go_button.clicked.connect(self.navigate_to_url)
        nav_layout.addWidget(self.go_button)

        # 레이아웃에 네비게이션 바 추가
        layout.addLayout(nav_layout)

        # 웹뷰 생성 및 설정
        self.web_view = QWebEngineView()
        self.web_view.setPage(WebEnginePage(self.profile, self.web_view))

        # 자바스크립트 팝업 허용 설정
        settings = self.web_view.page().settings()
        settings.setAttribute(settings.WebAttribute.JavascriptEnabled, True)
        settings.setAttribute(settings.WebAttribute.JavascriptCanOpenWindows, True)
        settings.setAttribute(settings.WebAttribute.AllowWindowActivationFromJavaScript, True)

        # 초기 URL을 홈 URL로 설정
        self.web_view.setUrl(QUrl(self.home_url))

        # URL 변경 시그널 연결
        self.web_view.urlChanged.connect(self.update_url_bar)

        # 레이아웃에 웹뷰 추가
        layout.addWidget(self.web_view)

        # 초기 버튼 상태 설정
        self.update_navigation_buttons()

        # 네비게이션 상태 변경 시그널 연결
        self.web_view.loadFinished.connect(self.update_navigation_buttons)

    def handle_download_requested(self, download):
        """
        다운로드 요청이 발생하면 저장 위치를 묻고 파일을 저장합니다.
        """
        suggested_filename = download.downloadFileName()
        # 파일 저장 대화상자
        save_path, _ = QFileDialog.getSaveFileName(self, "파일 저장", suggested_filename)
        if save_path:
            download.setPath(save_path)
            download.accept()

    def go_home(self):
        self.web_view.setUrl(QUrl(self.home_url))

    def navigate_back(self):
        self.web_view.back()

    def navigate_forward(self):
        self.web_view.forward()

    def reload_page(self):
        self.web_view.reload()

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        self.web_view.setUrl(QUrl(url))

    def update_url_bar(self, url):
        self.url_bar.setText(url.toString())
        self.url_bar.setCursorPosition(0)

    def update_navigation_buttons(self):
        self.back_button.setEnabled(self.web_view.history().canGoBack())
        self.forward_button.setEnabled(self.web_view.history().canGoForward())


def main():
    app = QApplication(sys.argv)
    browser = WebBrowser()
    browser.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
