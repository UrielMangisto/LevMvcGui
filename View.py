from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QGroupBox, QPushButton
from qt_material import apply_stylesheet

class MovieView(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Setting up the UI
        self.setWindowTitle("Movie Info")
        self.setGeometry(120, 50, 800, 600)

        # Applying Material Design stylesheet
        apply_stylesheet(self, theme='light_teal.xml')

        # Central widget and layout
        self.central_widget = QWidget(self)
        self.layout = QVBoxLayout(self.central_widget)

        # Putting in padding
        self.layout.setContentsMargins(20, 10, 20, 20)

        # Setting up the title label
        self.title_label = QLabel("Movie Title")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)
        
        # Font of the title label
        font = self.title_label.font()
        font.setPointSize(20)
        font.setBold(True)
        self.title_label.setFont(font)

        # Setting up the H layout
        self.h_layout = QHBoxLayout()

        # Setting up the group box for media details
        self.movie_details_group = QGroupBox("Movie Details")
        self.movie_details_layout = QVBoxLayout()
        self.movie_details_group.setLayout(self.movie_details_layout)

        # Setting the font size of the group box
        font = self.movie_details_group.font()
        font.setPointSize(15)
        self.movie_details_group.setFont(font)

        # Setting up the movie details
        self.movie_year = QLabel("Year: ")
        self.movie_details_layout.addWidget(self.movie_year)

        self.movie_rating = QLabel("rating: ")
        self.movie_details_layout.addWidget(self.movie_rating)

        self.movie_genre = QLabel("genre: ")
        self.movie_details_layout.addWidget(self.movie_genre)

        self.movie_time = QLabel("time: ")
        self.movie_details_layout.addWidget(self.movie_time)

        self.movie_imdb_id = QLabel("IMDB: ")
        self.movie_details_layout.addWidget(self.movie_imdb_id)

        
        

        self.h_layout.addWidget(self.movie_details_group)

        # Setting up the image of the movie
        self.movie_image = QLabel()
        # Setting the image
        self.movie_image.setFixedSize(400, 480)
        # Centering the image in the label
        self.h_layout.addWidget(self.movie_image)

        # Setting up the main widget
        self.central_widget.setLayout(self.layout)

        self.layout.addLayout(self.h_layout)

        # Button to trigger Imagga
        self.imagge_Ai = QPushButton("Generate imagge ai")
        self.layout.addWidget(self.imagge_Ai)

        # Setting up the tags and their corresponding percentages
        self.tags_and_percentages_layout = QVBoxLayout()  # Create a QVBoxLayout for tags and their percentages
        self.layout.addLayout(self.tags_and_percentages_layout)  # Add the new layout to the main layout

        self.tag1_layout = QHBoxLayout()  # Create an HBoxLayout for tag1 and its percentage
        self.tags_and_percentages_layout.addLayout(self.tag1_layout)  # Add the layout to the new QVBoxLayout

        self.tag1 = QLabel("Tag 1")
        self.tag1_layout.addWidget(self.tag1)

        self.percentage1 = QLabel("percentage 1")
        self.tag1_layout.addWidget(self.percentage1)

        self.tag2_layout = QHBoxLayout()  # Create an HBoxLayout for tag2 and its percentage
        self.tags_and_percentages_layout.addLayout(self.tag2_layout)  # Add the layout to the new QVBoxLayout

        self.tag2 = QLabel("Tag 2")
        self.tag2_layout.addWidget(self.tag2)

        self.percentage2 = QLabel("percentage 2")
        self.tag2_layout.addWidget(self.percentage2)

        self.tag3_layout = QHBoxLayout()  # Create an HBoxLayout for tag3 and its percentage
        self.tags_and_percentages_layout.addLayout(self.tag3_layout)  # Add the layout to the new QVBoxLayout

        self.tag3 = QLabel("Tag 3")
        self.tag3_layout.addWidget(self.tag3)

        self.percentage3 = QLabel("percentage 3")
        self.tag3_layout.addWidget(self.percentage3)

        # Center the text in the tags
        self.tag1.setAlignment(Qt.AlignCenter)
        self.tag2.setAlignment(Qt.AlignCenter)
        self.tag3.setAlignment(Qt.AlignCenter)
        self.percentage1.setAlignment(Qt.AlignCenter)
        self.percentage2.setAlignment(Qt.AlignCenter)
        self.percentage3.setAlignment(Qt.AlignCenter)

        # Make the text bigger & bolder
        font = self.tag1.font()
        font.setPointSize(18)
        self.tag1.setFont(font)
        self.tag2.setFont(font)
        self.tag3.setFont(font)

        # Hide the tags initially
        self.tag1.hide()
        self.tag2.hide()
        self.tag3.hide()

        self.setCentralWidget(self.central_widget)