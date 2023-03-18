from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit)
from PySide6.QtCore import Qt, QEvent

class Sign_in(QWidget):

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

        label1 = QLabel("ID")
        label1.setFont(QFont("Vesper Libre", 20))
        label1.setStyleSheet('''
        QLabel {
        color: rgb(132, 113, 77);
        }
        ''')

        self.enter1 = QLineEdit("Enter the ID")
        self.enter1.setFont(QFont("Vesper Libre", 20))
        self.enter1.setStyleSheet('''
        QLineEdit {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(148, 132, 99);
        }
        ''')

        label2 = QLabel("* 8 digits")
        label2.setFont(QFont("Vesper Libre", 15))
        label2.setStyleSheet('''
        QLabel {
        color: rgb(255, 0, 0);
        }
        ''')

        h_layout2 = QHBoxLayout()
        h_layout2.addWidget(label1)
        h_layout2.addSpacing(10)
        h_layout2.addWidget(self.enter1)
        h_layout2.addWidget(label2)

        button1 = QPushButton("Sign in")
        button1.setFont(QFont("Vesper Libre", 25))
        button1.setStyleSheet('''
                QPushButton {
                border: 3px solid rgb(132, 113, 77);
                color: rgb(249, 246, 236);
                background-color: rgb(182, 170, 145);
                }
                ''')

        h_layout3 = QHBoxLayout()
        h_layout3.addSpacing(200)
        h_layout3.addWidget(button1)
        h_layout3.addSpacing(200)

        v_layout = QVBoxLayout()
        v_layout.addSpacing(30)
        v_layout.addLayout(h_layout1)
        v_layout.addLayout(h_layout2)
        v_layout.addLayout(h_layout3)
        v_layout.addSpacing(50)

        self.setLayout(v_layout)
        self.setStyleSheet("background-color: #F9F6EC;")
        self.setWindowTitle("Sign in")
        self.setGeometry(400, 200, 500, 400)
        self.show()

        self.enter1.setFocusPolicy(Qt.NoFocus)
        self.enter1.installEventFilter(self)

    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonPress:
            if source is self.enter1:
                self.enter1.setFocus()
                text = self.enter1.text()
                if text == "Enter the ID":
                    self.enter1.setText("")
            else:
                self.enter1.clearFocus()
                text = self.enter1.text()
                if text == "":
                    self.enter1.setText("Enter the ID")
        return super().eventFilter(source, event)

    def mousePressEvent(self, event):
        if not self.enter1.underMouse():
            self.enter1.clearFocus()
            text = self.enter1.text()
            if text == "":
                self.enter1.setText("Enter the ID")
        super().mousePressEvent(event)


if __name__ == "__main__":
    app = QApplication()
    ui = Sign_in()
    app.exec()
