from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QLabel, QPushButton
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from frontPage import FrontPage

class Page(QWidget):
    def __init__(self, page_number):
        super().__init__()
        layout = QVBoxLayout()

        header = QLabel(f"Page {page_number}")
        header.setFont(QFont("Arial", 24, QFont.Bold))
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)

        layout.addWidget(QLabel(f"Page {page_number} Content"))

        back_button = QPushButton("Back to Dashboard")
        back_button.clicked.connect(self.back_to_main)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def back_to_main(self):
        main_window.stack.setCurrentIndex(0)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(850, 600)  # Set fixed size for the main window
        self.setWindowTitle("Enhanced PyQt Application")

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.front_page = FrontPage(self)
        self.page2 = Page(2)
        self.page3 = Page(3)
        self.page4 = Page(4)

        self.stack.addWidget(self.front_page)
        self.stack.addWidget(self.page2)
        self.stack.addWidget(self.page3)
        self.stack.addWidget(self.page4)

        self.stack.setCurrentWidget(self.front_page)

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
