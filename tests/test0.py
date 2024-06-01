import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Popup Widget Example")
        self.setGeometry(100, 100, 400, 300)

        self.button = QPushButton("Open Popup", self)
        self.button.setGeometry(50, 50, 150, 30)
        self.button.clicked.connect(self.open_popup)

        # Placeholder for the popup widget
        self.popup_widget = None

    def open_popup(self):
        # Create the popup widget
        self.popup_widget = QWidget(self)
        self.popup_widget.setGeometry(0, 0, 200, 100)  # Set geometry as needed
        self.popup_widget.setStyleSheet("background-color: white; border: 1px solid black")  # Set styles
        layout = QVBoxLayout(self.popup_widget)
        label = QLabel("This is a popup!", self.popup_widget)
        layout.addWidget(label)

        # Position the popup widget relative to the button
        button_pos = self.button.pos()  # Get button position
        popup_x = button_pos.x() + self.button.width() + 5  # Adjust as needed
        popup_y = button_pos.y() + self.button.height() + 5  # Adjust as needed
        self.popup_widget.move(popup_x, popup_y)

        # Show the popup widget
        self.popup_widget.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
