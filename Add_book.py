from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit,
                               QTextEdit, QCheckBox, QScrollArea)
from PySide6.QtCore import Qt, QEvent
from Sign_in import Sign_in  # change to main menu by your self na non , left only import sign in and from and import


# use in main menu instead


class Add_book(QWidget):
    def __init__(self):
        super().__init__()
        self.sign_in = None
        book_image = QLabel()
        pixmap = QPixmap(u"png")
        book_image.setPixmap(pixmap)
        blank = QLabel("")

        h_layout1 = QHBoxLayout()
        h_layout1.addWidget(blank)
        h_layout1.addWidget(book_image)
        h_layout1.addWidget(blank)

        title = QLabel("Title")
        title.setFont(QFont("Vesper Libre", 25))
        title.setStyleSheet('''
        QLabel {
        color: rgb(132, 113, 77);
        }
        ''')

        self.title_name = QLineEdit(self)
        self.title_name.setPlaceholderText("Enter title")
        self.title_name.setFont(QFont("Vesper Libre", 20))
        self.title_name.setStyleSheet('''
        QLineEdit {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(148, 132, 99);
        }
        ''')

        h_layout2 = QHBoxLayout()
        h_layout2.addSpacing(30)
        h_layout2.addWidget(title)
        h_layout2.addSpacing(40)
        h_layout2.addWidget(self.title_name)
        h_layout2.addSpacing(30)

        author = QLabel("Author")
        author.setFont(QFont("Vesper Libre", 20))
        author.setStyleSheet('''
        QLabel {
        color: rgb(132, 113, 77);
        }
        ''')

        self.author_name = QLineEdit(self)
        self.author_name.setPlaceholderText("Enter the author")
        self.author_name.setFont(QFont("Vesper Libre", 25))
        self.author_name.setStyleSheet('''
        QLineEdit {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(148, 132, 99);
        }
        ''')

        h_layout3 = QHBoxLayout()
        h_layout3.addSpacing(30)
        h_layout3.addWidget(author)
        h_layout3.addSpacing(15)
        h_layout3.addWidget(self.author_name)
        h_layout3.addSpacing(30)

        description = QLabel("Description")
        description.setFont(QFont("Vesper Libre", 20))
        description.setStyleSheet('''
        QLabel {
        color: rgb(132, 113, 77);
        }
        ''')

        h_layout4 = QHBoxLayout()
        h_layout4.addSpacing(30)
        h_layout4.addWidget(description)

        self.description_name = QTextEdit("Enter the description")
        self.description_name.setFont(QFont("Vesper Libre", 25))
        self.description_name.setStyleSheet('''
        QTextEdit   {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(148, 132, 99);
        }
        ''')


        h_layout5 = QHBoxLayout()
        h_layout5.addSpacing(50)
        h_layout5.addWidget(self.description_name)
        h_layout5.addSpacing(30)

        category = QLabel("Category")
        category.setFont(QFont("Vesper Libre", 25))
        category.setStyleSheet('''
        QLabel {
        color: rgb(132, 113, 77);
        }
        ''')

        h_layout6 = QHBoxLayout()
        h_layout6.addSpacing(30)
        h_layout6.addWidget(category)

        Romance_button = QCheckBox("Romance")
        Romance_button.setChecked(False)
        Romance_button.book = "Romance"
        Romance_button.setFont(QFont("Vesper Libre", 20))
        Romance_button.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')
        Romance_button.toggled.connect(self.OnCLickedRomance)

        Mystery_button = QCheckBox("Mystery")
        Mystery_button.setChecked(False)
        Mystery_button.book = "Mystery"
        Mystery_button.setFont(QFont("Vesper Libre", 20))
        Mystery_button.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')
        Mystery_button.toggled.connect(self.OnCLickedMystery)

        h_layout7 = QHBoxLayout()
        h_layout7.addSpacing(50)
        h_layout7.addWidget(Romance_button)
        h_layout7.addSpacing(45)
        h_layout7.addWidget(Mystery_button)

        Fantasy_and_science_fiction_button = QCheckBox("Fantasy and science fiction")
        Fantasy_and_science_fiction_button.setChecked(False)
        Fantasy_and_science_fiction_button.book = "Fantasy and science fiction"
        Fantasy_and_science_fiction_button.setFont(QFont("Vesper Libre", 20))
        Fantasy_and_science_fiction_button.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')
        Fantasy_and_science_fiction_button.toggled.connect(self.OnCLickedFantasy_and_science_fiction)

        Thrillers_horror_button = QCheckBox("Thrillers and horror")
        Thrillers_horror_button.setChecked(False)
        Thrillers_horror_button.book = "Thrillers and horror"
        Thrillers_horror_button.setFont(QFont("Vesper Libre", 20))
        Thrillers_horror_button.setStyleSheet('''
                QCheckBox {
                color: rgb(132, 113, 77);
                }
                ''')
        Thrillers_horror_button.toggled.connect(self.OnCLickedThrillers_horror)

        h_layout8 = QHBoxLayout()
        h_layout8.addSpacing(50)
        h_layout8.addWidget(Fantasy_and_science_fiction_button)
        h_layout8.addSpacing(45)
        h_layout8.addWidget(Thrillers_horror_button)

        Young_adult_button = QCheckBox("Young adult")
        Young_adult_button.setChecked(False)
        Young_adult_button.book = "Young adult"
        Young_adult_button.setFont(QFont("Vesper Libre", 20))
        Young_adult_button.setStyleSheet('''
                QCheckBox {
                color: rgb(132, 113, 77);
                }
                ''')
        Young_adult_button.toggled.connect(self.OnCLickedYoung_adult)

        Children_fiction_button = QCheckBox("Children’s fiction")
        Children_fiction_button.setChecked(False)
        Children_fiction_button.book = "Children’s fiction"
        Children_fiction_button.setFont(QFont("Vesper Libre", 20))
        Children_fiction_button.setStyleSheet('''
                        QCheckBox {
                        color: rgb(132, 113, 77);
                        }
                        ''')
        Children_fiction_button.toggled.connect(self.OnCLickedChildren_fiction)

        h_layout9 = QHBoxLayout()
        h_layout9.addSpacing(50)
        h_layout9.addWidget(Young_adult_button)
        h_layout9.addSpacing(45)
        h_layout9.addWidget(Children_fiction_button)

        Inspirational_and_religious_button = QCheckBox("Inspirational and religious")
        Inspirational_and_religious_button.setChecked(False)
        Inspirational_and_religious_button.book = "Children’s fiction"
        Inspirational_and_religious_button.setFont(QFont("Vesper Libre", 20))
        Inspirational_and_religious_button.setStyleSheet('''
                                QCheckBox {
                                color: rgb(132, 113, 77);
                                }
                                ''')
        Inspirational_and_religious_button.toggled.connect(self.OnCLickedInspirational_and_religious)

        Biography_and_autobiography_button = QCheckBox("Biography and autobiography")
        Biography_and_autobiography_button.setChecked(False)
        Biography_and_autobiography_button.book = "Biography and autobiography"
        Biography_and_autobiography_button.setFont(QFont("Vesper Libre", 20))
        Biography_and_autobiography_button.setStyleSheet('''                                           
                                        QCheckBox {                                                            
                                        color: rgb(132, 113, 77);                                              
                                        }                                                                      
                                        ''')
        Biography_and_autobiography_button.toggled.connect(self.OnCLickedInspirational_and_religious)

        h_layout10 = QHBoxLayout()
        h_layout10.addSpacing(50)
        h_layout10.addWidget(Inspirational_and_religious_button)
        h_layout10.addSpacing(45)
        h_layout10.addWidget(Biography_and_autobiography_button)

        price = QLabel("Price")
        price.setFont(QFont("Vesper Libre", 25))
        price.setStyleSheet('''
               QLabel {
               color: rgb(132, 113, 77);
               }
               ''')

        price_cost = QLineEdit("Enter the price")
        price_cost.setFont(QFont("Vesper Libre", 20))
        price_cost.setStyleSheet('''
        QLineEdit {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(148, 132, 99);
        }
        ''')

        h_layout11 = QHBoxLayout()
        h_layout11.addSpacing(160)
        h_layout11.addWidget(price)
        h_layout11.addSpacing(25)
        h_layout11.addWidget(price_cost)
        h_layout11.addSpacing(160)

        add_button = QPushButton("Add")
        add_button.setFont(QFont("Vesper Libre", 20))
        add_button.setStyleSheet('''
        QPushButton {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(148, 132, 99);
        }
        ''')
        add_button.clicked.connect(self.getSign_inPanel)
        # in this one u have to create add book function too na, I cant figure out สมองบวม

        cancel_button = QPushButton("Cancel")
        cancel_button.setFont(QFont("Vesper Libre", 20))
        cancel_button.setStyleSheet('''
        QPushButton {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(148, 132, 99);
        }
        ''')
        cancel_button.clicked.connect(self.getSign_inPanel)

        h_layout12 = QHBoxLayout()
        h_layout12.addSpacing(20)
        h_layout12.addWidget(add_button)
        h_layout12.addSpacing(300)
        h_layout12.addWidget(cancel_button)
        h_layout12.addSpacing(20)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout1)
        v_layout.addLayout(h_layout2)
        v_layout.addLayout(h_layout3)
        v_layout.addLayout(h_layout4)
        v_layout.addLayout(h_layout5)
        v_layout.addLayout(h_layout6)
        v_layout.addLayout(h_layout7)
        v_layout.addLayout(h_layout8)
        v_layout.addLayout(h_layout9)
        v_layout.addLayout(h_layout10)
        v_layout.addLayout(h_layout11)
        v_layout.addLayout(h_layout12)

        # self.title_name.setFocusPolicy(Qt.NoFocus)
        # self.title_name.installEventFilter(self)
        # self.author_name.setFocusPolicy(Qt.NoFocus)
        # self.author_name.installEventFilter(self)
        # self.description_name.setFocusPolicy(Qt.NoFocus)
        # self.description_name.installEventFilter(self)
        # price_cost.setFocusPolicy(Qt.NoFocus)
        # price_cost.installEventFilter(self)

        self.setLayout(v_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_widget = QWidget()
        scroll_widget.setLayout(v_layout)

        scroll_area.setWidget(scroll_widget)

        # set the scroll area as the central widget
        self.setLayout(QVBoxLayout(self))
        self.layout().addWidget(scroll_area)
        self.setWindowTitle("Add Book")
        self.setFixedSize(700, 600)
        self.setStyleSheet("background-color: #F9F6EC;")
        self.show()

    def OnCLickedRomance(self):
        Romance_button = self.sender()
        print("Book " + Romance_button.book + " is " + str(Romance_button.isChecked()))

    def OnCLickedMystery(self):
        Mystery_button = self.sender()
        print("Book " + Mystery_button.book + " is " + str(Mystery_button.isChecked()))

    def OnCLickedFantasy_and_science_fiction(self):
        Fantasy_and_science_fiction_button = self.sender()
        print("Book " + Fantasy_and_science_fiction_button.book + " is " + str(
            Fantasy_and_science_fiction_button.isChecked()))

    def OnCLickedThrillers_horror(self):
        Thrillers_horror_button = self.sender()
        print("Book " + Thrillers_horror_button.book + " is " + str(Thrillers_horror_button.isChecked()))

    def OnCLickedYoung_adult(self):
        Young_adult_button = self.sender()
        print("Book " + Young_adult_button.book + " is " + str(Young_adult_button.isChecked()))

    def OnCLickedChildren_fiction(self):
        Children_fiction_button = self.sender()
        print("Book " + Children_fiction_button.book + " is " + str(Children_fiction_button.isChecked()))

    def OnCLickedInspirational_and_religious(self):
        Inspirational_and_religious_button = self.sender()
        print("Book " + Inspirational_and_religious_button.book + " is " + str(
            Inspirational_and_religious_button.isChecked()))

    def OnCLickedBiography_and_autobiography(self):
        Biography_and_autobiography_button = self.sender()
        print("Book " + Biography_and_autobiography_button.book + " is " + str(
            Biography_and_autobiography_button.isChecked()))

    def getSign_inPanel(self):  # wait for main menu done then just import main menu page na
        self.sign_in = Sign_in()
        self.close()

    # def eventFilter(self, source, event):
    #     if event.type() == QEvent.MouseButtonPress:
    #         if source is self.title_name:
    #             self.title_name.setFocus()
    #             text_title = self.title_name.text()
    #             if text_title == "Enter the title":
    #                 self.title_name.setText("")
    #     if event.type() == QEvent.MouseButtonPress:
    #         if source is self.author_name:
    #             self.author_name.setFocus()
    #             text_author = self.author_name.text()
    #             if text_author == "Enter the author":
    #                 self.author_name.setText("")
        # if event.type() == QEvent.MouseButtonPress:
        #     if source is self.description_name:
        #         self.description_name.doSetTextCursor()
        #         text_description = self.description_name.toPlainText()
        #         if text_description == "Enter the description":
        #             self.description_name.setText("")
        # return super().eventFilter(source, event)

    # def mousePressEvent(self, event):
    #     if not self.title_name.underMouse():
    #         self.title_name.clearFocus()
    #         text = self.title_name.text()
    #         if text == "":
    #             self.title_name.setText("Enter the title")
    #     if not self.author_name.underMouse():
    #         self.author_name.clearFocus()
    #         text = self.author_name.text()
    #         if text == "":
    #             self.author_name.setText("Enter the author")
    #      if not self.description_name.setPlainText("Enter the description"):
    #         self.description_name.textCursor()
    #          text = self.description_name.toPlainText()
    #          if text == "":
    #              self.description_name.setText("Enter the description")
    #     super().mousePressEvent(event)

if __name__ == "__main__":
    app = QApplication()
    ui = Add_book()
    app.exec()

# all the connected checkbox used last function isChecked() and get their result at last na I print sentence for u to identify easier
