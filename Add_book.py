import abstractBook

from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit,
                               QTextEdit, QCheckBox, QScrollArea, QMainWindow)
from PySide6.QtCore import Qt, QEvent

import essential
from Sign_in import Sign_in  # change to main menu by your self na non , left only import sign in and from and import
import BookCategory

# use in main menu instead


class Add_book(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Romance = None
        self.sign_in = None
        self.category = []
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

        self.author_name = QLineEdit(self)
        self.author_name.setPlaceholderText("Enter the author")
        self.author_name.setFont(QFont("Vesper Libre", 20))
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

        self.Romance_button = QCheckBox("Romance")
        self.Romance_button.setChecked(False)
        self.Romance_button.book = "Romance"
        self.Romance_button.setFont(QFont("Vesper Libre", 20))
        self.Romance_button.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        self.Mystery_button = QCheckBox("Mystery")
        self.Mystery_button.setChecked(False)
        self.Mystery_button.book = "Mystery"
        self.Mystery_button.setFont(QFont("Vesper Libre", 20))
        self.Mystery_button.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        h_layout7 = QHBoxLayout()
        h_layout7.addSpacing(50)
        h_layout7.addWidget(self.Romance_button)
        h_layout7.addSpacing(25)
        h_layout7.addWidget(self.Mystery_button)

        self.Fantasy_and_science_fiction_button = QCheckBox("Fantasy and science fiction")
        self.Fantasy_and_science_fiction_button.setChecked(False)
        self.Fantasy_and_science_fiction_button.book = "Fantasy and science fiction"
        self.Fantasy_and_science_fiction_button.setFont(QFont("Vesper Libre", 20))
        self.Fantasy_and_science_fiction_button.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        self.Thrillers_horror_button = QCheckBox("Thrillers and horror")
        self.Thrillers_horror_button.setChecked(False)
        self.Thrillers_horror_button.book = "Thrillers and horror"
        self.Thrillers_horror_button.setFont(QFont("Vesper Libre", 20))
        self.Thrillers_horror_button.setStyleSheet('''
                QCheckBox {
                color: rgb(132, 113, 77);
                }
                ''')

        h_layout8 = QHBoxLayout()
        h_layout8.addSpacing(50)
        h_layout8.addWidget(self.Fantasy_and_science_fiction_button)
        h_layout8.addSpacing(25)
        h_layout8.addWidget(self.Thrillers_horror_button)

        self.Young_adult_button = QCheckBox("Young adult")
        self.Young_adult_button.setChecked(False)
        self.Young_adult_button.book = "Young adult"
        self.Young_adult_button.setFont(QFont("Vesper Libre", 20))
        self.Young_adult_button.setStyleSheet('''
                QCheckBox {
                color: rgb(132, 113, 77);
                }
                ''')

        self.Children_fiction_button = QCheckBox("Children’s fiction")
        self.Children_fiction_button.setChecked(False)
        self.Children_fiction_button.book = "Children’s fiction"
        self.Children_fiction_button.setFont(QFont("Vesper Libre", 20))
        self.Children_fiction_button.setStyleSheet('''
                        QCheckBox {
                        color: rgb(132, 113, 77);
                        }
                        ''')

        h_layout9 = QHBoxLayout()
        h_layout9.addSpacing(50)
        h_layout9.addWidget(self.Young_adult_button)
        h_layout9.addSpacing(25)
        h_layout9.addWidget(self.Children_fiction_button)

        self.Inspirational_and_religious_button = QCheckBox("Inspirational and religious")
        self.Inspirational_and_religious_button.setChecked(False)
        self.Inspirational_and_religious_button.book = "Children’s fiction"
        self.Inspirational_and_religious_button.setFont(QFont("Vesper Libre", 20))
        self.Inspirational_and_religious_button.setStyleSheet('''
                                QCheckBox {
                                color: rgb(132, 113, 77);
                                }
                                ''')

        self.Biography_and_autobiography_button = QCheckBox("Biography and autobiography")
        self.Biography_and_autobiography_button.setChecked(False)
        self.Biography_and_autobiography_button.book = "Biography and autobiography"
        self.Biography_and_autobiography_button.setFont(QFont("Vesper Libre", 20))
        self.Biography_and_autobiography_button.setStyleSheet('''                                           
                                        QCheckBox {                                                            
                                        color: rgb(132, 113, 77);                                              
                                        }                                                                      
                                        ''')

        h_layout10 = QHBoxLayout()
        h_layout10.addSpacing(50)
        h_layout10.addWidget(self.Inspirational_and_religious_button)
        h_layout10.addSpacing(25)
        h_layout10.addWidget(self.Biography_and_autobiography_button)

        self.Action_and_Adventure_button = QCheckBox("Action and Adventure")
        self.Action_and_Adventure_button.setChecked(False)
        self.Action_and_Adventure_button.book = "Action and Adventure"
        self.Action_and_Adventure_button.setFont(QFont("Vesper Libre", 20))
        self.Action_and_Adventure_button.setStyleSheet('''
                                        QCheckBox {
                                        color: rgb(132, 113, 77);
                                        }
                                        ''')

        self.Classics_button = QCheckBox("Classics")
        self.Classics_button.setChecked(False)
        self.Classics_button.book = "Classics"
        self.Classics_button.setFont(QFont("Vesper Libre", 20))
        self.Classics_button.setStyleSheet('''                                           
                                                QCheckBox {                                                            
                                                color: rgb(132, 113, 77);                                              
                                                }                                                                      
                                                ''')

        h_layout11 = QHBoxLayout()
        h_layout11.addSpacing(50)
        h_layout11.addWidget(self.Action_and_Adventure_button)
        h_layout11.addSpacing(25)
        h_layout11.addWidget(self.Classics_button)

        self.comic_button = QCheckBox("Comic book")
        self.comic_button.setChecked(False)
        self.comic_button.book = "Comic book"
        self.comic_button.setFont(QFont("Vesper Libre", 20))
        self.comic_button.setStyleSheet('''
                                                QCheckBox {
                                                color: rgb(132, 113, 77);
                                                }
                                                ''')

        self.historical_button = QCheckBox("Historical fiction")
        self.historical_button.setChecked(False)
        self.historical_button.book = "Historical fiction"
        self.historical_button.setFont(QFont("Vesper Libre", 20))
        self.historical_button.setStyleSheet('''                                           
                                                        QCheckBox {                                                            
                                                        color: rgb(132, 113, 77);                                              
                                                        }                                                                      
                                                        ''')

        h_layout12 = QHBoxLayout()
        h_layout12.addSpacing(50)
        h_layout12.addWidget(self.comic_button)
        h_layout12.addSpacing(25)
        h_layout12.addWidget(self.historical_button)

        self.literary_fiction_button = QCheckBox("Literary fiction")
        self.literary_fiction_button.setChecked(False)
        self.literary_fiction_button.book = "Literary fiction"
        self.literary_fiction_button.setFont(QFont("Vesper Libre", 20))
        self.literary_fiction_button.setStyleSheet('''
                                                        QCheckBox {
                                                        color: rgb(132, 113, 77);
                                                        }
                                                        ''')

        self.science_fiction_button = QCheckBox("Science fiction")
        self.science_fiction_button.setChecked(False)
        self.science_fiction_button.book = "Science fiction"
        self.science_fiction_button.setFont(QFont("Vesper Libre", 20))
        self.science_fiction_button.setStyleSheet('''                                           
                                                                QCheckBox {                                                            
                                                                color: rgb(132, 113, 77);                                              
                                                                }                                                                      
                                                                ''')

        h_layout13 = QHBoxLayout()
        h_layout13.addSpacing(50)
        h_layout13.addWidget(self.literary_fiction_button)
        h_layout13.addSpacing(25)
        h_layout13.addWidget(self.science_fiction_button)

        self.short_stories_button = QCheckBox("Short Stories")
        self.short_stories_button.setChecked(False)
        self.short_stories_button.book = "Short Stories"
        self.short_stories_button.setFont(QFont("Vesper Libre", 20))
        self.short_stories_button.setStyleSheet('''
                                                                QCheckBox {
                                                                color: rgb(132, 113, 77);
                                                                }
                                                                ''')

        self.suspense_and_thrillers_button = QCheckBox("Suspense and Thrillers")
        self.suspense_and_thrillers_button.setChecked(False)
        self.suspense_and_thrillers_button.book = "Suspense and Thrillers"
        self.suspense_and_thrillers_button.setFont(QFont("Vesper Libre", 20))
        self.suspense_and_thrillers_button.setStyleSheet('''                                           
                                                                        QCheckBox {                                                            
                                                                        color: rgb(132, 113, 77);                                              
                                                                        }                                                                      
                                                                        ''')

        h_layout14 = QHBoxLayout()
        h_layout14.addSpacing(50)
        h_layout14.addWidget(self.short_stories_button)
        h_layout14.addSpacing(25)
        h_layout14.addWidget(self.suspense_and_thrillers_button)

        self.womens_fiction_button = QCheckBox("Women's Fiction")
        self.womens_fiction_button.setChecked(False)
        self.womens_fiction_button.book = "Women's Fiction"
        self.womens_fiction_button.setFont(QFont("Vesper Libre", 20))
        self.womens_fiction_button.setStyleSheet('''
                                                                        QCheckBox {
                                                                        color: rgb(132, 113, 77);
                                                                        }
                                                                        ''')

        self.cookbooks_button = QCheckBox("Cookbooks")
        self.cookbooks_button.setChecked(False)
        self.cookbooks_button.book = "Cookbooks"
        self.cookbooks_button.setFont(QFont("Vesper Libre", 20))
        self.cookbooks_button.setStyleSheet('''                                           
                                                                                QCheckBox {                                                            
                                                                                color: rgb(132, 113, 77);                                              
                                                                                }                                                                      
                                                                                ''')

        h_layout15 = QHBoxLayout()
        h_layout15.addSpacing(50)
        h_layout15.addWidget(self.womens_fiction_button)
        h_layout15.addSpacing(25)
        h_layout15.addWidget(self.cookbooks_button)

        self.essay_button = QCheckBox("Essays")
        self.essay_button.setChecked(False)
        self.essay_button.book = "Essays"
        self.essay_button.setFont(QFont("Vesper Libre", 20))
        self.essay_button.setStyleSheet('''
                                                                                QCheckBox {
                                                                                color: rgb(132, 113, 77);
                                                                                }
                                                                                ''')

        self.memoir_button = QCheckBox("Memoir")
        self.memoir_button.setChecked(False)
        self.memoir_button.book = "Memoir"
        self.memoir_button.setFont(QFont("Vesper Libre", 20))
        self.memoir_button.setStyleSheet('''                                           
                                    QCheckBox {                                                            
                                    color: rgb(132, 113, 77);                                              
                                    }                                                                      
                                    ''')

        h_layout16 = QHBoxLayout()
        h_layout16.addSpacing(50)
        h_layout16.addWidget(self.essay_button)
        h_layout16.addSpacing(25)
        h_layout16.addWidget(self.memoir_button)

        self.poetry_button = QCheckBox("Poetry")
        self.poetry_button.setChecked(False)
        self.poetry_button.book = "Poetry"
        self.poetry_button.setFont(QFont("Vesper Libre", 20))
        self.poetry_button.setStyleSheet('''
                                    QCheckBox {
                                    color: rgb(132, 113, 77);
                                    }
                                    ''')

        self.true_crime_button = QCheckBox("True Crime")
        self.true_crime_button.setChecked(False)
        self.true_crime_button.book = "True Crime"
        self.true_crime_button.setFont(QFont("Vesper Libre", 20))
        self.true_crime_button.setStyleSheet('''                                           
                                            QCheckBox {                                                            
                                            color: rgb(132, 113, 77);                                              
                                            }                                                                      
                                            ''')

        h_layout17 = QHBoxLayout()
        h_layout17.addSpacing(50)
        h_layout17.addWidget(self.poetry_button)
        h_layout17.addSpacing(25)
        h_layout17.addWidget(self.true_crime_button)

        price = QLabel("Price/day")
        price.setFont(QFont("Vesper Libre", 25))
        price.setStyleSheet('''
               QLabel {
               color: rgb(132, 113, 77);
               }
               ''')

        self.price_cost = QLineEdit(self)
        self.price_cost.setPlaceholderText("Enter the price")
        self.price_cost.setFont(QFont("Vesper Libre", 20))
        self.price_cost.setStyleSheet('''
        QLineEdit {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(148, 132, 99);
        }
        ''')

        h_layout18 = QHBoxLayout()
        h_layout18.addSpacing(160)
        h_layout18.addWidget(price)
        h_layout18.addSpacing(25)
        h_layout18.addWidget(self.price_cost)
        h_layout18.addSpacing(160)

        self.add_button = QPushButton("Add")
        self.add_button.setFont(QFont("Vesper Libre", 20))
        self.add_button.setStyleSheet('''
        QPushButton {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(148, 132, 99);
        }
        ''')
        self.add_button.clicked.connect(self.save_and_go_main)
        # in this one u have to create add book function too na, I cant figure out สมองบวม

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setFont(QFont("Vesper Libre", 20))
        self.cancel_button.setStyleSheet('''
        QPushButton {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(148, 132, 99);   
        }
        ''')
        self.cancel_button.clicked.connect(self.getMainPanel)

        h_layout19 = QHBoxLayout()
        h_layout19.addSpacing(20)
        h_layout19.addWidget(self.cancel_button)
        h_layout19.addSpacing(300)
        h_layout19.addWidget(self.add_button)
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

    def getMainPanel(self):  # wait for main menu done then just import main menu page na
        self.sign_in = Sign_in()
        self.close()

    def check_category(self):
        if self.Romance_button.isChecked():
            self.category.append(BookCategory.BookCategory(1))
        if self.Mystery_button.isChecked():
            self.category.append(BookCategory.BookCategory(2))
        if self.Fantasy_and_science_fiction_button.isChecked():
            self.category.append(BookCategory.BookCategory(3))
        if self.Thrillers_horror_button.isChecked():
            self.category.append(BookCategory.BookCategory(4))
        if self.Young_adult_button.isChecked():
            self.category.append(BookCategory.BookCategory(5))
        if self.Children_fiction_button.isChecked():
            self.category.append(BookCategory.BookCategory(6))
        if self.Inspirational_and_religious_button.isChecked():
            self.category.append(BookCategory.BookCategory(7))
        if self.Biography_and_autobiography_button.isChecked():
            self.category.append(BookCategory.BookCategory(8))
        if self.Action_and_Adventure_button.isChecked():
            self.category.append(BookCategory.BookCategory(9))
        if self.Classics_button.isChecked():
            self.category.append(BookCategory.BookCategory(10))
        if self.comic_button.isChecked():
            self.category.append(BookCategory.BookCategory(11))
        if self.historical_button.isChecked():
            self.category.append(BookCategory.BookCategory(12))
        if self.literary_fiction_button.isChecked():
            self.category.append(BookCategory.BookCategory(13))
        if self.science_fiction_button.isChecked():
            self.category.append(BookCategory.BookCategory(14))
        if self.short_stories_button.isChecked():
            self.category.append(BookCategory.BookCategory(15))
        if self.suspense_and_thrillers_button.isChecked():
            self.category.append(BookCategory.BookCategory(16))
        if self.womens_fiction_button.isChecked():
            self.category.append(BookCategory.BookCategory(17))
        if self.cookbooks_button.isChecked():
            self.category.append(BookCategory.BookCategory(18))
        if self.essay_button.isChecked():
            self.category.append(BookCategory.BookCategory(19))
        if self.memoir_button.isChecked():
            self.category.append(BookCategory.BookCategory(20))
        if self.poetry_button.isChecked():
            self.category.append(BookCategory.BookCategory(21))
        if self.true_crime_button.isChecked():
            self.category.append(BookCategory.BookCategory(22))

    def get_cateogry(self):
        return self.category

    def save_and_go_main(self):
        self.check_category()
        self.sign_in = Sign_in()
        self.close()


if __name__ == "__main__":
    app = QApplication()
    ui = Add_book()
    app.exec()

# all the connected checkbox used last function isChecked() and get their result at last na I print sentence for u to identify easier
