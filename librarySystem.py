import os
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QObject
from libraryUI.Home import Home
from libraryUI.Sign_in import Sign_in
from libraryUI.Sign_up import Sign_up


class librarySystem(QObject):
    # singleton
    __instance = None

    # constructor
    def __init__(self):
        # check if LibrarySystem is already created
        if librarySystem.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            librarySystem.__instance = self
            self.__current = None

    def start(self):
        self.__current = Home()
        # Connect to the buttonClicked signal from the Home panel
        self.__current.buttonClicked.connect(self.handleButtonClicked)

    def handleButtonClicked(self, button_name):
        if button_name == "Sign_in":
            # Navigate to the Sign_in panel
            self.__current.close()
            sign_in = Sign_in()
            sign_in.signedIn.connect(self.backToHome)  # Main Menu
            self.__current = sign_in
        elif button_name == "Sign_up":
            # Navigate to the Sign_up panel
            self.__current.close()
            sign_up = Sign_up()
            sign_up.signedUp.connect(self.backToHome)  # Connect to the signedIn signal
            self.__current = Sign_up()

    def backToHome(self):
        self.__current.close()
        self.__current = Home()

    @staticmethod
    def get_instance():
        if librarySystem.__instance is None:
            librarySystem()
        return librarySystem.__instance


    @staticmethod
    def get_id():
        return "kkkkk"

    @staticmethod
    def save_images(pixmap, title_name):
        # set image directory BookSwap resources/images
        image_dir = os.path.join(os.path.dirname(__file__), 'resources', 'images')
        if not os.path.exists(image_dir):
            os.mkdir(image_dir)
        if title_name is not None:
            image_path = os.path.join(image_dir, title_name + '.jpg')
            pixmap.save(image_path, 'jpg')
            return True
        else:
            return False


if __name__ == "__main__":
    app = QApplication([])
    library_system = librarySystem.get_instance()
    library_system.start()
    sys.exit(app.exec())
