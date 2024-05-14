from PySide6.QtWidgets import QApplication
from Model import MoviesModel
import sys

from ListView import MovieListView
from ListController import MovieListController

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create and show the movie list view
    movie_list_view = MovieListView()
    model = MoviesModel()
    movie_list_controller = MovieListController(movie_list_view,model=model)
    movie_list_view.show()

    sys.exit(app.exec())
