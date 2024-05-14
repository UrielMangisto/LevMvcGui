import requests
import json
from typing import Optional
from Dto import MovieDto
from config import  BASE_URL

class MoviesModel:
    """Model Class for the Movie Entity"""

    def __init__(self, BASE_URL: str = BASE_URL):
        self.BASE_URL = BASE_URL

    def get_movies(self) -> Optional[list[MovieDto]]:
        """
        GET - /api/Movie
        Returns:
            Optional[list[MovieDto]] - a list of all movies in the database in the Movie format
            None if response.status_code == 404
        """

        url = f"{self.BASE_URL}/Movie"
        # url = http://localhost:{self.PORT}/api/Movies/
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                json_str = response.text
                json_obj = json.loads(json_str)
                return [MovieDto(**obj) for obj in json_obj]
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        return None

    def get_movie_id(self, id: int) -> Optional[MovieDto]:
        """
        GET - /api/Movie/{id}
        Args:
            id: int - the id of the movie in the database
        Returns:
            Optional[Movie] - a movies in the database with the id=id in the Movie format
            None if response.status_code == 404
        """
        url = f"{self.BASE_URL}/Movie/{id}"
        # url = f"http://localhost:{self.PORT}/api/Movies/{id}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                json_str = response.text
                json_obj = json.loads(json_str)
                return MovieDto(**json_obj)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        return None

    def get_movie_imdbID(self, imdbID: str) -> Optional[MovieDto]:
        """
        GET - /api/Movie/search/{imdbID}
        Args:
            imdbID: str - the imdbID of the movie in the database
        Returns:
            Optional[Movie] - a movies in the database with the imdbID=imdbID in the Movie format
            None if response.status_code == 404
        """
        url = f"{self.BASE_URL}/Movie/search/{imdbID}"
        # url = f"http://localhost:{self.PORT}/api/Movies/search/{imdbID}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                json_str = response.text
                json_obj = json.loads(json_str)
                return MovieDto(**json_obj)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        return None

    def get_movies_search(
        self, s: str, y: Optional[int] = None
    ) -> Optional[list[MovieDto]]:
        """
        GET - /api/Movie/search/?s=s
        Args:
            s: str - search term
            y: int - year of the media
        Returns:
            Optional[list[MediaDto]] - a list of media in the Omdb API database in the Media format
            None if response.status_code == 404
        """
        # url = f"http://localhost:{self.PORT}/api/Movies/search/?s={s}"
        try:
            url = f"{self.BASE_URL}/Movie/search/?s={s}"
            if y:
                url += f"&y={y}"

            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                json_str = response.text
                json_obj = json.loads(json_str)
                return [MovieDto(**obj) for obj in json_obj]
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        return None

    def post_movie(self, imdbID: str) -> Optional[MovieDto]:
        """
        POST - /api/Movie/?imdbID=imdbID
        Args:
            imdbID : str - the imdbID of the movie in the database
        Returns:
            Optional[Movie] - a movie that was inserted in the database from the Omdb API
            None if response.status_code == 404
        """
        # url = f"http://localhost:{self.PORT}/api/Movies?imdbID={imdbID}"
        url = f"{self.BASE_URL}/Movie?imdbID={imdbID}"

        try:
            response = requests.post(url, timeout=5)
            if response.status_code in {200, 201}:
                json_str = response.text
                json_obj = json.loads(json_str)
                return MovieDto(**json_obj)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        return None
    
    def delete_movie(self, movie_id: int) -> bool:
        """
        DELETE - /api/Movie/{movie_id}
        Returns:
            bool - True if the object was deleting else False
        """
        url = f"{self.BASE_URL}/Movie/{movie_id}"

        try:
            response = requests.delete(url, timeout=5)
            return response.status_code == 204
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        return False