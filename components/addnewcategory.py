from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QApplication
from PySide6.QtCore import Qt
class AddCategory(QWidget):
    def __init__(self):
        super().__init__()
        
        self.layout = QVBoxLayout()

        self.label = QLabel("Enter new expense category")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet(self.title_style())

        self.input = QLineEdit()
        self.input.setAlignment(Qt.AlignCenter)
        self.input.setStyleSheet(self.input_style())

        self.buttonLayout = QHBoxLayout()
        self.cancel = QPushButton("Cancel")
        self.setButton = QPushButton("Add")
        self.buttonLayout.addWidget(self.cancel)
        self.buttonLayout.addWidget(self.setButton)
        self.buttonWidget = QWidget()
        self.buttonWidget.setLayout(self.buttonLayout)
        self.buttonWidget.setStyleSheet(self.button_style())

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.buttonWidget)
        
        widget = QWidget()
        widget.setLayout(self.layout)
        widget.setFixedSize(400, 200)
        widget.setStyleSheet("background-color: white; border: 1px solid #099eb1;")

        self.layout2 = QHBoxLayout()
        self.layout2.addWidget(widget)

        self.setLayout(self.layout2)

        
    
    def title_style(self):
        return """
            font-size: 20px;
            font-weight: bold;
            border: none;
        """
    
    def input_style(self):
        return """
            QLineEdit{
                font-size: 15px;
                padding: 5px;
                margin: 0 100px;
            }
            QLineEdit::up-button {
                border: none;
                width: 0px;
            }
            QLineEdit::down-button {
                border: none;
                width: 0px;
            }
        """
    
    def button_style(self):
        return """
            QWidget{
                border: none;
            }
            QPushButton{
                background-color: #099eb1;
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 8px;
                border: none;
                margin: 3px;
            }
            QPushButton::hover{
                background-color: white;
                color: #099eb1;
                border: 2px solid #099eb1;
            }
        """


if __name__ == "__main__":
    app = QApplication([])
    w = AddCategory()
    w.show()
    app.exec()