import sys

from PySide6.QtWidgets import QApplication

from View import MovieView
from controller import MovieController

from Model import MoviesModel

def main():
    app = QApplication(sys.argv)
   

    view = MovieView()
    controller = MovieController(view)

    controller.show()

    sys.exit(app.exec())
    #app = QApplication(sys.argv)
    #window = LibraryView()

if __name__ == "__main__":
    main()

