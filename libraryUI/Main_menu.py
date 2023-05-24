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
        self.filter_combobox = QComboBox(self.filter_menu)
        self.filter_combobox.addItems(["Food", "Drink", "Other"])
        self.filter_combobox.setStyleSheet('''
                    QComboBox {
                        color: rgb(249, 246, 236);
                        background-color: rgb(182, 170, 145);
                    }
                    QComboBox QAbstractItemView {
                        border: 2px solid rgb(132, 113, 77);
                        color: rgb(249, 246, 236);
                        background-color: rgb(182, 170, 145);
                        selection-background-color: rgb(132, 113, 77);
                    }
                ''')
        self.filter_menu.setLayout(QVBoxLayout())
        self.filter_menu.layout().addWidget(self.filter_combobox)

        # Calculate the maximum width of the menu based on the combobox items
        max_width = 0
        font_metrics = self.filter_combobox.fontMetrics()
        for index in range(self.filter_combobox.count()):
            text = self.filter_combobox.itemText(index)
            width = font_metrics.boundingRect(text).width()
            max_width = max(max_width, width)

        # Set the width of the menu
        self.filter_menu.setFixedWidth(max_width + 20)

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
