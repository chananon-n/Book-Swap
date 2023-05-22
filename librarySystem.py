import sys

from PySide6.QtWidgets import QApplication

from libraryUI.Home import Home
from libraryUI.Sign_in import Sign_in
from libraryUI.Sign_up import Sign_up


class librarySystem:
    # singleton
    __instance = None

    # constructor
    def __init__(self):
        # check if librarySystem is already created
        if librarySystem.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            librarySystem.__instance = self
            self.__current = Home()


# main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    librarySystem()
    sys.exit(app.exec())
