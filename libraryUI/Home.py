from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget)
from PySide6.QtCore import Signal
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

        signin_button = QPushButton("Signin")
        signin_button.setStyleSheet('''
        QPushButton {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(249, 246, 236);
        background-color: rgb(182, 170, 145);
        }
        ''')
        signin_button.setFont(QFont("Vesper Libre", 25))
        from librarySystem import librarySystem
        signin_button.clicked.connect(self.signin)

        h_layout3 = QHBoxLayout()
        h_layout3.addSpacing(200)
        h_layout3.addWidget(signin_button)
        h_layout3.addSpacing(200)

        signup_button = QPushButton("Sign up")
        signup_button.setFont(QFont("Vesper Libre", 25))
        signup_button.setStyleSheet('''
                QPushButton {
                border: 3px solid rgb(132, 113, 77);
                color: rgb(249, 246, 236);
                background-color: rgb(182, 170, 145);
                }
                ''')
        from librarySystem import librarySystem
        signup_button.clicked.connect(self.signup)


        h_layout4 = QHBoxLayout()
        h_layout4.addSpacing(200)
        h_layout4.addWidget(signup_button)
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

    def signup(self):
        from librarySystem import librarySystem
        librarySystem.setState("Sign_up")
        self.close()

    def signin(self):
        from librarySystem import librarySystem
        librarySystem.setState("Sign_in")
        self.close()


if __name__ == "__main__":
    app = QApplication()
    ui = Home()
    app.exec()
