from PySide6.QtWidgets import QLabel, QDoubleSpinBox, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PySide6.QtCore import Qt
class SetIncome(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()

        label = QLabel("Enter Your Income")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(self.title_style())

        input = QDoubleSpinBox()
        input.setAlignment(Qt.AlignCenter)
        input.setStyleSheet(self.input_style())

        buttonLayout = QHBoxLayout()
        setButton = QPushButton("Set")
        buttonLayout.addWidget(setButton)
        buttonWidget = QWidget()
        buttonWidget.setLayout(buttonLayout)
        buttonWidget.setStyleSheet(self.button_style())

        layout.addWidget(label)
        layout.addWidget(input)
        layout.addWidget(buttonWidget)
        
        widget = QWidget()
        widget.setLayout(layout)
        widget.setFixedSize(400, 200)
        widget.setStyleSheet("background-color: white; border: 1px solid #099eb1;")

        layout2 = QHBoxLayout()
        layout2.addWidget(widget)

        self.setLayout(layout2)

        
    
    def title_style(self):
        return """
            font-size: 20px;
            font-weight: bold;
            border: none;
        """
    
    def input_style(self):
        return """
            QDoubleSpinBox{
                font-size: 15px;
                padding: 5px;
                margin: 0 100px;
            }
            QDoubleSpinBox::up-button {
                border: none;
                width: 0px;
            }
            QDoubleSpinBox::down-button {
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
