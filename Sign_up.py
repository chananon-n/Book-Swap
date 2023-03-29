
from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QDialog)
from PySide6.QtCore import Qt, QEvent
import Home
import essential


class Sign_up(QWidget):
    def __init__(self):
        super().__init__()
        label = QLabel()
        pixmap = QPixmap(u"Book_Logo.png")
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

        self.enter1 = QLineEdit("Enter the store name")
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

        v_layout = QVBoxLayout()
        v_layout.addSpacing(30)
        v_layout.addLayout(h_layout1)
        v_layout.addLayout(h_layout2)
        v_layout.addLayout(h_layout3)
        v_layout.addLayout(h_layout4)
        v_layout.addSpacing(50)

        self.setLayout(v_layout)
        self.setStyleSheet("background-color: #F9F6EC;")
        self.setWindowTitle("Sign Up")
        self.show()

        self.enter1.setFocusPolicy(Qt.NoFocus)
        self.enter1.installEventFilter(self)
        button1.clicked.connect(self.sign_up)

    def sign_up(self):
        text = self.enter1.text()
        dialog = QDialog()
        if text == "Enter the store name" or text == "":
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
            button.clicked.connect(self.back_main_menu)
        v_layout = QVBoxLayout()
        v_layout.addWidget(label)
        v_layout.addWidget(button)
        dialog.setLayout(v_layout)
        dialog.exec()

    def back_main_menu(self):
        self.home = Home.Home()
        self.close()



    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonPress:
            if source is self.enter1:
                self.enter1.setFocus()
                text = self.enter1.text()
                if text == "Enter the store name":
                    self.enter1.setText("")
            else:
                self.enter1.clearFocus()
                text = self.enter1.text()
                if text == "":
                    self.enter1.setText("Enter the store name")
        return super().eventFilter(source, event)

    def mousePressEvent(self, event):
        if not self.enter1.underMouse():
            self.enter1.clearFocus()
            text = self.enter1.text()
            if text == "":
                self.enter1.setText("Enter the store name")
        super().mousePressEvent(event)


if __name__ == "__main__":
    app = QApplication()
    ui = Sign_up()
    app.exec()
