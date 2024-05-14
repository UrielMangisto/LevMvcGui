import sys
from PySide6.QtWidgets import QApplication
from typing import Optional
from PySide6.QtWidgets import (
    QListWidgetItem,
)

from View import MovieView
from ListView import MovieListView
from controller import MovieController
from Model import MoviesModel
from Dto import MovieDto

class MovieListController:
    def __init__(self, view: MovieListView,model : MoviesModel ) -> None:
        self.view = view
        self.model = model
        self.movies: Optional[list[MovieDto]] = []
        #self.create_random_data_for_debug()
        self.movies = self.model.get_movies()
        self.populate_movie_list()
        self.view.select_movie_button.clicked.connect(self.handle_select_movie)
        self.view.load_movies_button.clicked.connect(self.handle_load_movies)
        self.view.search_button.clicked.connect(self.handle_search_movie)
        self.view.add_movie_button.clicked.connect(self.handle_add_movie)
        self.view.remove_movie_button.clicked.connect(self.handle_remove_movie)

    def populate_movie_list(self) -> None:
        if self.movies is not None:  # Check if movies exist
            for movie in self.movies:
                item = QListWidgetItem(movie.title)
                self.view.movie_list_widget.addItem(item)
        else:
            # Handle the case where no movies are retrieved
            print("No movies found to populate the list.")


    def handle_select_movie(self) -> None:
        selected_movie_item = self.view.movie_list_widget.currentItem()
        movie_search = self.model.get_movies_search(selected_movie_item.text())
        if movie_search:
            selected_partof_movie = movie_search.pop(0)
            selected_movie= self.model.get_movie_imdbID(selected_partof_movie.imdbID)
            # Pass the selected movie to another view, e.g., MovieView
            movie_view = MovieView()  # Assuming MovieView is already defined
            movie_controller = MovieController(movie_view)  # Assuming MovieController is already defined
            movie_controller.movie = selected_movie
            # Here you might need to fetch movie details based on the selected movie and pass it to MovieController
            movie_controller.show()  # Show the MovieView
            app = QApplication(sys.argv)
            sys.exit(app.exec())

    
        
    def handle_load_movies(self) -> None:
        # Clear the movie list widget
        self.view.movie_list_widget.clear()

        # Fetch movies from the model
        movies = self.model.get_movies()
        if movies:
            # Populate the movie list widget with the fetched movies
            for movie in movies:
                item = QListWidgetItem(movie.title)
                self.view.movie_list_widget.addItem(item)
    def handle_search_movie(self) -> None:
        # Perform search based on user input
        search_term = self.view.search_input.text()
        # Clear the movie list widget
        self.view.movie_list_widget.clear()

        # Fetch movies based on the search term
        movies = self.model.get_movies_search(search_term)
        if movies:
            # Populate the movie list widget with the fetched movies
            for movie in movies:
                item = QListWidgetItem(movie.title)
                self.view.movie_list_widget.addItem(item)
    
    def handle_add_movie(self) -> None:
        selected_movie_item = self.view.movie_list_widget.currentItem()
        movie_search = self.model.get_movies_search(selected_movie_item.text())
        if self.searchMovieInList(selected_movie_item.text()):
             msgtxt = f"The movie {selected_movie_item.text()} is alredy in the list!"
             self.view.show_message(msgtxt)
             return
        if movie_search:
            selected_partof_movie = movie_search.pop(0)
            self.model.post_movie(selected_partof_movie.imdbID)
            msgtxt = f"The movie {selected_partof_movie.title} was added to the list successfully!"
            self.view.show_message(msgtxt)

    def handle_remove_movie(self) -> None:
        selected_movie_item = self.view.movie_list_widget.currentItem()
        selected_movie = self.searchMovieInList(selected_movie_item.text())
        if not self.searchMovieInList(selected_movie_item.text()):
             msgtxt = f"The movie {selected_movie_item.text()} is not in the list!"
             self.view.show_message(msgtxt)
        if selected_movie:
            is_deleted = self.model.delete_movie(selected_movie.id)
            if is_deleted:
                self.view.show_message("Movie Removed Successfully!")
                self.handle_load_movies()
            else:
                self.view.show_message("Movie Removing was Failed")

    def searchMovieInList(self,movieName):
        for movie in self.movies:
            if movie.title == movieName:
                return movie
        return None