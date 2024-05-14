from PySide6.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, QListWidget, QPushButton,
    QLineEdit, QHBoxLayout, QStatusBar, QTabWidget, QTabBar
)

from qt_material import apply_stylesheet

class MovieListView(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Setting up the UI
        self.setWindowTitle("Movie List")
        self.setGeometry(120, 50, 800, 600)

        # Applying Material Design stylesheet
        apply_stylesheet(self, theme='dark_teal.xml')

        # Central widget and layout
        self.central_widget = QWidget(self)
        self.layout = QVBoxLayout(self.central_widget)

        # Search section
        self.search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_button = QPushButton("Search")
        self.search_layout.addWidget(self.search_input)
        self.search_layout.addWidget(self.search_button)
        self.layout.addLayout(self.search_layout)

        # List widget to display movies
        self.movie_list_widget = QListWidget()
        self.layout.addWidget(self.movie_list_widget)

        # Buttons
        self.select_movie_button = QPushButton("Select Movie")
        self.add_movie_button = QPushButton("Add To List")
        self.remove_movie_button = QPushButton("Remove Movie")
        self.load_movies_button = QPushButton("Load Movies")

        self.layout.addWidget(self.select_movie_button)
        self.layout.addWidget(self.add_movie_button)
        self.layout.addWidget(self.remove_movie_button)
        self.layout.addWidget(self.load_movies_button)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # Set central widget
        self.setCentralWidget(self.central_widget)

    def show_message(self, message: str, duration: int = 3000) -> None:
           """
           Display a temporary message in the status bar.
           Args:
               message: str - The message to display.
               duration: int - Duration of the message in milliseconds (default: 3000ms).
           """
           self.status_bar.showMessage(message, duration)