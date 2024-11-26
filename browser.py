from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Browser")
        self.browser = QWebEngineView()
        self.browser.setUrl("https://google.com")

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.browser.back)

        self.forward_button = QPushButton("Forward")
        self.forward_button.clicked.connect(self.browser.forward)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.url_bar)
        self.layout.addWidget(self.back_button)
        self.layout.addWidget(self.forward_button)
        self.layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = f"http://{url}"
        self.browser.setUrl(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec_())
