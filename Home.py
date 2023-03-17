# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Home.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Home(QWidget):
    def __init__(self):
        super().__init__()
        label = QLabel()
        pixmap = QPixmap(u"Book_Logo.png")
        label.setPixmap(pixmap)
        blank = QLabel("")

        h_layout2 = QHBoxLayout()
        h_layout2.addWidget(blank)
        h_layout2.addWidget(label)
        h_layout2.addWidget(blank)

        button1 = QPushButton()
        button1.setStyleSheet('''
        QPushButton {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(249, 246, 236);
        background-color: rgb(182, 170, 145);
        }
        ''')
        button1.setText("Signin")
        button1.setFont(QFont("Vesper Libre", 25))


        h_layout3 = QHBoxLayout()
        h_layout3.addSpacing(200)
        h_layout3.addWidget(button1)
        h_layout3.addSpacing(200)


        button2 = QPushButton("Sign up")
        button2.setFont(QFont("Vesper Libre", 25))
        button2.setStyleSheet('''
                QPushButton {
                border: 3px solid rgb(132, 113, 77);
                color: rgb(249, 246, 236);
                background-color: rgb(182, 170, 145);
                }
                ''')


        h_layout4 = QHBoxLayout()
        h_layout4.addSpacing(200)
        h_layout4.addWidget(button2)
        h_layout4.addSpacing(200)

        v_layout = QVBoxLayout()
        v_layout.addSpacing(30)
        v_layout.addLayout(h_layout2)
        v_layout.addLayout(h_layout3)
        v_layout.addLayout(h_layout4)
        v_layout.addSpacing(50)

        myColor = '#920310'
        self.setLayout(v_layout)
        self.setStyleSheet("background-color: #F9F6EC;")
        self.setWindowTitle("Home")
        self.show()


if __name__ == "__main__":
    app = QApplication()
    ui = Home()
    app.exec()