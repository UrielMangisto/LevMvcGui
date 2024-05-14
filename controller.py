from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


from View import MovieView
from ImageModel import ImageModel


from PySide6.QtCore import QObject

class MovieController(QObject):
    def __init__(self, view : MovieView):
        super().__init__()
        self.view = view
        self.movie = None
        self.view.imagge_Ai.clicked.connect(self.handle_ai_tags)
        self.show()

    def show(self):
        self.view.tag1.hide()
        self.view.tag2.hide()
        self.view.tag3.hide()
        self.view.percentage1.hide()
        self.view.percentage2.hide()
        self.view.percentage3.hide()


        self.set_movie()
        
        self.view.show()

    def handle_movie_selected(self):
        # Assuming you have a method to get movie details by title
        self.set_movie()


    def set_movie(self) -> None:
        if not self.movie:
            return
    
        self.view.title_label.setText(f"{self.movie.title}")
       
        self.view.movie_year.setText(f"Year:\t{self.movie.year}")
        self.view.movie_rating.setText(f"rating:\t{self.movie.rating}")
        self.view.movie_imdb_id.setText(f"Imdb ID:\t{self.movie.imdbID}")
        self.view.movie_genre.setText(f"genre:\t{self.movie.genre}")
        self.view.movie_time.setText(f"time:\t{self.movie.time}")
        self.set_image()

    def set_image(self) -> None:
        if not self.movie:
            return

        self.image: bytes = ImageModel().get_image(self.movie.poster_url)
        pixmap = QPixmap()
        pixmap.loadFromData(self.image)
        pixmap = pixmap.scaled(
            self.view.movie_image.width(),
            self.view.movie_image.height(),
            Qt.KeepAspectRatio,
            Qt.FastTransformation,
        )
        self.view.movie_image.setAlignment(Qt.AlignCenter)
        self.view.movie_image.setPixmap(pixmap)


    def handle_ai_tags(self) -> None:
        image_model = ImageModel()
        image_tags, percentages = image_model.post_image(self.image)
        # Display the first three tags and their corresponding percentages
        for i in range(3):
            tag_label = getattr(self.view, f"tag{i + 1}")
            percentage_label = getattr(self.view, f"percentage{i + 1}")

            if i < len(image_tags):
                tag_label.setText(image_tags[i])
                percentage_label.setText(f"{percentages[i]:.2f}%")  # Displaying percentages with two decimal points
                tag_label.show()
                percentage_label.show()
            else:
                # If there are less than three tags, hide the remaining labels
                tag_label.hide()
                percentage_label.hide()


