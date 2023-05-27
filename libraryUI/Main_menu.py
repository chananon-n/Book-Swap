from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Main_menu(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        tab_widget = QTabWidget()
        tab_widget.setFont(QFont("Vesper Libre", 20))
        tab_widget.setStyleSheet('''
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

        tab_widget.addTab(book_tab, "Book")
        tab_widget.addTab(e_book_tab, "E-book")
        tab_widget.addTab(history_tab, "History")

        search_place_book = QLineEdit()
        search_place_book.setPlaceholderText("Search book name")
        search_place_book.setFont(QFont("Vesper Libre", 20))
        search_place_book.setStyleSheet('''
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

        self.fantasyAndScienceFictionCheck_book = QCheckBox("Fantasy and Science Fiction")
        self.fantasyAndScienceFictionCheck_book.setChecked(False)
        self.fantasyAndScienceFictionCheck_book.setFont(QFont("Vesper Libre", 16))
        self.fantasyAndScienceFictionCheck_book.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
                }
            ''')

        self.thrillersHorrorCheck_book = QCheckBox("Thrillers and Horror")
        self.thrillersHorrorCheck_book.setChecked(False)
        self.thrillersHorrorCheck_book.setFont(QFont("Vesper Libre", 16))
        self.thrillersHorrorCheck_book.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
                }
            ''')

        self.youngAdultCheck_book = QCheckBox("Young Adult")
        self.youngAdultCheck_book.setChecked(False)
        self.youngAdultCheck_book.setFont(QFont("Vesper Libre", 16))
        self.youngAdultCheck_book.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
                }
            ''')

        self.childrenFictionCheck_book = QCheckBox("Children Fiction")
        self.childrenFictionCheck_book.setChecked(False)
        self.childrenFictionCheck_book.setFont(QFont("Vesper Libre", 16))
        self.childrenFictionCheck_book.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
                }
            ''')

        self.inspirationalReligiousCheck_book = QCheckBox("Inspirational and Religious")
        self.inspirationalReligiousCheck_book.setChecked(False)
        self.inspirationalReligiousCheck_book.setFont(QFont("Vesper Libre", 16))
        self.inspirationalReligiousCheck_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')

        self.biographyAndAutobiographyCheck_book = QCheckBox("Biography and Autobiography")
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

        self.classicCheck_book = QCheckBox("Classic")
        self.classicCheck_book.setChecked(False)
        self.classicCheck_book.setFont(QFont("Vesper Libre", 16))
        self.classicCheck_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')

        self.comicBookCheck_book = QCheckBox("Comic Book")
        self.comicBookCheck_book.setChecked(False)
        self.comicBookCheck_book.setFont(QFont("Vesper Libre", 16))
        self.comicBookCheck_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')

        self.historicalFictionCheck_book = QCheckBox("Historical Fiction")
        self.historicalFictionCheck_book.setChecked(False)
        self.historicalFictionCheck_book.setFont(QFont("Vesper Libre", 16))
        self.historicalFictionCheck_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')

        self.literaryCheck_book = QCheckBox("Literary")
        self.literaryCheck_book.setChecked(False)
        self.literaryCheck_book.setFont(QFont("Vesper Libre", 16))
        self.literaryCheck_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')

        self.scienceFiction_book = QCheckBox("Science Fiction")
        self.scienceFiction_book.setChecked(False)
        self.scienceFiction_book.setFont(QFont("Vesper Libre", 16))
        self.scienceFiction_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')

        self.shortStoryCheck_book = QCheckBox("Short Story")
        self.shortStoryCheck_book.setChecked(False)
        self.shortStoryCheck_book.setFont(QFont("Vesper Libre", 16))
        self.shortStoryCheck_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')

        self.suspenseAndThrillerCheck_book = QCheckBox("Suspense and Thriller")
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
        self.cookBookCheck_book = QCheckBox("Cook Book")
        self.cookBookCheck_book.setChecked(False)
        self.cookBookCheck_book.setFont(QFont("Vesper Libre", 16))
        self.cookBookCheck_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                    }
                ''')

        self.essayCheck_book = QCheckBox("Essay")
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

        self.trueCrimeCheck_book = QCheckBox("True Crime")
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
        h_layout1_book.addWidget(search_place_book)
        h_layout1_book.addSpacing(20)
        h_layout1_book.addWidget(self.filter_button_book)

        v_layout_book = QVBoxLayout(book_tab)
        v_layout_book.addLayout(h_layout1_book)

        tab_widget.removeTab(tab_widget.indexOf(book_tab))
        book_tab.setLayout(v_layout_book)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_area.setWidget(book_tab)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        tab_widget.insertTab(0, scroll_area, "Book")
        self.filter_button_book.setMenu(self.filter_menu_book)

        search_place_e_book = QLineEdit()
        search_place_e_book.setPlaceholderText("Search e-book name")
        search_place_e_book.setFont(QFont("Vesper Libre", 20))
        search_place_e_book.setStyleSheet('''
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

        self.fantasyAndScienceFictionCheck_e_book = QCheckBox("Fantasy and Science Fiction")
        self.fantasyAndScienceFictionCheck_e_book.setChecked(False)
        self.fantasyAndScienceFictionCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.fantasyAndScienceFictionCheck_e_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                        }
                    ''')

        self.thrillersHorrorCheck_e_book = QCheckBox("Thrillers and Horror")
        self.thrillersHorrorCheck_e_book.setChecked(False)
        self.thrillersHorrorCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.thrillersHorrorCheck_e_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                        }
                    ''')

        self.youngAdultCheck_e_book = QCheckBox("Young Adult")
        self.youngAdultCheck_e_book.setChecked(False)
        self.youngAdultCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.youngAdultCheck_e_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                        }
                    ''')

        self.childrenFictionCheck_e_book = QCheckBox("Children Fiction")
        self.childrenFictionCheck_e_book.setChecked(False)
        self.childrenFictionCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.childrenFictionCheck_e_book.setStyleSheet('''
                    QCheckBox {
                        color: rgb(132, 113, 77);
                        }
                    ''')

        self.inspirationalReligiousCheck_e_book = QCheckBox("Inspirational and Religious")
        self.inspirationalReligiousCheck_e_book.setChecked(False)
        self.inspirationalReligiousCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.inspirationalReligiousCheck_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')

        self.biographyAndAutobiographyCheck_e_book = QCheckBox("Biography and Autobiography")
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

        self.classicCheck_e_book = QCheckBox("Classic")
        self.classicCheck_e_book.setChecked(False)
        self.classicCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.classicCheck_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')

        self.comicBookCheck_e_book = QCheckBox("Comic Book")
        self.comicBookCheck_e_book.setChecked(False)
        self.comicBookCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.comicBookCheck_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')

        self.historicalFictionCheck_e_book = QCheckBox("Historical Fiction")
        self.historicalFictionCheck_e_book.setChecked(False)
        self.historicalFictionCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.historicalFictionCheck_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')

        self.literaryCheck_e_book = QCheckBox("Literary")
        self.literaryCheck_e_book.setChecked(False)
        self.literaryCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.literaryCheck_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')

        self.scienceFiction_e_book = QCheckBox("Science Fiction")
        self.scienceFiction_e_book.setChecked(False)
        self.scienceFiction_e_book.setFont(QFont("Vesper Libre", 16))
        self.scienceFiction_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')

        self.shortStoryCheck_e_book = QCheckBox("Short Story")
        self.shortStoryCheck_e_book.setChecked(False)
        self.shortStoryCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.shortStoryCheck_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')

        self.suspenseAndThrillerCheck_e_book = QCheckBox("Suspense and Thriller")
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
        self.cookBookCheck_e_book = QCheckBox("Cook Book")
        self.cookBookCheck_e_book.setChecked(False)
        self.cookBookCheck_e_book.setFont(QFont("Vesper Libre", 16))
        self.cookBookCheck_e_book.setStyleSheet('''
                            QCheckBox {
                                color: rgb(132, 113, 77);
                            }
                        ''')

        self.essayCheck_e_book = QCheckBox("Essay")
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

        self.trueCrimeCheck_e_book = QCheckBox("True Crime")
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

        h_layout1_e_book = QHBoxLayout()
        h_layout1_e_book.addWidget(search_place_e_book)
        h_layout1_e_book.addSpacing(20)
        h_layout1_e_book.addWidget(self.filter_button_e_book)

        v_layout_e_book = QVBoxLayout(e_book_tab)
        v_layout_e_book.addLayout(h_layout1_e_book)

        #scroll of e-book is after this line
        tab_widget.removeTab(tab_widget.indexOf(e_book_tab))
        e_book_tab.setLayout(v_layout_e_book)

        # Create the scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Set e_book_tab as the widget for the scroll area
        scroll_area.setWidget(e_book_tab)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Add the scroll area to the tab_widget
        tab_widget.insertTab(1, scroll_area, "E-Book")

        #set the history can scroll after this line
        # history = librarySystem.getHistory(12345678)
        # history_count = len(history)
        # v_layout_history = QVBoxLayout(history_tab)
        # for i in range(history_count):
        #     v_layout_history.addSpacing(10)
        #     v_layout_history.addWidget(QLabel(history[i]))
        #     v_layout_history.addSpacing(10)
        # history_tab.setLayout(v_layout_history)


        tab_widget.setCurrentIndex(0)


        self.add_button = QPushButton("Add")
        self.add_button.setFont(QFont("Vesper Libre", 20))
        self.add_button.setStyleSheet('''
            QPushButton {
                border: 3px solid rgb(132, 113, 77);
                color: rgb(249, 246, 236);
                background-color: rgb(182, 170, 145);
            }
        ''')
        h_layout_add = QHBoxLayout()
        h_layout_add.addSpacing(700)
        h_layout_add.addWidget(self.add_button)

        v_layout_add = QVBoxLayout()
        v_layout_add.addLayout(h_layout_add)

        main_layout = QVBoxLayout(central_widget)
        main_layout.addWidget(tab_widget)
        main_layout.addLayout(v_layout_add)

        self.setStyleSheet("background-color: #F9F6EC;")
        self.setWindowTitle("Main_menu")
        self.setGeometry(400, 200, 800, 500)
        self.show()

        tab_widget.currentChanged.connect(self.on_tab_changed)

    def on_tab_changed(self, index):
        if index == 2:  # History tab index is 2
            self.add_button.hide()
        else:
            self.add_button.show()


if __name__ == "__main__":
    app = QApplication([])
    ui = Main_menu()
    app.exec()
