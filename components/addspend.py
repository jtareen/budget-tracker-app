from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QComboBox,
    QDoubleSpinBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget
)
from PySide6.QtCore import Qt
class AddSpending(QWidget):
    def __init__(self):
        super().__init__()
        
        self.layout = QVBoxLayout()

        self.label = QLabel("Enter Spendings")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet(self.title_style())

        self.inputLayout = QVBoxLayout()

        self.input1Layout = QHBoxLayout()
        self.input1Label = QLabel("Amount :")
        self.input1Label.setStyleSheet("")
        self.input1 = QDoubleSpinBox()
        self.input1Layout.addWidget(self.input1Label)
        self.input1Layout.addWidget(self.input1)
        self.input1widget = QWidget()
        self.input1widget.setLayout(self.input1Layout)

        self.input2Layout = QHBoxLayout()
        self.input2Label = QLabel("Category :")
        self.input2 = QComboBox()
        self.input2.addItems(["item1", "item2", "item3", "item4", "item5"])
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
        self.cancel = QPushButton("Cancel")
        self.setButton = QPushButton("Enter")
        self.buttonLayout.addWidget(self.cancel)
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
            QComboBox{
                
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
    w = AddSpending()
    w.show()
    app.exec()