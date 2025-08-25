class Movie:
    def __init__(self, id: int, title: str, overview: str, genres: list, keywords: list, cast: list, crew: list):
        self.id = id
        self.title = title
        self.overview = overview
        self.genres = genres
        self.keywords = keywords
        self.cast = cast
        self.crew = crew

    def __repr__(self):
        return f"Movie(id={self.id}, title='{self.title}', overview='{self.overview}', genres={self.genres}, keywords={self.keywords}, cast={self.cast}, crew={self.crew})"