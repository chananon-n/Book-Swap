import sys
from PySide6.QtWidgets import QApplication
from libraryUI.Home import Home
from libraryUI.Sign_in import Sign_in
import libraryUI.Sign_up


class librarySystem:
    # singleton
    __instance = None

    # constructor
    def __init__(self):
        # check if LibrarySystem is already created
        if librarySystem.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            librarySystem.__instance = self
            self.__current = Home()
            # Connect to the buttonClicked signal from the Home panel
            self.__current.buttonClicked.connect(self.handleButtonClicked)

    def handleButtonClicked(self, button_name):
        if button_name == "Sign_in":
            # Navigate to the Sign_in panel
            self.__current.close()
            sign_in = Sign_in()
            sign_in.signedIn.connect(self.backToHome)  # Connect to the signedIn signal
            self.__current = sign_in
        elif button_name == "Sign_up":
            # Navigate to the Sign_up panel
            self.__current.close()
            sign_up = libraryUI.Sign_up.Sign_up()
            sign_up.signedUp.connect(self.backToHome)  # Connect to the signedUp signal
            self.__current = sign_up

    @staticmethod
    def get_instance():
        if librarySystem.__instance is None:
            librarySystem()
        return librarySystem.__instance

    @staticmethod
    def checkSignUp(store_name):
        if store_name == "":
            return False
        else:
            return True

    @staticmethod
    def get_id():
        return "12345678"

    def backToHome(self):
        self.__current.close()
        self.__current = Home()
        self.__current.buttonClicked.connect(self.handleButtonClicked)  # Reconnect the signal
        self.__current.show()


if __name__ == "__main__":
    app = QApplication([])
    library_system = librarySystem.get_instance()
    sys.exit(app.exec())
