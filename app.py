from PySide6.QtWidgets import (
    QApplication, QMainWindow,
)
from components.frontPage import FrontPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(850, 600)  # Set fixed size for the main window
        self.setWindowTitle("Enhanced PyQt Application")

        self.front_page = FrontPage(self)
        self.setCentralWidget(self.front_page)

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()