from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget)
from PySide6.QtCore import Qt, Signal
import os


class Home(QWidget):
    buttonClicked = Signal(str)  # Custom signal for button clicks

    def __init__(self):
        super().__init__()
        # Get the absolute path of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        label = QLabel()
        pixmap = QPixmap(os.path.join(script_dir, u"../resources/Book_Logo.png"))
        label.setPixmap(pixmap)
        blank = QLabel("")

        h_layout2 = QHBoxLayout()
        h_layout2.addWidget(blank)
        h_layout2.addWidget(label)
        h_layout2.addWidget(blank)

        Signin_button = QPushButton("Signin")
        Signin_button.setStyleSheet('''
        QPushButton {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(249, 246, 236);
        background-color: rgb(182, 170, 145);
        }
        ''')
        Signin_button.setFont(QFont("Vesper Libre", 25))
        Signin_button.clicked.connect(lambda: self.handleButtonClicked("Sign_in"))  # Emit signal for Sign_in button

        h_layout3 = QHBoxLayout()
        h_layout3.addSpacing(200)
        h_layout3.addWidget(Signin_button)
        h_layout3.addSpacing(200)

        Signup_button = QPushButton("Sign up")
        Signup_button.setFont(QFont("Vesper Libre", 25))
        Signup_button.setStyleSheet('''
                QPushButton {
                border: 3px solid rgb(132, 113, 77);
                color: rgb(249, 246, 236);
                background-color: rgb(182, 170, 145);
                }
                ''')
        Signup_button.clicked.connect(lambda: self.handleButtonClicked("Sign_up"))  # Emit signal for Sign_up button

        h_layout4 = QHBoxLayout()
        h_layout4.addSpacing(200)
        h_layout4.addWidget(Signup_button)
        h_layout4.addSpacing(200)

        v_layout = QVBoxLayout()
        v_layout.addSpacing(30)
        v_layout.addLayout(h_layout2)
        v_layout.addLayout(h_layout3)
        v_layout.addLayout(h_layout4)
        v_layout.addSpacing(50)

        self.setLayout(v_layout)
        self.setStyleSheet("background-color: #F9F6EC;")
        self.setWindowTitle("Home")
        self.setGeometry(400, 200, 800, 500)
        self.show()

    def handleButtonClicked(self, button_name):
        self.buttonClicked.emit(button_name)  # Emit the buttonClicked signal with the button name


if __name__ == "__main__":
    app = QApplication()
    ui = Home()
    app.exec()
