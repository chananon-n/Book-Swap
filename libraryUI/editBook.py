from PySide6.QtGui import QPixmap, QFont, QDragEnterEvent

import sys

from PySide6.QtGui import QPixmap, QFont

from PySide6.QtWidgets import QMainWindow, QLabel, QHBoxLayout, QWidget, QLineEdit, QTextEdit, QCheckBox, QPushButton, \
    QDialog, QVBoxLayout, QScrollArea, QApplication
from PySide6.QtCore import *


from libraryUI.Sign_in import Sign_in


class EditEbook(QMainWindow):
    def __init__(self, e):
        super().__init__()
        self.ebook = e
        self.URL = "Test.pdf"
        self.pixmap = None
        self.price = 0
        self.type = "ebook"
        self.title = "title"
        self.author = "author"
        self.description = "description"
        self.category = ["Romance"]
        self.image = QLabel()
        # replace path of your image at placeholder.png
        self.placeholder_image = QPixmap("placeholder.png")

        self.image.setPixmap(self.placeholder_image)
        self.image.setScaledContents(True)
        self.image.setMinimumSize(250, 250)
        self.image.setAlignment(Qt.AlignCenter)
        self.image.setStyleSheet("border: 2px dashed gray; color: gray;")
        self.image.setText("Please drag and drop a book image here")

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

        self.fantasyAndScienceFictionButton = QCheckBox("Fantasy and science fiction")
        self.fantasyAndScienceFictionButton.setChecked(False)
        self.fantasyAndScienceFictionButton.setFont(QFont("Vesper Libre", 20))
        self.fantasyAndScienceFictionButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        self.thrillersAndHorrorButton = QCheckBox("Thrillers and horror")
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

        self.youngAndAdultButton = QCheckBox("Young adult")
        self.youngAndAdultButton.setChecked(False)
        self.youngAndAdultButton.setFont(QFont("Vesper Libre", 20))
        self.youngAndAdultButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        self.childrenFictionButton = QCheckBox("Children’s fiction")
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

        self.inspirationalAndReligiousButton = QCheckBox("Inspirational and religious")
        self.inspirationalAndReligiousButton.setChecked(False)
        self.inspirationalAndReligiousButton.setFont(QFont("Vesper Libre", 20))
        self.inspirationalAndReligiousButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        self.biographyAndAutobiographyButton = QCheckBox("Biography and autobiography")
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

        self.classicButton = QCheckBox("Classics")
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

        self.shortStoriesButton = QCheckBox("Short Stories")
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

        self.womenFictionButton = QCheckBox("Women's Fiction")
        self.womenFictionButton.setChecked(False)
        self.womenFictionButton.setFont(QFont("Vesper Libre", 20))
        self.womenFictionButton.setStyleSheet('''
        QCheckBox {
        color: rgb(132, 113, 77);
        }
        ''')

        self.cookBookButton = QCheckBox("Cookbooks")
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

        self.essayButton = QCheckBox("Essays")
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

        self.trueCrimeButton = QCheckBox("True Crime")
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
        self.priceCost.setPlaceholderText(str(self.price))
        self.priceCost.setFont(QFont("Vesper Libre", 20))
        self.priceCost.setStyleSheet('''
        QLineEdit {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(132, 113, 77);
        }
        ''')

        hLayout18 = QHBoxLayout()
        hLayout18.addSpacing(160)
        hLayout18.addWidget(price)
        hLayout18.addSpacing(25)
        hLayout18.addWidget(self.priceCost)
        hLayout18.addSpacing(160)

        url = QLabel("URL")
        url.setFont(QFont("Vesper Libre", 25))
        url.setStyleSheet('''
        QLabel {
        color: rgb(132, 113, 77);
        }
        ''')

        self.urlTextEdit = QTextEdit(self)
        self.urlTextEdit.setPlaceholderText(self.URL)
        self.urlTextEdit.setFont(QFont("Vesper Libre", 20))
        self.urlTextEdit.setStyleSheet('''
        QTextEdit {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(132, 113, 77);
        }
        ''')

        hLayout19 = QHBoxLayout()
        hLayout19.addSpacing(20)
        hLayout19.addWidget(url)

        hLayout20 = QHBoxLayout()
        hLayout20.addSpacing(20)
        hLayout20.addWidget(self.urlTextEdit)
        hLayout20.addSpacing(20)

        self.submitButton = QPushButton("Submit")
        self.submitButton.setFont(QFont("Vesper Libre", 20))
        self.submitButton.setStyleSheet('''
        QPushButton {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(132, 113, 77);
        }
        ''')

        self.submitButton.clicked.connect(self.submit)

        self.cancelButton = QPushButton("Remove")
        self.cancelButton.setFont(QFont("Vesper Libre", 20))
        self.cancelButton.setStyleSheet('''
        QPushButton {
        border: 3px solid rgb(132, 113, 77);
        color: rgb(132, 113, 77);
        }
        ''')

        hLayout21 = QHBoxLayout()
        hLayout21.addSpacing(20)
        hLayout21.addWidget(self.cancelButton)
        hLayout21.addSpacing(300)
        hLayout21.addWidget(self.submitButton)
        hLayout21.addSpacing(20)

        vLayout = QVBoxLayout()
        vLayout.addLayout(hLayout1)
        vLayout.addLayout(hLayout2)
        vLayout.addLayout(hLayout3)
        vLayout.addLayout(hLayout4)
        vLayout.addLayout(hLayout5)
        vLayout.addLayout(hLayout6)
        vLayout.addLayout(hLayout7)
        vLayout.addLayout(hLayout8)
        vLayout.addLayout(hLayout9)
        vLayout.addLayout(hLayout10)
        vLayout.addLayout(hLayout11)
        vLayout.addLayout(hLayout12)
        vLayout.addLayout(hLayout13)
        vLayout.addLayout(hLayout14)
        vLayout.addLayout(hLayout15)
        vLayout.addLayout(hLayout16)
        vLayout.addLayout(hLayout17)
        vLayout.addLayout(hLayout18)
        vLayout.addLayout(hLayout19)
        vLayout.addLayout(hLayout20)
        vLayout.addLayout(hLayout21)
        self.setLayout(vLayout)
        self.cancelButton.clicked.connect(self.remove)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_widget = QWidget()
        scroll_widget.setLayout(vLayout)

        scroll_area.setWidget(scroll_widget)

        self.setCentralWidget(scroll_area)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setWindowTitle("Edit Book")
        self.setFixedSize(700, 600)
        self.setStyleSheet("background-color: #F9F6EC;")
        self.check_category()
        self.show()

    # Connect to Home Page not yet.
    def remove(self):
        from librarySystem import librarySystem
        #remove ebook from ebook list
        librarySystem.ebook_list.remove(self.ebook)
        self.close()

    def check_category(self):
        oldGenre = [self.romanceButton, self.mysteryButton, self.fantasyAndScienceFictionButton,
                    self.thrillersAndHorrorButton, self.youngAndAdultButton, self.childrenFictionButton,
                    self.inspirationalAndReligiousButton, self.biographyAndAutobiographyButton,
                    self.actionAndAdventureButton, self.classicButton, self.comicButton,
                    self.historicalButton, self.literaryFictionButton, self.scienceFictionButton,
                    self.shortStoriesButton, self.suspenseAndThrillersButton, self.womenFictionButton,
                    self.cookBookButton, self.essayButton, self.memoirButton, self.poetryButton,
                    self.trueCrimeButton]
        for i in range(0, len(self.category)):
            if self.category[i] == oldGenre[i].text():
                oldGenre[i].setChecked(True)

    def save_category(self):
        newGenre = [self.romanceButton, self.mysteryButton, self.fantasyAndScienceFictionButton,
                    self.thrillersAndHorrorButton, self.youngAndAdultButton, self.childrenFictionButton,
                    self.inspirationalAndReligiousButton, self.biographyAndAutobiographyButton,
                    self.actionAndAdventureButton, self.classicButton, self.comicButton,
                    self.historicalButton, self.literaryFictionButton, self.scienceFictionButton,
                    self.shortStoriesButton, self.suspenseAndThrillersButton, self.womenFictionButton,
                    self.cookBookButton, self.essayButton, self.memoirButton, self.poetryButton,
                    self.trueCrimeButton]
        self.category = []
        for i in range(len(newGenre)):
            if newGenre[i].isChecked():
                self.category.append(newGenre[i].text())
            else:
                self.category.append("None")

    def submit(self):
        # Save the dropped image to the project's images folder and create the folder if it doesn't exist
        title_name = self.title
        self.pixmap = self.image.pixmap()
        from librarySystem import librarySystem
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
            # Go back to home page
            self.save_category()
            pass

    def getCategory(self):
        return self.category

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls() and event.mimeData().urls()[0].toString().endswith(".png"):
            event.acceptProposedAction()

    def dropEvent(self, event):
        url = event.mimeData().urls()[0]
        file_path = url.toLocalFile()
        if file_path.endswith('.png'):
            self.pixmap = QPixmap(file_path)
            self.image.setPixmap(self.pixmap)
            self.image.setScaledContents(True)
            self.image.setStyleSheet("border: #F9F6EC;")

    # I don't understand about save URL or save and go next page


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = EditEbook()
    app.exec()
