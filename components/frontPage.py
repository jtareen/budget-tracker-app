from PySide6.QtWidgets import ( QWidget, QVBoxLayout,
    QHBoxLayout, QLabel, QPushButton, QStackedLayout
)
from components.setincome import SetIncome
from components.picturewidget import PictureWidget
from components.addspend import AddSpending

from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import os

baseadress = os.path.dirname(__file__)

class FrontPage(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        layout = QVBoxLayout()

        # Title 'Dashboard'
        title_layout = QVBoxLayout()
        title = QLabel("Dashboard")
        title.setFont(QFont("Arial", 24, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        
        title_widget = QWidget()
        title_widget.setLayout(title_layout)
        title_widget.setFixedHeight(50)  # Set fixed height for the title widget
        title_layout.addWidget(title)
        layout.addWidget(title_widget)

        # Top white widgets with labels and text fields
        top_labels_text = ['Income', 'Spent', 'Remainig']
        top_layout = QHBoxLayout()
        for i in range(3):
            widget_layout = QVBoxLayout()
            label = QLabel(top_labels_text[i])
            label.setFont(QFont("Arial", 14))  # Increase label font size
            label.setAlignment(Qt.AlignCenter)  # Center align the text
            text_field = QLabel("0")
            text_field.setFont(QFont("Arial", 18, QFont.Bold))  # Increase text field font size
            text_field.setAlignment(Qt.AlignCenter)  # Center align the text
            widget_layout.addWidget(label)
            widget_layout.addWidget(text_field)
            widget_widget = QWidget()
            widget_widget.setLayout(widget_layout)
            widget_widget.setFixedSize(250, 100)
            widget_widget.setStyleSheet("""
                background-color: white;
                padding: 10px;
            """)
            top_layout.addWidget(widget_widget)
        top_layout_widget = QWidget()
        top_layout_widget.setLayout(top_layout)
        top_layout_widget.setFixedHeight(120)  # Set fixed height for the top layout widget
        layout.addWidget(top_layout_widget)

        # Blue area with label and picture
        pictureWidget = PictureWidget()
        setIncomeWidget = SetIncome()
        addSpendingWidget = AddSpending()

        self.stackLayout = QStackedLayout()
        self.stackLayout.addWidget(addSpendingWidget)
        self.stackLayout.addWidget(setIncomeWidget)
        self.stackLayout.addWidget(pictureWidget)

        layout.addLayout(self.stackLayout)

        # Bottom purple buttons
        button_labels_text = ['Set Income', 'Add Spending', 'Show Expenses']
        bottom_layout = QHBoxLayout()
        for i in range(3):
            button = QPushButton(button_labels_text[i])
            button.setFixedSize(250, 50)
            
            button.clicked.connect(self.popup(i))
            button.setCursor(Qt.PointingHandCursor)
            button.setStyleSheet("""
                QPushButton {
                    background-color: purple;
                    color: white;
                    font-weight: bold;
                    border: none;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: white;
                    color: purple;
                    border: 2px solid purple
                }
            """)
            bottom_layout.addWidget(button)
        bottom_layout_widget = QWidget()
        bottom_layout_widget.setLayout(bottom_layout)
        bottom_layout_widget.setFixedHeight(60)  # Set fixed height for the bottom layout widget
        layout.addWidget(bottom_layout_widget)

        self.setLayout(layout)

    def popup(self, index):
        if index == 1:
            self.set_income()
        elif index == 2:
            self.enter_spend()
        else:
            self.add_category()

    def set_income(self):
        pass

    def enter_spend(self):
        pass

    def add_category(self):
        pass
