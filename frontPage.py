from PyQt5.QtWidgets import ( QWidget, QVBoxLayout,
    QHBoxLayout, QLabel, QPushButton
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

class FrontPage(QWidget):
    def __init__(self, main_win):
        super().__init__()
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
        top_layout = QHBoxLayout()
        for i in range(3):
            widget_layout = QVBoxLayout()
            label = QLabel(f"Label {i + 1}")
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
        pixmap = QPixmap('./graph.png')
        picture.setPixmap(pixmap.scaled(750, 300, Qt.KeepAspectRatio))
        picture.setAlignment(Qt.AlignCenter)
        picture.setStyleSheet("""
            background-color: white;
            border: 1px solid #ccc;
            border-radius: 10px;
        """)
        
        picture_layout.addWidget(picture)
        picture_widget = QWidget()
        picture_widget.setLayout(picture_layout)
        
        layout.addWidget(picture_widget)

        # Bottom purple buttons
        bottom_layout = QHBoxLayout()
        for i in range(3):
            button = QPushButton(f"Page {i + 2}")
            button.setFixedSize(250, 50)
            
            button.clicked.connect(self.navigate_to_page(i + 1, main_win))
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

    def navigate_to_page(self, index, main_win):
        def switch():
            main_win.stack.setCurrentIndex(index)
        return switch
