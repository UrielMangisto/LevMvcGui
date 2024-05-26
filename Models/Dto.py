class MovieDto:

    def __init__(
        self,
        id: int,
        title: str,
        genre: str,
        posterURL: str,
        rating: float,
        year: int,
        imdbID: str,
        time: int,
        
        
    ):
        self.id = id
        self.title = title
        self.poster_url = posterURL
        self.rating = rating
        self.year = year
        self.imdbID = imdbID
        self.time = time
        self.genre = genre
