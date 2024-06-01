from PySide6.QtWidgets import QLabel, QDoubleSpinBox, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PySide6.QtCore import Qt
from scripts.test import Expense
class SetIncome(QWidget):
    def __init__(self, front_page):
        super().__init__()
        self.front_page = front_page
        layout = QVBoxLayout()

        label = QLabel("Enter Your Income")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(self.title_style())

        self.input = QDoubleSpinBox()
        self.input.setMinimum(0.0)
        self.input.setMaximum(10000000.0)
        self.input.setDecimals(0)
        self.input.setValue(0)
        self.input.setAlignment(Qt.AlignCenter)
        self.input.setStyleSheet(self.input_style())

        buttonLayout = QHBoxLayout()
        setButton = QPushButton("Set")
        setButton.clicked.connect(self.set_button_clicked())
        buttonLayout.addWidget(setButton)
        buttonWidget = QWidget()
        buttonWidget.setLayout(buttonLayout)
        buttonWidget.setStyleSheet(self.button_style())

        layout.addWidget(label)
        layout.addWidget(self.input)
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
    
    def set_button_clicked(self):
        def update_income():
            self.front_page.income = int(self.input.text())
            self.front_page.text_fields[0].setText(str(self.front_page.income))
            self.front_page.text_fields[2].setText(str(self.front_page.income-Expense.total_expanse))
            self.front_page.stackLayout.setCurrentIndex(1)
            self.input.setValue(0)
        return update_income