from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit,
                               QTextEdit, QCheckBox, QScrollArea, QMainWindow)
from PySide6.QtCore import Qt, QEvent
from Sign_in import Sign_in  # change to main menu by your self na non , left only import sign in and from and import


# use in main menu instead


class Add_book(QMainWindow):
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
        self.title_name.setPlaceholderText("Enter the title")
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
        author.setFont(QFont("Vesper Libre", 25))
        author.setStyleSheet('''
        QLabel {
        color: rgb(132, 113, 77);
        }
        ''')

        author_name = QLineEdit(self)
        author_name.setPlaceholderText("Enter the author")
        author_name.setFont(QFont("Vesper Libre", 20))
        author_name.setStyleSheet('''
        QLineEdit {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(148, 132, 99);
        }
        ''')

        h_layout3 = QHBoxLayout()
        h_layout3.addSpacing(30)
        h_layout3.addWidget(author)
        h_layout3.addSpacing(15)
        h_layout3.addWidget(author_name)
        h_layout3.addSpacing(30)

        description = QLabel("Description")
        description.setFont(QFont("Vesper Libre", 25))
        description.setStyleSheet('''
        QLabel {
        color: rgb(132, 113, 77);
        }
        ''')

        h_layout4 = QHBoxLayout()
        h_layout4.addSpacing(30)
        h_layout4.addWidget(description)

        self.description_name = QTextEdit(self)
        self.description_name.setPlaceholderText("Enter the description")
        self.description_name.setFont(QFont("Vesper Libre", 20))
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
        h_layout7.addSpacing(25)
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
        h_layout8.addSpacing(25)
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
        h_layout9.addSpacing(25)
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
        h_layout10.addSpacing(25)
        h_layout10.addWidget(Biography_and_autobiography_button)

        Action_and_Adventure_button = QCheckBox("Action and Adventure")
        Action_and_Adventure_button.setChecked(False)
        Action_and_Adventure_button.book = "Action and Adventure"
        Action_and_Adventure_button.setFont(QFont("Vesper Libre", 20))
        Action_and_Adventure_button.setStyleSheet('''
                                        QCheckBox {
                                        color: rgb(132, 113, 77);
                                        }
                                        ''')

        Classics_button = QCheckBox("Classics")
        Classics_button.setChecked(False)
        Classics_button.book = "Classics"
        Classics_button.setFont(QFont("Vesper Libre", 20))
        Classics_button.setStyleSheet('''                                           
                                                QCheckBox {                                                            
                                                color: rgb(132, 113, 77);                                              
                                                }                                                                      
                                                ''')

        h_layout11 = QHBoxLayout()
        h_layout11.addSpacing(50)
        h_layout11.addWidget(Action_and_Adventure_button)
        h_layout11.addSpacing(25)
        h_layout11.addWidget(Classics_button)

        comic_button = QCheckBox("Comic book")
        comic_button.setChecked(False)
        comic_button.book = "Comic book"
        comic_button.setFont(QFont("Vesper Libre", 20))
        comic_button.setStyleSheet('''
                                                QCheckBox {
                                                color: rgb(132, 113, 77);
                                                }
                                                ''')

        historical_button = QCheckBox("Historical fiction")
        historical_button.setChecked(False)
        historical_button.book = "Historical fiction"
        historical_button.setFont(QFont("Vesper Libre", 20))
        historical_button.setStyleSheet('''                                           
                                                        QCheckBox {                                                            
                                                        color: rgb(132, 113, 77);                                              
                                                        }                                                                      
                                                        ''')

        h_layout12 = QHBoxLayout()
        h_layout12.addSpacing(50)
        h_layout12.addWidget(comic_button)
        h_layout12.addSpacing(25)
        h_layout12.addWidget(historical_button)

        literary_fiction_button = QCheckBox("Literary fiction")
        literary_fiction_button.setChecked(False)
        literary_fiction_button.book = "Literary fiction"
        literary_fiction_button.setFont(QFont("Vesper Libre", 20))
        literary_fiction_button.setStyleSheet('''
                                                        QCheckBox {
                                                        color: rgb(132, 113, 77);
                                                        }
                                                        ''')

        science_fiction_button = QCheckBox("Science fiction")
        science_fiction_button.setChecked(False)
        science_fiction_button.book = "Science fiction"
        science_fiction_button.setFont(QFont("Vesper Libre", 20))
        science_fiction_button.setStyleSheet('''                                           
                                                                QCheckBox {                                                            
                                                                color: rgb(132, 113, 77);                                              
                                                                }                                                                      
                                                                ''')

        h_layout13 = QHBoxLayout()
        h_layout13.addSpacing(50)
        h_layout13.addWidget(literary_fiction_button)
        h_layout13.addSpacing(25)
        h_layout13.addWidget(science_fiction_button)

        short_stories_button = QCheckBox("Short Stories")
        short_stories_button.setChecked(False)
        short_stories_button.book = "Short Stories"
        short_stories_button.setFont(QFont("Vesper Libre", 20))
        short_stories_button.setStyleSheet('''
                                                                QCheckBox {
                                                                color: rgb(132, 113, 77);
                                                                }
                                                                ''')

        suspense_and_thrillers_button = QCheckBox("Suspense and Thrillers")
        suspense_and_thrillers_button.setChecked(False)
        suspense_and_thrillers_button.book = "Suspense and Thrillers"
        suspense_and_thrillers_button.setFont(QFont("Vesper Libre", 20))
        suspense_and_thrillers_button.setStyleSheet('''                                           
                                                                        QCheckBox {                                                            
                                                                        color: rgb(132, 113, 77);                                              
                                                                        }                                                                      
                                                                        ''')

        h_layout14 = QHBoxLayout()
        h_layout14.addSpacing(50)
        h_layout14.addWidget(short_stories_button)
        h_layout14.addSpacing(25)
        h_layout14.addWidget(suspense_and_thrillers_button)

        womens_fiction_button = QCheckBox("Women's Fiction")
        womens_fiction_button.setChecked(False)
        womens_fiction_button.book = "Women's Fiction"
        womens_fiction_button.setFont(QFont("Vesper Libre", 20))
        womens_fiction_button.setStyleSheet('''
                                                                        QCheckBox {
                                                                        color: rgb(132, 113, 77);
                                                                        }
                                                                        ''')

        cookbooks_button = QCheckBox("Cookbooks")
        cookbooks_button.setChecked(False)
        cookbooks_button.book = "Cookbooks"
        cookbooks_button.setFont(QFont("Vesper Libre", 20))
        cookbooks_button.setStyleSheet('''                                           
                                                                                QCheckBox {                                                            
                                                                                color: rgb(132, 113, 77);                                              
                                                                                }                                                                      
                                                                                ''')

        h_layout15 = QHBoxLayout()
        h_layout15.addSpacing(50)
        h_layout15.addWidget(womens_fiction_button)
        h_layout15.addSpacing(25)
        h_layout15.addWidget(cookbooks_button)

        essay_button = QCheckBox("Essays")
        essay_button.setChecked(False)
        essay_button.book = "Essays"
        essay_button.setFont(QFont("Vesper Libre", 20))
        essay_button.setStyleSheet('''
                                                                                QCheckBox {
                                                                                color: rgb(132, 113, 77);
                                                                                }
                                                                                ''')

        memoir_button = QCheckBox("Memoir")
        memoir_button.setChecked(False)
        memoir_button.book = "Memoir"
        memoir_button.setFont(QFont("Vesper Libre", 20))
        memoir_button.setStyleSheet('''                                           
                                    QCheckBox {                                                            
                                    color: rgb(132, 113, 77);                                              
                                    }                                                                      
                                    ''')

        h_layout16 = QHBoxLayout()
        h_layout16.addSpacing(50)
        h_layout16.addWidget(essay_button)
        h_layout16.addSpacing(25)
        h_layout16.addWidget(memoir_button)

        poetry_button = QCheckBox("Poetry")
        poetry_button.setChecked(False)
        poetry_button.book = "Poetry"
        poetry_button.setFont(QFont("Vesper Libre", 20))
        poetry_button.setStyleSheet('''
                                    QCheckBox {
                                    color: rgb(132, 113, 77);
                                    }
                                    ''')

        true_crime_button = QCheckBox("True Crime")
        true_crime_button.setChecked(False)
        true_crime_button.book = "True Crime"
        true_crime_button.setFont(QFont("Vesper Libre", 20))
        true_crime_button.setStyleSheet('''                                           
                                            QCheckBox {                                                            
                                            color: rgb(132, 113, 77);                                              
                                            }                                                                      
                                            ''')

        h_layout17 = QHBoxLayout()
        h_layout17.addSpacing(50)
        h_layout17.addWidget(poetry_button)
        h_layout17.addSpacing(25)
        h_layout17.addWidget(true_crime_button)

        price = QLabel("Price/day")
        price.setFont(QFont("Vesper Libre", 25))
        price.setStyleSheet('''
               QLabel {
               color: rgb(132, 113, 77);
               }
               ''')

        price_cost = QLineEdit(self)
        price_cost.setPlaceholderText("Enter the price")
        price_cost.setFont(QFont("Vesper Libre", 20))
        price_cost.setStyleSheet('''
        QLineEdit {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(148, 132, 99);
        }
        ''')

        h_layout18 = QHBoxLayout()
        h_layout18.addSpacing(160)
        h_layout18.addWidget(price)
        h_layout18.addSpacing(25)
        h_layout18.addWidget(price_cost)
        h_layout18.addSpacing(160)

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

        h_layout19 = QHBoxLayout()
        h_layout19.addSpacing(20)
        h_layout19.addWidget(cancel_button)
        h_layout19.addSpacing(300)
        h_layout19.addWidget(add_button)
        h_layout19.addSpacing(20)

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
        v_layout.addLayout(h_layout13)
        v_layout.addLayout(h_layout14)
        v_layout.addLayout(h_layout15)
        v_layout.addLayout(h_layout16)
        v_layout.addLayout(h_layout17)
        v_layout.addLayout(h_layout18)
        v_layout.addLayout(h_layout19)
        self.setLayout(v_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_widget = QWidget()
        scroll_widget.setLayout(v_layout)

        scroll_area.setWidget(scroll_widget)

        self.setCentralWidget(scroll_area)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
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


if __name__ == "__main__":
    app = QApplication()
    ui = Add_book()
    app.exec()

# all the connected checkbox used last function isChecked() and get their result at last na I print sentence for u to identify easier
