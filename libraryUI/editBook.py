from PySide6.QtGui import QPixmap, QFont
from PySide6.QtWidgets import QMainWindow, QLabel, QHBoxLayout, QWidget, QLineEdit, QTextEdit, QCheckBox
from PySide6.QtCore import *


class EditEbook(QMainWindow):
    def __init__(self):
        super().__init__()
        self.price = 0.0
        self.type = "ebook"
        self.title = ""
        self.author = ""
        self.description = ""
        self.category = []
        self.image = QLabel()
        # replace path of your image at placeholder.png
        self.placeholder_image = QPixmap("placeholder.png")

        self.image.setPixmap(self.placeholder_image)
        self.image.setScaledContents(True)
        self.image.setMinimumSize(250, 250)
        self.image.setAlignment(Qt.AlignCenter)
        self.image.setStyleSheet("border: 2px dashed gray; color: gray;")
        self.image.setText("Please drag and droup a book image here")

        layout = QHBoxLayout()
        layout.addWidget(self.image)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        self.setAcceptDrops(True)
        blank = QLabel("")

        hLayout1 = QHBoxLayout()
        hLayout1.addWidget(blank)
        hLayout1.addWidget(self.image)
        hLayout1.addWidget(blank)

        title = QLabel("Title")
        title.setFont(QFont("Vesper Libre", 25))
        title.setStyleSheet('''
        QLabel {
        color: rgb(132, 113, 77);
        }
        ''')

        self.titleName = QLineEdit(self)
        self.titleName.setPlaceholderText(self.title)
        self.titleName.setFont(QFont("Vesper Libre", 20))
        self.titleName.setStyleSheet('''
        QLineEdit {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(148, 132, 99);
        }
        ''')

        hLayout2 = QHBoxLayout()
        hLayout2.addSpacing(30)
        hLayout2.addWidget(title)
        hLayout2.addSpacing(40)
        hLayout2.addWidget(self.titleName)
        hLayout2.addSpacing(30)

        author = QLabel("Author")
        author.setFont(QFont("Vesper Libre", 25))
        author.setStyleSheet('''
        QLabel {
        color: rgb(132, 113, 77);
        }
        ''')

        self.authorName = QLineEdit(self)
        self.authorName.setPlaceholderText(self.author)
        self.authorName.setFont(QFont("Vesper Libre", 20))
        self.authorName.setStyleSheet('''
        QLineEdit {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(148, 132, 99);
        }
        ''')

        hLayout3 = QHBoxLayout()
        hLayout3.addSpacing(30)
        hLayout3.addWidget(author)
        hLayout3.addSpacing(15)
        hLayout3.addWidget(self.authorName)
        hLayout3.addSpacing(30)

        description = QLabel("Description")
        description.setFont(QFont("Vesper Libre", 25))
        description.setStyleSheet('''
        QLabel {
        color: rgb(132, 113, 77);
        }
        ''')

        hLayout4 = QHBoxLayout()
        hLayout4.addSpacing(30)
        hLayout4.addWidget(description)

        self.descriptionName = QTextEdit(self)
        self.descriptionName.setPlaceholderText(self.description)
        self.descriptionName.setFont(QFont("Vesper Libre", 20))
        self.descriptionName.setStyleSheet('''
        QTextEdit {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(148, 132, 99);
        }
        ''')

        hLayout5 = QHBoxLayout()
        hLayout5.addSpacing(50)
        hLayout5.addWidget(self.descriptionName)
        hLayout5.addSpacing(30)

        category = QLabel("Category")
        category.setFont(QFont("Vesper Libre", 25))
        category.setStyleSheet('''
        QLabel {
        color: rgb(132, 113, 77);
        }
        ''')

        hLayout6 = QHBoxLayout()
        hLayout6.addSpacing(50)
        hLayout6.addWidget(category)

        self.romanceButton = QCheckBox("Romance")
        self.romanceButton.setChecked(False)
        self.romanceButton.setFont(QFont("Vesper Libre", 20))
        self.romanceButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        self.mysteryButton = QCheckBox("Mystery")
        self.mysteryButton.setChecked(False)
        self.mysteryButton.setFont(QFont("Vesper Libre", 20))
        self.mysteryButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        hLayout7 = QHBoxLayout()
        hLayout7.addSpacing(50)
        hLayout7.addWidget(self.romanceButton)
        hLayout7.addSpacing(25)
        hLayout7.addWidget(self.mysteryButton)

        self.fantasyAndScienceFictionButton = QCheckBox("Fantasy and Science Fiction")
        self.fantasyAndScienceFictionButton.setChecked(False)
        self.fantasyAndScienceFictionButton.setFont(QFont("Vesper Libre", 20))
        self.fantasyAndScienceFictionButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        self.thrillersAndHorrorButton = QCheckBox("Thrillers and Horror")
        self.thrillersAndHorrorButton.setChecked(False)
        self.thrillersAndHorrorButton.setFont(QFont("Vesper Libre", 20))
        self.thrillersAndHorrorButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        hLayout8 = QHBoxLayout()
        hLayout8.addSpacing(50)
        hLayout8.addWidget(self.fantasyAndScienceFictionButton)
        hLayout8.addSpacing(25)
        hLayout8.addWidget(self.thrillersAndHorrorButton)

        self.youngAndAdultButton = QCheckBox("Young and Adult")
        self.youngAndAdultButton.setChecked(False)
        self.youngAndAdultButton.setFont(QFont("Vesper Libre", 20))
        self.youngAndAdultButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        self.childrenFictionButton = QCheckBox("Children Fiction")
        self.childrenFictionButton.setChecked(False)
        self.childrenFictionButton.setFont(QFont("Vesper Libre", 20))
        self.childrenFictionButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        hLayout9 = QHBoxLayout()
        hLayout9.addSpacing(50)
        hLayout9.addWidget(self.youngAndAdultButton)
        hLayout9.addSpacing(25)
        hLayout9.addWidget(self.childrenFictionButton)

        self.inspirationalAndReligiousButton = QCheckBox("Inspirational and Religious")
        self.inspirationalAndReligiousButton.setChecked(False)
        self.inspirationalAndReligiousButton.setFont(QFont("Vesper Libre", 20))
        self.inspirationalAndReligiousButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        self.biographyAndAutobiographyButton = QCheckBox("Biography and Autobiography")
        self.biographyAndAutobiographyButton.setChecked(False)
        self.biographyAndAutobiographyButton.setFont(QFont("Vesper Libre", 20))
        self.biographyAndAutobiographyButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        hLayout10 = QHBoxLayout()
        hLayout10.addSpacing(50)
        hLayout10.addWidget(self.inspirationalAndReligiousButton)
        hLayout10.addSpacing(25)
        hLayout10.addWidget(self.biographyAndAutobiographyButton)

        self.actionAndAdventureButton = QCheckBox("Action and Adventure")
        self.actionAndAdventureButton.setChecked(False)
        self.actionAndAdventureButton.setFont(QFont("Vesper Libre", 20))
        self.actionAndAdventureButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        self.classicButton = QCheckBox("Classic")
        self.classicButton.setChecked(False)
        self.classicButton.setFont(QFont("Vesper Libre", 20))
        self.classicButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        hLayout11 = QHBoxLayout()
        hLayout11.addSpacing(50)
        hLayout11.addWidget(self.actionAndAdventureButton)
        hLayout11.addSpacing(25)
        hLayout11.addWidget(self.classicButton)

        self.comicButton = QCheckBox("Comic book")
        self.comicButton.setChecked(False)
        self.comicButton.setFont(QFont("Vesper Libre", 20))
        self.comicButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        self.historicalButton = QCheckBox("Historical fiction")
        self.historicalButton.setChecked(False)
        self.historicalButton.setFont(QFont("Vesper Libre", 20))
        self.historicalButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        hLayout12 = QHBoxLayout()
        hLayout12.addSpacing(50)
        hLayout12.addWidget(self.comicButton)
        hLayout12.addSpacing(25)
        hLayout12.addWidget(self.historicalButton)

        self.literaryFictionButton = QCheckBox("Literary fiction")
        self.literaryFictionButton.setChecked(False)
        self.literaryFictionButton.setFont(QFont("Vesper Libre", 20))
        self.literaryFictionButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        self.scienceFictionButton = QCheckBox("Science fiction")
        self.scienceFictionButton.setChecked(False)
        self.scienceFictionButton.setFont(QFont("Vesper Libre", 20))
        self.scienceFictionButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        hLayout13 = QHBoxLayout()
        hLayout13.addSpacing(50)
        hLayout13.addWidget(self.literaryFictionButton)
        hLayout13.addSpacing(25)
        hLayout13.addWidget(self.scienceFictionButton)

        self.shortStoriesButton = QCheckBox("Short stories")
        self.shortStoriesButton.setChecked(False)
        self.shortStoriesButton.setFont(QFont("Vesper Libre", 20))
        self.shortStoriesButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        self.suspenseAndThrillersButton = QCheckBox("Suspense and Thrillers")
        self.suspenseAndThrillersButton.setChecked(False)
        self.suspenseAndThrillersButton.setFont(QFont("Vesper Libre", 20))
        self.suspenseAndThrillersButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        hLayout14 = QHBoxLayout()
        hLayout14.addSpacing(50)
        hLayout14.addWidget(self.shortStoriesButton)
        hLayout14.addSpacing(25)
        hLayout14.addWidget(self.suspenseAndThrillersButton)

        self.womenFictionButton = QCheckBox("Women's fiction")
        self.womenFictionButton.setChecked(False)
        self.womenFictionButton.setFont(QFont("Vesper Libre", 20))
        self.womenFictionButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        self.cookBookButton = QCheckBox("Cookbook")
        self.cookBookButton.setChecked(False)
        self.cookBookButton.setFont(QFont("Vesper Libre", 20))
        self.cookBookButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        hLayout15 = QHBoxLayout()
        hLayout15.addSpacing(50)
        hLayout15.addWidget(self.womenFictionButton)
        hLayout15.addSpacing(25)
        hLayout15.addWidget(self.cookBookButton)

        self.essayButton = QCheckBox("Essay")
        self.essayButton.setChecked(False)
        self.essayButton.setFont(QFont("Vesper Libre", 20))
        self.essayButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        self.memoirButton = QCheckBox("Memoir")
        self.memoirButton.setChecked(False)
        self.memoirButton.setFont(QFont("Vesper Libre", 20))
        self.memoirButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        hLayout16 = QHBoxLayout()
        hLayout16.addSpacing(50)
        hLayout16.addWidget(self.essayButton)
        hLayout16.addSpacing(25)
        hLayout16.addWidget(self.memoirButton)

        self.poetryButton = QCheckBox("Poetry")
        self.poetryButton.setChecked(False)
        self.poetryButton.setFont(QFont("Vesper Libre", 20))
        self.poetryButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        self.trueCrimeButton = QCheckBox("True crime")
        self.trueCrimeButton.setChecked(False)
        self.trueCrimeButton.setFont(QFont("Vesper Libre", 20))
        self.trueCrimeButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        hLayout17 = QHBoxLayout()
        hLayout17.addSpacing(50)
        hLayout17.addWidget(self.poetryButton)
        hLayout17.addSpacing(25)
        hLayout17.addWidget(self.trueCrimeButton)

        price = QLabel("Price")
        price.setFont(QFont("Vesper Libre", 25))
        price.setStyleSheet('''
        QLabel {
        color: rgb(132, 113, 77);
        }
        ''')
        
        self.priceCost = QLineEdit(self)
        self.priceCost.setPlaceholderText(self.price)
        









