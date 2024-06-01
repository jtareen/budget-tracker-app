from PySide6.QtWidgets import (
    QLabel,
    QComboBox,
    QDoubleSpinBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget
)
from PySide6.QtCore import Qt
from scripts.test import Expense

class AddSpending(QWidget):
    def __init__(self, front_page):
        super().__init__()
        self.front_page = front_page
        self.expense_list = []

        for i in self.front_page.expenses:
            self.expense_list.append(i.get_name())
        
        self.layout = QVBoxLayout()

        self.label = QLabel("Enter Spendings")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet(self.title_style())

        self.inputLayout = QVBoxLayout()

        self.input1Layout = QHBoxLayout()
        self.input1Label = QLabel("Amount :")
        self.input1Label.setStyleSheet("")
        self.input1 = QDoubleSpinBox()
        self.input1.setMinimum(0.0)
        self.input1.setMaximum(10000000.0)
        self.input1.setDecimals(0)
        self.input1.setValue(0)
        self.input1Layout.addWidget(self.input1Label)
        self.input1Layout.addWidget(self.input1)
        self.input1widget = QWidget()
        self.input1widget.setLayout(self.input1Layout)

        self.input2Layout = QHBoxLayout()
        self.input2Label = QLabel("Category :")
        self.input2 = QComboBox()
        self.input2.addItems(self.expense_list)
        self.input2Layout.addWidget(self.input2Label)
        self.input2Layout.addWidget(self.input2)
        self.input2widget = QWidget()
        self.input2widget.setLayout(self.input2Layout)

        self.inputLayout.setContentsMargins(0, 0, 0, 0)
        self.inputLayout.setSpacing(0)
        self.inputLayout.addWidget(self.input1widget)
        self.inputLayout.addWidget(self.input2widget)
        self.inputwidget = QWidget()
        self.inputwidget.setStyleSheet(self.input_style())
        self.inputwidget.setLayout(self.inputLayout)

        self.buttonLayout = QHBoxLayout()
        self.setButton = QPushButton("Enter")
        self.setButton.clicked.connect(self.enter_button_clicked())
        self.buttonLayout.addWidget(self.setButton)
        self.buttonWidget = QWidget()
        self.buttonWidget.setLayout(self.buttonLayout)
        self.buttonWidget.setStyleSheet(self.button_style())

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.inputwidget)
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
            QWidget{
                border: none;
            }
            QLabel{
                padding: 3px;
                font-size: 12px;
                font-weight: 700;
            }
            QComboBox, QDoubleSpinBox{
                padding: 5px;
                font-size: 12px;
                border: 1px solid #099eb1;     
            }
            QDoubleSpinBox::up-button {
                border: none;
                width: 0px;
            }
            QDoubleSpinBox::down-button {
                border: none;
                width: 0px;
            }
            QComboBox::drop-down{
                background-image: url('./assets/downarrow.png');
                width: 20px;
                height: 20px;
                background-color: #099eb1;
                border: 1px solid #099eb1;
            }
            QComboBox::drop-down:hover{
                border: 1px solid white;
            }
            QComboBox::down-arrow{
                width: 20px;
                height: 20px;
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
    
    def enter_button_clicked(self):
        def enter_spending():
            amount = self.input1.text()
            index = self.input2.currentIndex()
            self.input1.setValue(0)
            self.input2.setCurrentIndex(0)
            self.front_page.expenses[index].add_amount(int(amount))
            self.front_page.text_fields[1].setText(str(Expense.total_expanse))
            self.front_page.text_fields[2].setText(str(self.front_page.income-Expense.total_expanse))
            
        return enter_spending