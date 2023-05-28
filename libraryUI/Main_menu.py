from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtCore import Qt


class Main_menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.checkList_book = None
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.tab_widget = QTabWidget()
        self.tab_widget.setFont(QFont("Vesper Libre", 20))
        self.tab_widget.setStyleSheet('''
            QTabWidget::pane {
                border: 3px solid rgb(132, 113, 77);
                background-color: rgb(182, 170, 145);
            }
            QTabBar::tab {
                color: rgb(249, 246, 236);
                background-color: rgb(132, 113, 77);
                height: 40px;
                width: 150px;
                margin-right: 0px;
            }
            QTabBar::tab:selected {
                background-color: rgb(182, 170, 145);
            }
            QTabWidget::tab-bar {
                alignment: left;
                left: 0;
            }
        ''')

        book_tab = QWidget()
        e_book_tab = QWidget()
        history_tab = QWidget()

        self.tab_widget.addTab(book_tab, "Book")
        self.tab_widget.addTab(e_book_tab, "E-book")
        self.tab_widget.addTab(history_tab, "History")

        self.search_place_book = QLineEdit()
        self.search_place_book.setPlaceholderText("Search book name")
        self.search_place_book.setFont(QFont("Vesper Libre", 20))
        self.search_place_book.setStyleSheet('''
            QLineEdit {
                border: 3px solid rgb(132, 113, 77);
                color: rgb(249, 246, 236);
                background-color: rgb(182, 170, 145);
            }
        ''')

        self.filter_button_book = QToolButton()
        self.filter_button_book.setText("Filter")
        self.filter_button_book.setFont(QFont("Vesper Libre", 20))
        self.filter_button_book.setStyleSheet('''
            QToolButton {
                border: 3px solid rgb(132, 113, 77);
                color: rgb(249, 246, 236);
                background-color: rgb(182, 170, 145);
            }
            QToolButton::menu-indicator {
                image: none;
            }
        ''')
        self.filter_button_book.setPopupMode(QToolButton.InstantPopup)

        self.filter_menu_book = QMenu(self.filter_button_book)

        self.romanceCheck_book = QCheckBox("Romance")
        self.romanceCheck_book.setChecked(False)
        self.romanceCheck_book.setFont(QFont("Vesper Libre", 16))
        self.romanceCheck_book.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
            }
        ''')

        self.mysteryCheck_book = QCheckBox("Mystery")
        self.mysteryCheck_book.setChecked(False)
        self.mysteryCheck_book.setFont(QFont("Vesper Libre", 16))
        self.mysteryCheck_book.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
                }
            ''')

        self.fantasyAndScienceFictionCheck_book = QCheckBox("Fantasy and science fiction")
        self.fantasyAndScienceFictionCheck_book.setChecked(False)
        self.fantasyAndScienceFictionCheck_book.setFont(QFont("Vesper Libre", 16))
        self.fantasyAndScienceFictionCheck_book.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
                }
            ''')

        self.thrillersHorrorCheck_book = QCheckBox("Thrillers and horror")
        self.thrillersHorrorCheck_book.setChecked(False)
        self.thrillersHorrorCheck_book.setFont(QFont("Vesper Libre", 16))
        self.thrillersHorrorCheck_book.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
                }
            ''')

        self.youngAdultCheck_book = QCheckBox("Young adult")
        self.youngAdultCheck_book.setChecked(False)
        self.youngAdultCheck_book.setFont(QFont("Vesper Libre", 16))
        self.youngAdultCheck_book.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
                }
            ''')

        self.childrenFictionCheck_book = QCheckBox("Children's fiction")
        self.childrenFictionCheck_book.setChecked(False)
        self.childrenFictionCheck_book.setFont(QFont("Vesper Libre", 16))
        self.childrenFictionCheck_book.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
                }
            ''')

        self.inspirationalReligiousCheck_book = QCheckBox("Inspiraltional and religious")
        self.inspirationalReligiousCheck_book.setChecked(False)
        self.inspirationalReligiousCheck_book.setFont(QFont("Vesper Libre", 16))
        self.inspirationalReligiousCheck_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')

        self.biographyAndAutobiographyCheck_book = QCheckBox("Biography and autobiography")
        self.biographyAndAutobiographyCheck_book.setChecked(False)
        self.biographyAndAutobiographyCheck_book.setFont(QFont("Vesper Libre", 16))
        self.biographyAndAutobiographyCheck_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')
        self.actionAndAdventureCheck_book = QCheckBox("Action and Adventure")
        self.actionAndAdventureCheck_book.setChecked(False)
        self.actionAndAdventureCheck_book.setFont(QFont("Vesper Libre", 16))
        self.actionAndAdventureCheck_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')

        self.classicCheck_book = QCheckBox("Classics")
        self.classicCheck_book.setChecked(False)
        self.classicCheck_book.setFont(QFont("Vesper Libre", 16))
        self.classicCheck_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')

        self.comicBookCheck_book = QCheckBox("Comic book")
        self.comicBookCheck_book.setChecked(False)
        self.comicBookCheck_book.setFont(QFont("Vesper Libre", 16))
        self.comicBookCheck_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')

        self.historicalFictionCheck_book = QCheckBox("Historical fiction")
        self.historicalFictionCheck_book.setChecked(False)
        self.historicalFictionCheck_book.setFont(QFont("Vesper Libre", 16))
        self.historicalFictionCheck_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')

        self.literaryCheck_book = QCheckBox("Literary fiction")
        self.literaryCheck_book.setChecked(False)
        self.literaryCheck_book.setFont(QFont("Vesper Libre", 16))
        self.literaryCheck_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')

        self.scienceFiction_book = QCheckBox("Science fiction")
        self.scienceFiction_book.setChecked(False)
        self.scienceFiction_book.setFont(QFont("Vesper Libre", 16))
        self.scienceFiction_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')

        self.shortStoryCheck_book = QCheckBox("Short Stories")
        self.shortStoryCheck_book.setChecked(False)
        self.shortStoryCheck_book.setFont(QFont("Vesper Libre", 16))
        self.shortStoryCheck_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')

        self.suspenseAndThrillerCheck_book = QCheckBox("Suspense and Thrillers")
        self.suspenseAndThrillerCheck_book.setChecked(False)
        self.suspenseAndThrillerCheck_book.setFont(QFont("Vesper Libre", 16))
        self.suspenseAndThrillerCheck_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')

        self.womensFictionCheck_book = QCheckBox("Women's Fiction")
        self.womensFictionCheck_book.setChecked(False)
        self.womensFictionCheck_book.setFont(QFont("Vesper Libre", 16))
        self.womensFictionCheck_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')
        self.cookBookCheck_book = QCheckBox("Cookbooks")
        self.cookBookCheck_book.setChecked(False)
        self.cookBookCheck_book.setFont(QFont("Vesper Libre", 16))
        self.cookBookCheck_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')

        self.essayCheck_book = QCheckBox("Essays")
        self.essayCheck_book.setChecked(False)
        self.essayCheck_book.setFont(QFont("Vesper Libre", 16))
        self.essayCheck_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')

        self.memoirCheck_book = QCheckBox("Memoir")
        self.memoirCheck_book.setChecked(False)
        self.memoirCheck_book.setFont(QFont("Vesper Libre", 16))
        self.memoirCheck_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')

        self.poetryCheck_book = QCheckBox("Poetry")
        self.poetryCheck_book.setChecked(False)
        self.poetryCheck_book.setFont(QFont("Vesper Libre", 16))
        self.poetryCheck_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')

        self.trueCrimeCheck_book = QCheckBox("TrueCrime")
        self.trueCrimeCheck_book.setChecked(False)
        self.trueCrimeCheck_book.setFont(QFont("Vesper Libre", 16))
        self.trueCrimeCheck_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')

        self.bookFilterLayout1 = QHBoxLayout()
        self.bookFilterLayout1.addSpacing(10)
        self.bookFilterLayout1.addWidget(self.romanceCheck_book)
        self.bookFilterLayout1.addSpacing(10)
        self.bookFilterLayout1.addWidget(self.mysteryCheck_book)
        self.bookFilterLayout1.addSpacing(10)
        self.bookFilterLayout1.addWidget(self.youngAdultCheck_book)

        self.bookFilterLayout2 = QHBoxLayout()
        self.bookFilterLayout2.addSpacing(10)
        self.bookFilterLayout2.addWidget(self.fantasyAndScienceFictionCheck_book)
        self.bookFilterLayout2.addSpacing(10)
        self.bookFilterLayout2.addWidget(self.classicCheck_book)

        self.bookFilterLayout3 = QHBoxLayout()
        self.bookFilterLayout3.addSpacing(10)
        self.bookFilterLayout3.addWidget(self.thrillersHorrorCheck_book)
        self.bookFilterLayout3.addSpacing(10)
        self.bookFilterLayout3.addWidget(self.childrenFictionCheck_book)

        self.bookFilterLayout4 = QHBoxLayout()
        self.bookFilterLayout4.addSpacing(10)
        self.bookFilterLayout4.addWidget(self.inspirationalReligiousCheck_book)
        self.bookFilterLayout4.addSpacing(10)
        self.bookFilterLayout4.addWidget(self.comicBookCheck_book)

        self.bookFilterLayout5 = QHBoxLayout()
        self.bookFilterLayout5.addSpacing(10)
        self.bookFilterLayout5.addWidget(self.biographyAndAutobiographyCheck_book)
        self.bookFilterLayout5.addSpacing(10)
        self.bookFilterLayout5.addWidget(self.literaryCheck_book)

        self.bookFilterLayout6 = QHBoxLayout()
        self.bookFilterLayout6.addSpacing(10)
        self.bookFilterLayout6.addWidget(self.actionAndAdventureCheck_book)
        self.bookFilterLayout6.addSpacing(10)
        self.bookFilterLayout6.addWidget(self.historicalFictionCheck_book)

        self.bookFilterLayout7 = QHBoxLayout()
        self.bookFilterLayout7.addSpacing(10)
        self.bookFilterLayout7.addWidget(self.scienceFiction_book)
        self.bookFilterLayout7.addSpacing(10)
        self.bookFilterLayout7.addWidget(self.shortStoryCheck_book)

        self.bookFilterLayout8 = QHBoxLayout()
        self.bookFilterLayout8.addSpacing(10)
        self.bookFilterLayout8.addWidget(self.suspenseAndThrillerCheck_book)
        self.bookFilterLayout8.addSpacing(10)
        self.bookFilterLayout8.addWidget(self.womensFictionCheck_book)

        self.bookFilterLayout9 = QHBoxLayout()
        self.bookFilterLayout9.addSpacing(10)
        self.bookFilterLayout9.addWidget(self.cookBookCheck_book)
        self.bookFilterLayout9.addSpacing(10)
        self.bookFilterLayout9.addWidget(self.essayCheck_book)
        self.bookFilterLayout9.addSpacing(10)
        self.bookFilterLayout9.addWidget(self.memoirCheck_book)
        self.bookFilterLayout9.addSpacing(10)
        self.bookFilterLayout9.addWidget(self.poetryCheck_book)

        self.bookFilterLayout10 = QHBoxLayout()
        self.bookFilterLayout10.addSpacing(10)
        self.bookFilterLayout10.addWidget(self.trueCrimeCheck_book)

        self.searchButton_book = QPushButton("Search")
        self.searchButton_book.setFont(QFont("Vesper Libre", 16))
        self.searchButton_book.setStyleSheet('''
                    QPushButton {
                        color: rgb(132, 113, 77);
                        border: 2px solid rgb(132, 113, 77);
                        border-radius: 10px;
                        padding: 0 8px;
                    }
                    QPushButton:hover {
                        background-color: rgb(132, 113, 77);
                        color: white;
                    }
                ''')

        self.bookFilterLayout10.addSpacing(30)
        self.bookFilterLayout10.addWidget(self.searchButton_book)
        self.searchButton_book.clicked.connect(self.getFilter_book)


        filter_menu_book_layout = QVBoxLayout()
        self.filter_menu_book.setLayout(filter_menu_book_layout)

        filter_layouts_book = [
            self.bookFilterLayout1,
            self.bookFilterLayout2,
            self.bookFilterLayout3,
            self.bookFilterLayout4,
            self.bookFilterLayout5,
            self.bookFilterLayout6,
            self.bookFilterLayout7,
            self.bookFilterLayout8,
            self.bookFilterLayout9,
            self.bookFilterLayout10
        ]

        for layout in filter_layouts_book:
            filter_menu_book_layout.addLayout(layout)

        # Book Tab: we need to create the place for putting the label for the coming book
        # my book here is to put the image after the user add their book

        h_layout1_book = QHBoxLayout()
        h_layout1_book.addWidget(self.search_place_book)
        h_layout1_book.addSpacing(20)
        h_layout1_book.addWidget(self.filter_button_book)

        # from librarySystem import librarySystem
        # all_book = librarySystem.getAllBooks()
        # e_book_count = len(all_book)
        #
        # columns = 3
        # rows = (e_book_count + columns - 1) // columns
        #
        # # Add the first layout to the main layout
        # layout.addLayout(h_layout1_book)
        #
        # for row in range(rows):
        #     h_layout_row = QHBoxLayout()
        #
        #     for col in range(columns):
        #         book_index = row * columns + col
        #
        #         if book_index < e_book_count:
        #             widget = QWidget()
        #             widget.setFixedSize(100, 200)
        #
        #             v_layout_item = QVBoxLayout(widget)
        #             v_layout_item.setContentsMargins(0, 0, 0, 0)
        #             v_layout_item.setSpacing(5)
        #
        #             label = QLabel()
        #             pixmap = QPixmap(all_book[book_index].get_picture())
        #             scaled_pixmap = pixmap.scaled(100, 150, Qt.AspectRatioMode.KeepAspectRatio)
        #             label.setPixmap(scaled_pixmap)
        #             label.setAlignment(Qt.AlignCenter)
        #
        #             self.editt_for_book = all_book[book_index]
        #             button = QPushButton(f"{self.editt_for_book.getBookID()}")
        #             button.setStyleSheet('''
        #                         QPushButton {
        #                             border: none;
        #                             color: rgb(132, 113, 77);
        #                             background-color: #F9F6EC;
        #                             text-decoration: underline;
        #                         }
        #
        #                         QPushButton:hover {
        #                             background-color: transparent;
        #                         }
        #                     ''')
        #             button.clicked.connect(self.edit_book)      #edit book
        #
        #             v_layout_item.addWidget(label)
        #             v_layout_item.addWidget(button)
        #
        #             h_layout_row.addWidget(widget)
        #
        #     layout.addLayout(h_layout_row)
        #
        # # Set the layout to the e-book tab widget
        # book_tab.setLayout(layout)
        #remove
        v_layout_book = QVBoxLayout(book_tab)
        v_layout_book.addLayout(h_layout1_book)

        self.tab_widget.removeTab(self.tab_widget.indexOf(book_tab))
        book_tab.setLayout(v_layout_book)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_area.setWidget(book_tab)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.tab_widget.insertTab(0, scroll_area, "Book")
        self.filter_button_book.setMenu(self.filter_menu_book)

        self.search_place_e_book = QLineEdit()
        self.search_place_e_book.setPlaceholderText("Search e-book name")
        self.search_place_e_book.setFont(QFont("Vesper Libre", 20))
        self.search_place_e_book.setStyleSheet('''
            QLineEdit {
                border: 3px solid rgb(132, 113, 77);
                color: rgb(249, 246, 236);
                background-color: rgb(182, 170, 145);
            }
        ''')

        self.filter_button_e_book = QToolButton()
        self.filter_button_e_book.setText("Filter")
        self.filter_button_e_book.setFont(QFont("Vesper Libre", 20))
        self.filter_button_e_book.setStyleSheet('''
            QToolButton {
                border: 3px solid rgb(132, 113, 77);
                color: rgb(249, 246, 236);
                background-color: rgb(182, 170, 145);
            }
            QToolButton::menu-indicator {
                image: none;
            }
        ''')
        self.filter_button_e_book.setPopupMode(QToolButton.InstantPopup)

        self.filter_menu_e_book = QMenu(self.filter_button_e_book)
        self.romanceCheck_e_book = QCheckBox("Romance")
        self.romanceCheck_e_book.setChecked(False)
        self.romanceCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.romanceCheck_e_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')

        self.mysteryCheck_e_book = QCheckBox("Mystery")
        self.mysteryCheck_e_book.setChecked(False)
        self.mysteryCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.mysteryCheck_e_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                        }
                    ''')

        self.fantasyAndScienceFictionCheck_e_book = QCheckBox("Fantasy and science fiction")
        self.fantasyAndScienceFictionCheck_e_book.setChecked(False)
        self.fantasyAndScienceFictionCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.fantasyAndScienceFictionCheck_e_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                        }
                    ''')

        self.thrillersHorrorCheck_e_book = QCheckBox("Thrillers and horror")
        self.thrillersHorrorCheck_e_book.setChecked(False)
        self.thrillersHorrorCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.thrillersHorrorCheck_e_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                        }
                    ''')

        self.youngAdultCheck_e_book = QCheckBox("Young adult")
        self.youngAdultCheck_e_book.setChecked(False)
        self.youngAdultCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.youngAdultCheck_e_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                        }
                    ''')

        self.childrenFictionCheck_e_book = QCheckBox("Children's fiction")
        self.childrenFictionCheck_e_book.setChecked(False)
        self.childrenFictionCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.childrenFictionCheck_e_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                        }
                    ''')

        self.inspirationalReligiousCheck_e_book = QCheckBox("Inspiraltional and religious")
        self.inspirationalReligiousCheck_e_book.setChecked(False)
        self.inspirationalReligiousCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.inspirationalReligiousCheck_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')

        self.biographyAndAutobiographyCheck_e_book = QCheckBox("Biography and autobiography")
        self.biographyAndAutobiographyCheck_e_book.setChecked(False)
        self.biographyAndAutobiographyCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.biographyAndAutobiographyCheck_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')
        self.actionAndAdventureCheck_e_book = QCheckBox("Action and Adventure")
        self.actionAndAdventureCheck_e_book.setChecked(False)
        self.actionAndAdventureCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.actionAndAdventureCheck_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')

        self.classicCheck_e_book = QCheckBox("Classics")
        self.classicCheck_e_book.setChecked(False)
        self.classicCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.classicCheck_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')

        self.comicBookCheck_e_book = QCheckBox("Comic book")
        self.comicBookCheck_e_book.setChecked(False)
        self.comicBookCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.comicBookCheck_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')

        self.historicalFictionCheck_e_book = QCheckBox("Historical fiction")
        self.historicalFictionCheck_e_book.setChecked(False)
        self.historicalFictionCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.historicalFictionCheck_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')

        self.literaryCheck_e_book = QCheckBox("Literary fiction")
        self.literaryCheck_e_book.setChecked(False)
        self.literaryCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.literaryCheck_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')

        self.scienceFiction_e_book = QCheckBox("Science fiction")
        self.scienceFiction_e_book.setChecked(False)
        self.scienceFiction_e_book.setFont(QFont("Vesper Libre", 16))
        self.scienceFiction_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')

        self.shortStoryCheck_e_book = QCheckBox("Short Stories")
        self.shortStoryCheck_e_book.setChecked(False)
        self.shortStoryCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.shortStoryCheck_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')

        self.suspenseAndThrillerCheck_e_book = QCheckBox("Suspense and Thrillers")
        self.suspenseAndThrillerCheck_e_book.setChecked(False)
        self.suspenseAndThrillerCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.suspenseAndThrillerCheck_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')

        self.womensFictionCheck_e_book = QCheckBox("Women's Fiction")
        self.womensFictionCheck_e_book.setChecked(False)
        self.womensFictionCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.womensFictionCheck_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')
        self.cookBookCheck_e_book = QCheckBox("Cookbooks")
        self.cookBookCheck_e_book.setChecked(False)
        self.cookBookCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.cookBookCheck_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')

        self.essayCheck_e_book = QCheckBox("Essays")
        self.essayCheck_e_book.setChecked(False)
        self.essayCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.essayCheck_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')

        self.memoirCheck_e_book = QCheckBox("Memoir")
        self.memoirCheck_e_book.setChecked(False)
        self.memoirCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.memoirCheck_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')

        self.poetryCheck_e_book = QCheckBox("Poetry")
        self.poetryCheck_e_book.setChecked(False)
        self.poetryCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.poetryCheck_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')

        self.trueCrimeCheck_e_book = QCheckBox("TrueCrime")
        self.trueCrimeCheck_e_book.setChecked(False)
        self.trueCrimeCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.trueCrimeCheck_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')

        self.e_bookFilterLayout1 = QHBoxLayout()
        self.e_bookFilterLayout1.addSpacing(10)
        self.e_bookFilterLayout1.addWidget(self.romanceCheck_e_book)
        self.e_bookFilterLayout1.addSpacing(10)
        self.e_bookFilterLayout1.addWidget(self.mysteryCheck_e_book)
        self.e_bookFilterLayout1.addSpacing(10)
        self.e_bookFilterLayout1.addWidget(self.youngAdultCheck_e_book)

        self.e_bookFilterLayout2 = QHBoxLayout()
        self.e_bookFilterLayout2.addSpacing(10)
        self.e_bookFilterLayout2.addWidget(self.fantasyAndScienceFictionCheck_e_book)
        self.e_bookFilterLayout2.addSpacing(10)
        self.e_bookFilterLayout2.addWidget(self.classicCheck_e_book)

        self.e_bookFilterLayout3 = QHBoxLayout()
        self.e_bookFilterLayout3.addSpacing(10)
        self.e_bookFilterLayout3.addWidget(self.thrillersHorrorCheck_e_book)
        self.e_bookFilterLayout3.addSpacing(10)
        self.e_bookFilterLayout3.addWidget(self.childrenFictionCheck_e_book)

        self.e_bookFilterLayout4 = QHBoxLayout()
        self.e_bookFilterLayout4.addSpacing(10)
        self.e_bookFilterLayout4.addWidget(self.inspirationalReligiousCheck_e_book)
        self.e_bookFilterLayout4.addSpacing(10)
        self.e_bookFilterLayout4.addWidget(self.comicBookCheck_e_book)

        self.e_bookFilterLayout5 = QHBoxLayout()
        self.e_bookFilterLayout5.addSpacing(10)
        self.e_bookFilterLayout5.addWidget(self.biographyAndAutobiographyCheck_e_book)
        self.e_bookFilterLayout5.addSpacing(10)
        self.e_bookFilterLayout5.addWidget(self.literaryCheck_e_book)

        self.e_bookFilterLayout6 = QHBoxLayout()
        self.e_bookFilterLayout6.addSpacing(10)
        self.e_bookFilterLayout6.addWidget(self.actionAndAdventureCheck_e_book)
        self.e_bookFilterLayout6.addSpacing(10)
        self.e_bookFilterLayout6.addWidget(self.historicalFictionCheck_e_book)

        self.e_bookFilterLayout7 = QHBoxLayout()
        self.e_bookFilterLayout7.addSpacing(10)
        self.e_bookFilterLayout7.addWidget(self.scienceFiction_e_book)
        self.e_bookFilterLayout7.addSpacing(10)
        self.e_bookFilterLayout7.addWidget(self.shortStoryCheck_e_book)

        self.e_bookFilterLayout8 = QHBoxLayout()
        self.e_bookFilterLayout8.addSpacing(10)
        self.e_bookFilterLayout8.addWidget(self.suspenseAndThrillerCheck_e_book)
        self.e_bookFilterLayout8.addSpacing(10)
        self.e_bookFilterLayout8.addWidget(self.womensFictionCheck_e_book)

        self.e_bookFilterLayout9 = QHBoxLayout()
        self.e_bookFilterLayout9.addSpacing(10)
        self.e_bookFilterLayout9.addWidget(self.cookBookCheck_e_book)
        self.e_bookFilterLayout9.addSpacing(10)
        self.e_bookFilterLayout9.addWidget(self.essayCheck_e_book)
        self.e_bookFilterLayout9.addSpacing(10)
        self.e_bookFilterLayout9.addWidget(self.memoirCheck_e_book)
        self.e_bookFilterLayout9.addSpacing(10)
        self.e_bookFilterLayout9.addWidget(self.poetryCheck_e_book)

        self.e_bookFilterLayout10 = QHBoxLayout()
        self.e_bookFilterLayout10.addSpacing(10)
        self.e_bookFilterLayout10.addWidget(self.trueCrimeCheck_e_book)
        self.searchButton = QPushButton("Search")
        self.searchButton.setFont(QFont("Vesper Libre", 16))
        self.searchButton.setStyleSheet('''
                    QPushButton {
                        background-color: rgb(132, 113, 77);
                        color: white;
                        border-radius: 10px;
                        padding: 10px;
                    }
                    QPushButton:hover {
                        background-color: rgb(163, 140, 97);
                    }
                ''')
        self.e_bookFilterLayout10.addSpacing(30)
        self.e_bookFilterLayout10.addWidget(self.searchButton)
        self.searchButton.clicked.connect(self.getFilter)

        filter_menu_e_book_layout = QVBoxLayout()
        self.filter_menu_e_book.setLayout(filter_menu_e_book_layout)

        filter_layouts_e_book = [
            self.e_bookFilterLayout1,
            self.e_bookFilterLayout2,
            self.e_bookFilterLayout3,
            self.e_bookFilterLayout4,
            self.e_bookFilterLayout5,
            self.e_bookFilterLayout6,
            self.e_bookFilterLayout7,
            self.e_bookFilterLayout8,
            self.e_bookFilterLayout9,
            self.e_bookFilterLayout10
        ]

        for layout in filter_layouts_e_book:
            filter_menu_e_book_layout.addLayout(layout)
        self.filter_button_e_book.setMenu(self.filter_menu_e_book)

        # Create the scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Set e_book_tab as the widget for the scroll area
        scroll_area.setWidget(e_book_tab)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Add the scroll area to the tab_widget
        self.tab_widget.insertTab(1, scroll_area, "E-Book")

        from librarySystem import librarySystem
        # set the history can scroll after this line

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Set e_book_tab as the widget for the scroll area
        scroll_area.setWidget(history_tab)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Add the scroll area to the tab_widget
        self.tab_widget.insertTab(2, scroll_area, "History")

        self.tab_widget.setCurrentIndex(0)

        self.add_button = QPushButton("Add")
        self.add_button.setFont(QFont("Vesper Libre", 20))
        self.add_button.setStyleSheet('''
            QPushButton {
                border: 3px solid rgb(132, 113, 77);
                color: rgb(249, 246, 236);
                background-color: rgb(182, 170, 145);
            }
        ''')

        self.exit_button = QPushButton("Exit")
        self.exit_button.setFont(QFont("Vesper Libre", 20))
        self.exit_button.setStyleSheet('''
            QPushButton {
                border: 3px solid rgb(132, 113, 77);
                color: rgb(249, 246, 236);
                background-color: rgb(182, 170, 145);
            }
        ''')
        h_layout_add = QHBoxLayout()
        h_layout_add.addWidget(self.exit_button)
        h_layout_add.addSpacing(600)
        h_layout_add.addWidget(self.add_button)

        v_layout_add = QVBoxLayout()
        v_layout_add.addLayout(h_layout_add)

        main_layout = QVBoxLayout(central_widget)
        main_layout.addWidget(self.tab_widget)
        main_layout.addLayout(v_layout_add)

        self.setStyleSheet("background-color: #F9F6EC;")
        self.setWindowTitle("Main_menu")
        self.setGeometry(400, 200, 800, 500)
        self.show()

        self.tab_widget.currentChanged.connect(self.on_tab_changed)
        self.add_button.clicked.connect(self.add)
        self.exit_button.clicked.connect(self.exit)

    def on_tab_changed(self, index):
        if index == 2:  # History tab index is 2
            history_tab = self.centralWidget().layout().itemAt(0).widget().widget(2)
            # Refresh the history tab contents
            self.refresh_history_tab(history_tab)
            self.add_button.hide()
            self.exit_button.hide()
        elif index == 1:  # E-Book tab index is 1
            e_book_tab = self.centralWidget().layout().itemAt(0).widget().widget(1)
            self.refresh_e_book_tab(e_book_tab)
            self.add_button.show()
            self.exit_button.show()
        elif index == 0:  # Book tab index is 0
            book_tab = self.centralWidget().layout().itemAt(0).widget().widget(0)
            self.refresh_book_tab(book_tab)
            self.add_button.show()
            self.exit_button.show()
        else:
            self.add_button.show()
            self.exit_button.show()

    def refresh_book_tab(self, book_tab):
        layout = book_tab.layout()
        if layout:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()

        if not layout:
            layout = QVBoxLayout(book_tab)

        h_layout1_e_book = QHBoxLayout()
        h_layout1_e_book.addWidget(self.search_place_book)
        h_layout1_e_book.addSpacing(20)
        h_layout1_e_book.addWidget(self.filter_button_book)
        from librarySystem import librarySystem
        all_e_book = librarySystem.getAllBooks()
        e_book_count = len(all_e_book)

        columns = 3
        rows = (e_book_count + columns - 1) // columns

        # Add the first layout to the main layout
        layout.addLayout(h_layout1_e_book)

        for row in range(rows):
            h_layout_row = QHBoxLayout()

            for col in range(columns):
                book_index = row * columns + col

                if book_index < e_book_count:
                    widget = QWidget()
                    widget.setFixedSize(100, 200)

                    v_layout_item = QVBoxLayout(widget)
                    v_layout_item.setContentsMargins(0, 0, 0, 0)
                    v_layout_item.setSpacing(5)

                    label = QLabel()
                    pixmap = QPixmap(all_e_book[book_index].get_picture())
                    scaled_pixmap = pixmap.scaled(100, 150, Qt.AspectRatioMode.KeepAspectRatio)
                    label.setPixmap(scaled_pixmap)
                    label.setAlignment(Qt.AlignCenter)

                    button = QPushButton(f"{all_e_book[book_index].getBookID()}")
                    button.setStyleSheet('''
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
                    self.editt_book = all_e_book[book_index]
                    button.clicked.connect(self.edit_book)

                    v_layout_item.addWidget(label)
                    v_layout_item.addWidget(button)

                    h_layout_row.addWidget(widget)

            layout.addLayout(h_layout_row)

        # Set the layout to the e-book tab widget
        book_tab.setLayout(layout)

    def refresh_e_book_tab(self, e_book_tab):
        layout = e_book_tab.layout()
        if layout:
            while layout.count():
                item = layout.takeAt(0)
                layout.removeItem(item)

        if not layout:
            layout = QVBoxLayout(e_book_tab)

        h_layout1_e_book = QHBoxLayout()
        h_layout1_e_book.addWidget(self.search_place_e_book)
        h_layout1_e_book.addSpacing(20)
        h_layout1_e_book.addWidget(self.filter_button_e_book)
        from librarySystem import librarySystem
        all_e_book = librarySystem.getAllEbook()
        e_book_count = len(all_e_book)

        columns = 3
        rows = (e_book_count + columns - 1) // columns

        # Add the first layout to the main layout
        layout.addLayout(h_layout1_e_book)

        for row in range(rows):
            h_layout_row = QHBoxLayout()

            for col in range(columns):
                book_index = row * columns + col

                if book_index < e_book_count:
                    widget = QWidget()
                    widget.setFixedSize(100, 200)

                    v_layout_item = QVBoxLayout(widget)
                    v_layout_item.setContentsMargins(0, 0, 0, 0)
                    v_layout_item.setSpacing(5)

                    label = QLabel()
                    pixmap = QPixmap(all_e_book[book_index].get_picture())
                    scaled_pixmap = pixmap.scaled(100, 150, Qt.AspectRatioMode.KeepAspectRatio)
                    label.setPixmap(scaled_pixmap)
                    label.setAlignment(Qt.AlignCenter)

                    self.editt_book = all_e_book[book_index]
                    button = QPushButton(f"{self.editt_book.getBookID()}")
                    button.setStyleSheet('''
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
                    button.clicked.connect(self.edit_book)

                    v_layout_item.addWidget(label)
                    v_layout_item.addWidget(button)

                    h_layout_row.addWidget(widget)

            layout.addLayout(h_layout_row)

        # Set the layout to the e-book tab widget
        e_book_tab.setLayout(layout)

    # recieve enter key press event from user
    def keyPressEvent(self, event):
        # if the user presses enter, search for the book
        if event.key() == Qt.Key_Return:
            self.search_Ebook()
    def search_Ebook(self):
        # get the search term from the user
        search_term = self.search_place_e_book.text()
        # search for the book
        from librarySystem import librarySystem
        book = librarySystem.searchEbook(search_term)
        librarySystem.ebook_list = book
        # refresh the e-book tab
        self.refresh_e_book_tab(self.centralWidget().layout().itemAt(0).widget().widget(1))

    def BookKeyPressEvent(self, event):
        # if the user presses enter, search for the book
        if event.key() == Qt.Key_Return:
            self.search_book()

    def search_book(self):
        # get the search term from the user
        search_term = self.search_place_book.text()
        # search for the book
        from librarySystem import librarySystem
        book = librarySystem.searchBook(search_term)
        librarySystem.book_list = book
        # refresh the book tab
        self.refresh_book_tab(self.centralWidget().layout().itemAt(0).widget().widget(0))



    def add(self):
        from librarySystem import librarySystem
        librarySystem.setState("Add_book")
        self.close()

    def exit(self):
        from librarySystem import librarySystem
        librarySystem.finishAndSave()
        self.close()

    def refresh_history_tab(self, history_tab):

        # Clear the existing layout
        layout = history_tab.layout()
        if layout:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    layout.removeWidget(widget)
                    widget.setParent(None)
                    widget.deleteLater()

        # Create a new layout if it doesn't exist
        if not layout:
            layout = QVBoxLayout(history_tab)

        from librarySystem import librarySystem
        # Retrieve the updated history data
        history = librarySystem.getHistory()

        for item in history:
            if item.type == 1:
                item.type = "Book"
            elif item.type == 2:
                item.type = "E-Book"
            k = str(item.type) + " " + str(item.name) + " " + str(item.author) + " " + str(item.date)
            label = QLabel()
            label.setText(k)
            label.setFont(QFont("Vesper Libre", 18))
            label.setStyleSheet('''
                QLabel {
                    color: black;
                }
            ''')
            layout.addWidget(label)

        layout.addSpacing(400)
        history_tab.setLayout(layout)

    def getFilter_book(self):
        self.checkList_book = []
        filter_book = [self.romanceCheck_book, self.mysteryCheck_book, self.fantasyAndScienceFictionCheck_book,
                    self.thrillersHorrorCheck_book, self.youngAdultCheck_book,
                    self.childrenFictionCheck_book, self.inspirationalReligiousCheck_book,
                    self.biographyAndAutobiographyCheck_book,
                    self.actionAndAdventureCheck_book, self.classicCheck_book, self.comicBookCheck_book,
                    self.historicalFictionCheck_book, self.literaryCheck_book, self.scienceFiction_book,
                    self.shortStoryCheck_book, self.suspenseAndThrillerCheck_book,
                    self.womensFictionCheck_book, self.cookBookCheck_book, self.essayCheck_book,
                    self.memoirCheck_book, self.poetryCheck_book, self.trueCrimeCheck_book]
        for i in range(len(filter_book)):
            if filter_book[i].isChecked():
                self.checkList_book.append(filter_book[i].text())
            else:
                self.checkList_book.append("None")
        from librarySystem import librarySystem
        temp = librarySystem.filterCategoryBook(self.checkList_book)
        return temp





    def getFilter(self):
        self.checkList = []
        filter_ebook = [self.romanceCheck_e_book, self.mysteryCheck_e_book, self.fantasyAndScienceFictionCheck_e_book,
                  self.thrillersHorrorCheck_e_book, self.youngAdultCheck_e_book,
                  self.childrenFictionCheck_e_book, self.inspirationalReligiousCheck_e_book,
                  self.biographyAndAutobiographyCheck_e_book,
                  self.actionAndAdventureCheck_e_book, self.classicCheck_e_book, self.comicBookCheck_e_book,
                  self.historicalFictionCheck_e_book, self.literaryCheck_e_book, self.scienceFiction_e_book,
                  self.shortStoryCheck_e_book, self.suspenseAndThrillerCheck_e_book,
                  self.womensFictionCheck_e_book, self.cookBookCheck_e_book, self.essayCheck_e_book,
                  self.memoirCheck_e_book, self.poetryCheck_e_book,
                  self.trueCrimeCheck_e_book]
        for i in range(len(filter_ebook)):
            if filter_ebook[i].isChecked():
                self.checkList.append(filter_ebook[i].text())
            else:
                self.checkList.append("None")
        from librarySystem import librarySystem
        temp = librarySystem.filterCategoryEbook(self.checkList)
        return temp  # Return the list of books that match the filter
    def edit_book(self):
        from librarySystem import librarySystem
        librarySystem.setUserSelect(self.editt_book)
        librarySystem.setState("Edit_Ebook")

    # def edit_forbook(self):
    #     from librarySystem import librarySystem
    #     librarySystem.setUserSelect(self.editt_for_book)
    #     librarySystem.setState("Edit_book")




if __name__ == "__main__":
    app = QApplication([])
    ui = Main_menu()
    app.exec()
