'''
import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
'''
'''
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QPushButton, QVBoxLayout, QWidget, QLineEdit, QComboBox

class Movie:
    def __init__(self, title, year, genre, duration):
        self.title = title
        self.year = year
        self.genre = genre
        self.duration = duration

class MovieListApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Movie List")
        self.setGeometry(100, 100, 400, 300)

        self.movie_list = QListWidget()
        self.movie_list.addItems(["The Shawshank Redemption", "Inception", "The Dark Knight", "Pulp Fiction"])

        self.search_input = QLineEdit()
        self.search_button = QPushButton("Search")
        self.filter_button = QPushButton("Filter by Genre")

        self.genre_combobox = QComboBox()
        self.genre_combobox.addItems(["Action", "Comedy", "Drama", "Sci-Fi", "Thriller"])

        layout = QVBoxLayout()
        layout.addWidget(self.search_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.movie_list)
        layout.addWidget(self.filter_button)
        layout.addWidget(self.genre_combobox)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MovieListApp()
    window.show()
    sys.exit(app.exec_())
'''
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QPushButton, QVBoxLayout, QWidget, QLineEdit, QComboBox

class Movie:
    def __init__(self, title, year, genre, duration):
        self.title = title
        self.year = year
        self.genre = genre
        self.duration = duration

class MovieListApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Movie List")
        self.setGeometry(100, 100, 400, 300)

        self.movies = [
            Movie("The Shawshank Redemption", 1994, "Drama", 142),
            Movie("Inception", 2010, "Sci-Fi", 148),
            Movie("The Dark Knight", 2008, "Action", 152),
            Movie("Pulp Fiction", 1994, "Crime", 154)
        ]

        self.movie_list = QListWidget()
        for movie in self.movies:
            self.movie_list.addItem(movie.title)

        self.search_input = QLineEdit()
        self.search_button = QPushButton("Search")
        self.filter_button = QPushButton("Filter by Genre")

        self.genre_combobox = QComboBox()
        self.genre_combobox.addItems(["Action", "Comedy", "Drama", "Sci-Fi", "Thriller"])

        layout = QVBoxLayout()
        layout.addWidget(self.search_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.movie_list)
        layout.addWidget(self.filter_button)
        layout.addWidget(self.genre_combobox)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MovieListApp()
    window.show()
    sys.exit(app.exec_())
