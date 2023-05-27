import os
from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QDialog)
from PySide6.QtCore import Qt


class Sign_up(QWidget):
    def __init__(self):
        super().__init__()
        # Get the absolute path of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        label = QLabel()
        pixmap = QPixmap(os.path.join(script_dir, u"../resources/Book_Logo.png"))
        label.setPixmap(pixmap)
        blank = QLabel("")

        h_layout1 = QHBoxLayout()
        h_layout1.addWidget(blank)
        h_layout1.addWidget(label)
        h_layout1.addWidget(blank)

        label1 = QLabel("Store name")
        label1.setFont(QFont("Vesper Libre", 25))
        label1.setStyleSheet('''
        QLabel {
        color: rgb(132, 113, 77);
        }
        ''')

        h_layout2 = QHBoxLayout()
        h_layout2.addSpacing(60)
        h_layout2.addWidget(label1)

        self.enter1 = QLineEdit(self)
        self.enter1.setPlaceholderText("Enter the store name")
        self.enter1.setFont(QFont("Vesper Libre", 20))
        self.enter1.setStyleSheet('''
        QLineEdit {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(148, 132, 99);
        }
        ''')

        h_layout3 = QHBoxLayout()
        h_layout3.addSpacing(60)
        h_layout3.addWidget(self.enter1)
        h_layout3.addSpacing(60)

        button1 = QPushButton("Sign up")
        button1.setFont(QFont("Vesper Libre", 25))
        button1.setStyleSheet('''
                QPushButton {
                border: 3px solid rgb(132, 113, 77);
                color: rgb(249, 246, 236);
                background-color: rgb(182, 170, 145);
                }
                ''')

        h_layout4 = QHBoxLayout()
        h_layout4.addSpacing(200)
        h_layout4.addWidget(button1)
        h_layout4.addSpacing(200)

        al_ac = QLabel("Already have an account?")
        al_ac.setFont(QFont("Vesper Libre", 13))
        al_ac.setStyleSheet('''QLabel {
                color: rgb(182, 170, 145);
            }''')

        button2 = QPushButton("Sign in")
        button2.setFont(QFont("Vesper Libre", 13))
        button2.setStyleSheet('''
        QPushButton {
                border: none;
                color: rgb(132, 113, 77);
                background-color: #F9F6EC;
                text-decoration: underline;
            }

            QPushButton:hover {
                background-color: transparent;
            }
        ''')
        button2.clicked.connect(self.sign_in)

        h_layout5 = QHBoxLayout()
        h_layout5.addSpacing(330)
        h_layout5.addWidget(al_ac)
        h_layout5.addWidget(button2)
        h_layout5.addSpacing(330)

        v_layout = QVBoxLayout()
        v_layout.addSpacing(30)
        v_layout.addLayout(h_layout1)
        v_layout.addLayout(h_layout2)
        v_layout.addLayout(h_layout3)
        v_layout.addLayout(h_layout4)
        v_layout.addLayout(h_layout5)
        v_layout.addSpacing(50)

        self.setLayout(v_layout)
        self.setStyleSheet("background-color: #F9F6EC;")
        self.setWindowTitle("Sign Up")
        self.setGeometry(400, 200, 800, 500)
        self.show()
        button1.clicked.connect(self.sign_up)

    def sign_up(self):
        store_name = self.enter1.text()
        dialog = QDialog()
        if store_name == "Enter the store name" or store_name.strip(" ") == "":
            dialog.setWindowTitle("Error")
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog.resize(300, 100)
            label = QLabel("Please enter the store name")
            label.setFont(QFont("Vesper Libre", 15))
            label.setStyleSheet('''
            QLabel {
            color: rgb(132, 113, 77);
            }
            ''')
            button = QPushButton("OK")
            button.setFont(QFont("Vesper Libre", 15))
            button.setStyleSheet('''
            QPushButton {
            border: 3px solid rgb(132, 113, 77);
            color: rgb(249, 246, 236);
            background-color: rgb(182, 170, 145);
            }
            ''')
            v_layout = QVBoxLayout()
            v_layout.addWidget(label)
            v_layout.addWidget(button)
            dialog.setLayout(v_layout)
            button.clicked.connect(dialog.close)
        else:
            dialog.setWindowTitle("Success")
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog.resize(300, 100)
            label = QLabel("Sign up successfully")
            label.setFont(QFont("Vesper Libre", 15))
            label.setStyleSheet('''QLabel {
            color: rgb(132, 113, 77);
            }
            ''')
            from librarySystem import librarySystem
            user = QLabel("Your ID is " + f"{librarySystem.createUserID(store_name)}")
            user.setFont(QFont("Vesper Libre", 15))
            user.setStyleSheet('''QLabel {
                        color: rgb(132, 113, 77);
                        }
                        ''')
            id_create = QLabel("Please remember your ID")
            id_create.setFont(QFont("Vesper Libre", 15))
            id_create.setStyleSheet('''QLabel {
                        color: rgb(132, 113, 77);
                        }
                        ''')
            button = QPushButton("OK")
            button.setFont(QFont("Vesper Libre", 15))
            button.setStyleSheet('''
            QPushButton {
            border: 3px solid rgb(132, 113, 77);
            color: rgb(249, 246, 236);
            background-color: rgb(182, 170, 145);
            }
            ''')
            button.clicked.connect(dialog.close)
            button.clicked.connect(self.home)
            v_layout = QVBoxLayout()
            v_layout.addWidget(label)
            v_layout.addWidget(user)
            v_layout.addWidget(id_create)
            v_layout.addWidget(button)
            dialog.setLayout(v_layout)
        dialog.exec()

    def home(self):
        from librarySystem import librarySystem
        librarySystem.setState("Home")
        self.close()

    def sign_in(self):
        from librarySystem import librarySystem
        librarySystem.setState("Sign_in")
        self.close()
