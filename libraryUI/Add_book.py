import os

from PySide6.QtGui import (QFont, QPixmap, QDragEnterEvent)
from PySide6.QtWidgets import *
from PySide6.QtCore import *

import libraryUI.Sign_in
from libraryUI.Sign_in import \
    Sign_in  # change to main menu by your self na non , left only import sign in and from and import
from librarySystem import *


# use in main menu instead


class Add_book(QMainWindow):

    def __init__(self):
        super().__init__()
        self.sign_in = None
        self.category = []
        self.book_type = []
        self.book_image = QLabel()
        self.placeholder_image = QPixmap(
            "placeholder.png")  # replace "placeholder.png" with the path to your placeholder image
        self.book_image.setPixmap(self.placeholder_image)
        self.book_image.setScaledContents(True)
        self.book_image.setMinimumSize(250, 250)
        self.book_image.setAlignment(Qt.AlignCenter)

        self.book_image.setStyleSheet("border: 2px dashed gray; color: gray;")
        self.book_image.setText("Please drag and drop a book image here")

        layout = QHBoxLayout()
        layout.addWidget(self.book_image)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setAcceptDrops(True)
        blank = QLabel("")

        h_layout1 = QHBoxLayout()
        h_layout1.addWidget(blank)
        h_layout1.addWidget(self.book_image)
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

        self.Comic_button = QCheckBox("Comic book")
        self.Comic_button.setChecked(False)
        self.Comic_button.book = "Comic book"
        self.Comic_button.setFont(QFont("Vesper Libre", 20))
        self.Comic_button.setStyleSheet('''
                                                QCheckBox {
                                                color: rgb(132, 113, 77);
                                                }
                                                ''')

        self.Historical_button = QCheckBox("Historical fiction")
        self.Historical_button.setChecked(False)
        self.Historical_button.book = "Historical fiction"
        self.Historical_button.setFont(QFont("Vesper Libre", 20))
        self.Historical_button.setStyleSheet('''                                           
                                                        QCheckBox {                                                            
                                                        color: rgb(132, 113, 77);                                              
                                                        }                                                                      
                                                        ''')

        h_layout12 = QHBoxLayout()
        h_layout12.addSpacing(50)
        h_layout12.addWidget(self.Comic_button)
        h_layout12.addSpacing(25)
        h_layout12.addWidget(self.Historical_button)
        self.Literary_fiction_button = QCheckBox("Literary fiction")
        self.Literary_fiction_button.setChecked(False)
        self.Literary_fiction_button.book = "Literary fiction"
        self.Literary_fiction_button.setFont(QFont("Vesper Libre", 20))
        self.Literary_fiction_button.setStyleSheet('''
                                                        QCheckBox {
                                                        color: rgb(132, 113, 77);
                                                        }
                                                        ''')

        self.Science_fiction_button = QCheckBox("Science fiction")
        self.Science_fiction_button.setChecked(False)
        self.Science_fiction_button.book = "Science fiction"
        self.Science_fiction_button.setFont(QFont("Vesper Libre", 20))
        self.Science_fiction_button.setStyleSheet('''                                           
                                                                QCheckBox {                                                            
                                                                color: rgb(132, 113, 77);                                              
                                                                }                                                                      
                                                                ''')

        h_layout13 = QHBoxLayout()
        h_layout13.addSpacing(50)
        h_layout13.addWidget(self.Literary_fiction_button)
        h_layout13.addSpacing(25)
        h_layout13.addWidget(self.Science_fiction_button)

        self.Short_stories_button = QCheckBox("Short Stories")
        self.Short_stories_button.setChecked(False)
        self.Short_stories_button.book = "Short Stories"
        self.Short_stories_button.setFont(QFont("Vesper Libre", 20))
        self.Short_stories_button.setStyleSheet('''
                                                                QCheckBox {
                                                                color: rgb(132, 113, 77);
                                                                }
                                                                ''')

        self.Suspense_and_thrillers_button = QCheckBox("Suspense and Thrillers")
        self.Suspense_and_thrillers_button.setChecked(False)
        self.Suspense_and_thrillers_button.book = "Suspense and Thrillers"
        self.Suspense_and_thrillers_button.setFont(QFont("Vesper Libre", 20))
        self.Suspense_and_thrillers_button.setStyleSheet('''                                           
                                                                        QCheckBox {                                                            
                                                                        color: rgb(132, 113, 77);                                              
                                                                        }                                                                      
                                                                        ''')

        h_layout14 = QHBoxLayout()
        h_layout14.addSpacing(50)
        h_layout14.addWidget(self.Short_stories_button)
        h_layout14.addSpacing(25)
        h_layout14.addWidget(self.Suspense_and_thrillers_button)
        self.Womens_fiction_button = QCheckBox("Women's Fiction")
        self.Womens_fiction_button.setChecked(False)
        self.Womens_fiction_button.book = "Women's Fiction"
        self.Womens_fiction_button.setFont(QFont("Vesper Libre", 20))
        self.Womens_fiction_button.setStyleSheet('''
                                                                        QCheckBox {
                                                                        color: rgb(132, 113, 77);
                                                                        }
                                                                        ''')

        self.Cookbooks_button = QCheckBox("Cookbooks")
        self.Cookbooks_button.setChecked(False)
        self.Cookbooks_button.book = "Cookbooks"
        self.Cookbooks_button.setFont(QFont("Vesper Libre", 20))
        self.Cookbooks_button.setStyleSheet('''                                           
                                                                                QCheckBox {                                                            
                                                                                color: rgb(132, 113, 77);                                              
                                                                                }                                                                      
                                                                                ''')

        h_layout15 = QHBoxLayout()
        h_layout15.addSpacing(50)
        h_layout15.addWidget(self.Womens_fiction_button)
        h_layout15.addSpacing(25)
        h_layout15.addWidget(self.Cookbooks_button)

        self.Essay_button = QCheckBox("Essays")
        self.Essay_button.setChecked(False)
        self.Essay_button.book = "Essays"
        self.Essay_button.setFont(QFont("Vesper Libre", 20))
        self.Essay_button.setStyleSheet('''
                                                                                QCheckBox {
                                                                                color: rgb(132, 113, 77);
                                                                                }
                                                                                ''')

        self.Memoir_button = QCheckBox("Memoir")
        self.Memoir_button.setChecked(False)
        self.Memoir_button.book = "Memoir"
        self.Memoir_button.setFont(QFont("Vesper Libre", 20))
        self.Memoir_button.setStyleSheet('''                                           
                                    QCheckBox {                                                            
                                    color: rgb(132, 113, 77);                                              
                                    }                                                                      
                                    ''')

        h_layout16 = QHBoxLayout()
        h_layout16.addSpacing(50)
        h_layout16.addWidget(self.Essay_button)
        h_layout16.addSpacing(25)
        h_layout16.addWidget(self.Memoir_button)

        self.Poetry_button = QCheckBox("Poetry")
        self.Poetry_button.setChecked(False)
        self.Poetry_button.book = "Poetry"
        self.Poetry_button.setFont(QFont("Vesper Libre", 20))
        self.Poetry_button.setStyleSheet('''
                                    QCheckBox {
                                    color: rgb(132, 113, 77);
                                    }
                                    ''')

        self.True_crime_button = QCheckBox("True Crime")
        self.True_crime_button.setChecked(False)
        self.True_crime_button.book = "True Crime"
        self.True_crime_button.setFont(QFont("Vesper Libre", 20))
        self.True_crime_button.setStyleSheet('''                                           
                                            QCheckBox {                                                            
                                            color: rgb(132, 113, 77);                                              
                                            }                                                                      
                                            ''')

        h_layout17 = QHBoxLayout()
        h_layout17.addSpacing(50)
        h_layout17.addWidget(self.Poetry_button)
        h_layout17.addSpacing(25)
        h_layout17.addWidget(self.True_crime_button)

        self.book_button = QRadioButton("Book")
        self.book_button.setChecked(False)  # Set one of the radio buttons as checked by default
        self.book_button.book = "Book"
        self.book_button.setFont(QFont("Vesper Libre", 20))
        self.book_button.setStyleSheet('''
                                        QRadioButton {
                                        color: rgb(132, 113, 77);
                                        }
                                        ''')

        self.e_book_button = QRadioButton("E-Book")
        self.e_book_button.setChecked(False)
        self.e_book_button.book = "E-Book"
        self.e_book_button.setFont(QFont("Vesper Libre", 20))
        self.e_book_button.setStyleSheet('''
                                            QRadioButton {
                                            color: rgb(132, 113, 77);
                                            }
                                            ''')

        h_layout18 = QHBoxLayout()
        h_layout18.addSpacing(50)
        h_layout18.addWidget(self.book_button)
        h_layout18.addSpacing(25)
        h_layout18.addWidget(self.e_book_button)

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

        h_layout19 = QHBoxLayout()
        h_layout19.addSpacing(160)
        h_layout19.addWidget(price)
        h_layout19.addSpacing(25)
        h_layout19.addWidget(self.price_cost)
        h_layout19.addSpacing(160)

        self.add_button = QPushButton("Add")
        self.add_button.setFont(QFont("Vesper Libre", 20))
        self.add_button.setStyleSheet('''
        QPushButton {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(148, 132, 99);
        }
        ''')
        self.add_button.clicked.connect(self.save_image)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setFont(QFont("Vesper Libre", 20))
        self.cancel_button.setStyleSheet('''
        QPushButton {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(148, 132, 99);   
        }
        ''')
        self.cancel_button.clicked.connect(self.cancel__goback)

        h_layout20 = QHBoxLayout()
        h_layout20.addSpacing(20)
        h_layout20.addWidget(self.cancel_button)
        h_layout20.addSpacing(300)
        h_layout20.addWidget(self.add_button)
        h_layout20.addSpacing(20)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout1)
        v_layout.addSpacing(20)
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
        v_layout.addLayout(h_layout20)
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

    def cancel__goback(self):  # wait for main menu done then just import main menu page na
        self.sign_in = Sign_in()
        self.close()

    def check_category(self):
        genre = [self.Romance_button, self.Mystery_button, self.Fantasy_and_science_fiction_button,
                 self.Thrillers_horror_button, self.Young_adult_button, self.Children_fiction_button,
                 self.Inspirational_and_religious_button, self.Biography_and_autobiography_button,
                 self.Action_and_Adventure_button, self.Classics_button, self.Comic_button,
                 self.Historical_button, self.Literary_fiction_button, self.Science_fiction_button,
                 self.Short_stories_button, self.Suspense_and_thrillers_button, self.Womens_fiction_button,
                 self.Cookbooks_button, self.Essay_button, self.Memoir_button, self.Poetry_button,
                 self.True_crime_button]
        for i in range(len(genre)):
            if genre[i].isChecked():
                self.category.append(genre[i].text())
            else:
                self.category.append("None")

    def check_booktype(self):
        if self.book_button.isChecked():
            librarySystem.addNewBook(self.pixmap, self.title_name.text(), self.author_name.text(),
                                     self.description_name.toPlainText(), self.get_category(),
                                     self.price_cost.text())
        if self.e_book_button.isChecked():
            librarySystem.addNewEbook(self.pixmap, self.title_name.text(), self.author_name.text(),
                                      self.description_name.toPlainText(), self.get_category(),
                                      self.price_cost.text())
        return self.book_type

    def get_category(self):
        print(self.category)
        return self.category

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls() and event.mimeData().urls()[0].toString().endswith('.png'):
            event.acceptProposedAction()

    def dropEvent(self, event):
        url = event.mimeData().urls()[0]
        file_path = url.toLocalFile()
        if file_path.endswith('.png'):
            self.pixmap = QPixmap(file_path)
            self.book_image.setPixmap(self.pixmap)
            self.book_image.setScaledContents(True)
            self.book_image.setStyleSheet("border: #F9F6EC")

    def save_image(self):
        # Save the dropped image to the project's images folder and create the folder if it doesn't exist
        title_name = self.title_name.text()
        self.pixmap = self.book_image.pixmap()
        if not librarySystem.save_images(self.pixmap, title_name):
            dialog = QDialog()
            dialog.setWindowTitle("Error")
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog.resize(300, 100)
            label = QLabel("Please check whether you enter a title for the book and image or not")
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
            v_layout = QVBoxLayout()
            v_layout.addWidget(label)
            v_layout.addWidget(button)
            dialog.setLayout(v_layout)
            dialog.exec()
        else:
            self.save_and_go_main()

    def save_and_go_main(self):
        if self.book_button.isChecked():
            title_name = self.title_name.text()
            self.pixmap = self.book_image.pixmap()
            if librarySystem.save_images(self.pixmap, title_name):
                self.check_category()
                self.close()  # main menu

        if self.e_book_button.isChecked():
            dialog = QDialog()
            dialog.setWindowTitle("URL link:")
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog.resize(300, 100)
            label = QLabel("URL link:")
            label.setFont(QFont("Vesper Libre", 15))
            label.setStyleSheet('''QLabel {
                                     color: rgb(132, 113, 77);
                                     }
                                     ''')
            self.Url = QLineEdit()
            self.Url.setFont(QFont("Vesper Libre", 15))
            self.Url.setStyleSheet('''QLineEdit {
                                     border: 3px solid rgb(132, 113, 77);
                                     color: rgb(249, 246, 236);
                                     background-color: rgb(182, 170, 145);
                                     }
                                     ''')
            h_layout = QHBoxLayout()
            h_layout.addWidget(label)
            h_layout.addWidget(self.Url)
            ok_button = QPushButton("OK")
            ok_button.setFont(QFont("Vesper Libre", 15))
            ok_button.setStyleSheet('''
                                     QPushButton {
                                     border: 3px solid rgb(132, 113, 77);
                                     color: rgb(249, 246, 236);
                                      background-color: rgb(182, 170, 145);
                                     }
                                     ''')
            ok_button.clicked.connect(dialog.close)  # Connect the clicked signal to the process_url function
            ok_button.clicked.connect(self.process_url)  # Connect the clicked signal to the process_url function

            cancel_button = QPushButton("Cancel")
            cancel_button.setFont(QFont("Vesper Libre", 15))
            cancel_button.setStyleSheet('''
                                            QPushButton {
                                            border: 3px solid rgb(132, 113, 77);
                                            color: rgb(249, 246, 236);
                                            background-color: rgb(182, 170, 145);
                                            }
                                            ''')
            cancel_button.clicked.connect(dialog.close)
            h_layout2 = QHBoxLayout()
            h_layout2.addWidget(cancel_button)
            h_layout2.addWidget(ok_button)
            v_layout = QVBoxLayout()
            v_layout.addLayout(h_layout)
            v_layout.addLayout(h_layout2)
            dialog.setLayout(v_layout)
            dialog.exec()

    def process_url(self):
        if self.Url.text():
            dialog = QDialog()
            # Process the URL entered by the user
            dialog.setWindowTitle("Success")
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog.resize(300, 100)
            label = QLabel(f"Your Url has been saved with {self.Url.text()}")
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
            button.clicked.connect(self.addBooK.emit)
            v_layout = QVBoxLayout()
            v_layout.addWidget(label)
            v_layout.addWidget(button)
            dialog.setLayout(v_layout)
            dialog.exec()
            if self.e_book_button.isChecked():
                title_name = self.title_name.text()
                self.pixmap = self.book_image.pixmap()
                if librarySystem.save_images(self.pixmap, title_name):
                    self.check_category()
                    self.close()  # menu
        else:
            dialog = QDialog()
            dialog.setWindowTitle("Error")
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog.resize(300, 100)
            label = QLabel("Please enter a URL link")
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
            v_layout = QVBoxLayout()
            v_layout.addWidget(label)
            v_layout.addWidget(button)
            dialog.setLayout(v_layout)
            dialog.exec()


if __name__ == "__main__":
    app = QApplication()
    ui = Add_book()
    app.exec()
