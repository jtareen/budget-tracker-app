from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap

import os

baseadress = os.path.dirname(__file__)


class PictureWidget(QWidget):
    def __init__(self):
        super().__init__()

        picture_layout = QVBoxLayout()
        
        picture_label_layout = QVBoxLayout()
        picture_label = QLabel("Graphical Representation of Expenses")
        picture_label.setFont(QFont("Arial", 12, QFont.Bold))
        picture_label.setAlignment(Qt.AlignCenter)
        picture_label_widget = QWidget()
        picture_label_widget.setLayout(picture_label_layout)
        picture_label_widget.setFixedHeight(30)
        picture_label_layout.addWidget(picture_label)
        picture_layout.addWidget(picture_label_widget)
        
        picture = QLabel()
        pixmap = QPixmap(os.path.join(baseadress, '../assets/graph.png'))
        picture.setPixmap(pixmap.scaled(750, 300, Qt.KeepAspectRatio))
        picture.setAlignment(Qt.AlignCenter)
        picture.setStyleSheet("""
            background-color: white;
            border: 1px solid #ccc;
            border-radius: 10px;
        """)
        
        picture_layout.addWidget(picture)
        self.setLayout(picture_layout)
        