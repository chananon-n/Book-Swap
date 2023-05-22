from PySide6.QtWidgets import (QApplication, QWidget)
from libraryUI.Sign_in import Sign_in  # change to main menu by your self na non , left only import sign in and from and import


class Remove_book(QWidget):

    def getSign_inPanel(self):  # wait for main menu done then just import main menu page na
        self.sign_in = Sign_in()
        self.close()


if __name__ == "__main__":
    app = QApplication()
    ui = Remove_book()
    app.exec()

# all the connected checkbox used last function isChecked() and get their result at last na I print sentence for u to identify easier
