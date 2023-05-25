from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *


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

        search_place = QLineEdit()
        search_place.setPlaceholderText("Search book name")
        search_place.setFont(QFont("Vesper Libre", 20))
        search_place.setStyleSheet('''
            QLineEdit {
                border: 3px solid rgb(132, 113, 77);
                color: rgb(249, 246, 236);
                background-color: rgb(182, 170, 145);
            }
        ''')

        self.filter_button = QToolButton()
        self.filter_button.setText("Filter")
        self.filter_button.setFont(QFont("Vesper Libre", 20))
        self.filter_button.setStyleSheet('''
            QToolButton {
                border: 3px solid rgb(132, 113, 77);
                color: rgb(249, 246, 236);
                background-color: rgb(182, 170, 145);
            }
            QToolButton::menu-indicator {
                image: none;
            }
        ''')
        self.filter_button.setPopupMode(QToolButton.InstantPopup)

        self.filter_menu = QMenu(self.filter_button)
        self.romanceCheck = QCheckBox("Romance")
        self.romanceCheck.setChecked(False)
        self.romanceCheck.setFont(QFont("Vesper Libre", 16))
        self.romanceCheck.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
            }
        ''')
        filter_layout1 = QHBoxLayout()
        filter_layout1.addSpacing(10)
        filter_layout1.addWidget(self.romanceCheck)
        self.mysteryCheck = QCheckBox("Mystery")
        self.mysteryCheck.setChecked(False)
        self.mysteryCheck.setFont(QFont("Vesper Libre", 16))
        self.mysteryCheck.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
            }
        ''')
        filter_layout1.addSpacing(10)
        filter_layout1.addWidget(self.mysteryCheck)
        self.fantasyAndScienceFictionCheck = QCheckBox("Fantasy and Science Fiction")
        self.fantasyAndScienceFictionCheck.setChecked(False)
        self.fantasyAndScienceFictionCheck.setFont(QFont("Vesper Libre", 16))
        self.fantasyAndScienceFictionCheck.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
            }
        ''')
        filter_layout2 = QHBoxLayout()
        filter_layout2.addSpacing(10)
        filter_layout2.addWidget(self.fantasyAndScienceFictionCheck)
        self.thrillersHorrorCheck = QCheckBox("Thrillers and Horror")
        self.thrillersHorrorCheck.setChecked(False)
        self.thrillersHorrorCheck.setFont(QFont("Vesper Libre", 16))
        self.thrillersHorrorCheck.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
            }
        ''')
        filter_layout3 = QHBoxLayout()
        filter_layout3.addSpacing(10)
        filter_layout3.addWidget(self.thrillersHorrorCheck)

        self.youngAdultCheck = QCheckBox("Young Adult")
        self.youngAdultCheck.setChecked(False)
        self.youngAdultCheck.setFont(QFont("Vesper Libre", 16))
        self.youngAdultCheck.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
            }
        ''')
        filter_layout1.addSpacing(10)
        filter_layout1.addWidget(self.youngAdultCheck)
        self.childrenFictionCheck = QCheckBox("Children Fiction")
        self.childrenFictionCheck.setChecked(False)
        self.childrenFictionCheck.setFont(QFont("Vesper Libre", 16))
        self.childrenFictionCheck.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
            }
        ''')
        filter_layout4 = QHBoxLayout()
        filter_layout3.addSpacing(10)
        filter_layout3.addWidget(self.childrenFictionCheck)

        self.inspirationalReligiousCheck = QCheckBox("Inspirational and Religious")
        self.inspirationalReligiousCheck.setChecked(False)
        self.inspirationalReligiousCheck.setFont(QFont("Vesper Libre", 16))
        self.inspirationalReligiousCheck.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
            }
        ''')
        filter_layout4.addSpacing(10)
        filter_layout4.addWidget(self.inspirationalReligiousCheck)

        self.biographyAndAutobiographyCheck = QCheckBox("Biography and Autobiography")
        self.biographyAndAutobiographyCheck.setChecked(False)
        self.biographyAndAutobiographyCheck.setFont(QFont("Vesper Libre", 16))
        self.biographyAndAutobiographyCheck.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
            }
        ''')
        filter_layout5 = QHBoxLayout()
        filter_layout5.addSpacing(10)
        filter_layout5.addWidget(self.biographyAndAutobiographyCheck)

        self.actionAndAdventureCheck = QCheckBox("Action and Adventure")
        self.actionAndAdventureCheck.setChecked(False)
        self.actionAndAdventureCheck.setFont(QFont("Vesper Libre", 16))
        self.actionAndAdventureCheck.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
            }
        ''')
        filter_layout6 = QHBoxLayout()
        filter_layout6.addSpacing(10)
        filter_layout6.addWidget(self.actionAndAdventureCheck)

        self.classicCheck = QCheckBox("Classic")
        self.classicCheck.setChecked(False)
        self.classicCheck.setFont(QFont("Vesper Libre", 16))
        self.classicCheck.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
            }
        ''')
        filter_layout2.addSpacing(10)
        filter_layout2.addWidget(self.classicCheck)

        self.comicBookCheck = QCheckBox("Comic Book")
        self.comicBookCheck.setChecked(False)
        self.comicBookCheck.setFont(QFont("Vesper Libre", 16))
        self.comicBookCheck.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
            }
        ''')
        filter_layout4.addSpacing(10)
        filter_layout4.addWidget(self.comicBookCheck)

        self.historicalFictionCheck = QCheckBox("Historical Fiction")
        self.historicalFictionCheck.setChecked(False)
        self.historicalFictionCheck.setFont(QFont("Vesper Libre", 16))
        self.historicalFictionCheck.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
            }
        ''')
        filter_layout6.addSpacing(10)
        filter_layout6.addWidget(self.historicalFictionCheck)

        self.literaryCheck = QCheckBox("Literary")
        self.literaryCheck.setChecked(False)
        self.literaryCheck.setFont(QFont("Vesper Libre", 16))
        self.literaryCheck.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
            }
        ''')
        filter_layout5.addSpacing(10)
        filter_layout5.addWidget(self.literaryCheck)

        self.scienceFiction = QCheckBox("Science Fiction")
        self.scienceFiction.setChecked(False)
        self.scienceFiction.setFont(QFont("Vesper Libre", 16))
        self.scienceFiction.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
            }
        ''')
        filter_layout7 = QHBoxLayout()
        filter_layout7.addSpacing(10)
        filter_layout7.addWidget(self.scienceFiction)

        self.shortStoryCheck = QCheckBox("Short Story")
        self.shortStoryCheck.setChecked(False)
        self.shortStoryCheck.setFont(QFont("Vesper Libre", 16))
        self.shortStoryCheck.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
            }
        ''')
        filter_layout7.addSpacing(10)
        filter_layout7.addWidget(self.shortStoryCheck)

        self.suspenseAndThrillerCheck = QCheckBox("Suspense and Thriller")
        self.suspenseAndThrillerCheck.setChecked(False)
        self.suspenseAndThrillerCheck.setFont(QFont("Vesper Libre", 16))
        self.suspenseAndThrillerCheck.setStyleSheet('''
            QCheckBox {
                color: rgb(132, 113, 77);
            }
        ''')
        filter_layout8 = QHBoxLayout()
        filter_layout8.addSpacing(10)
        filter_layout8.addWidget(self.suspenseAndThrillerCheck)


        self.filter_menu.setLayout(QVBoxLayout())
        self.filter_menu.layout().addLayout(filter_layout1)
        self.filter_menu.layout().addLayout(filter_layout2)
        self.filter_menu.layout().addLayout(filter_layout3)
        self.filter_menu.layout().addLayout(filter_layout4)
        self.filter_menu.layout().addLayout(filter_layout5)
        self.filter_menu.layout().addLayout(filter_layout6)
        self.filter_menu.layout().addLayout(filter_layout7)
        self.filter_menu.layout().addLayout(filter_layout8)


        # Connect the combobox currentIndexChanged signal to a slot



        self.filter_button.setMenu(self.filter_menu)

        h_layout1 = QHBoxLayout()
        h_layout1.addWidget(search_place)
        h_layout1.addSpacing(20)
        h_layout1.addWidget(self.filter_button)

        v_layout = QVBoxLayout(e_book_tab)
        v_layout.addLayout(h_layout1)

        main_layout = QVBoxLayout(central_widget)
        main_layout.addWidget(tab_widget)

        self.setStyleSheet("background-color: #F9F6EC;")
        self.setWindowTitle("Main_menu")
        self.setGeometry(400, 200, 800, 500)
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    ui = Main_menu()
    app.exec()
