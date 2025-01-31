class Movie:
    def __init__(self, name, director,genre, year):
        self.name = name
        self.director = director
        self.genre = genre
        self.year = year

def main() -> None:
    EEAAO = Movie("Everything Everywhere All at Once", "Daniel Kwan",
          "Surreal Drama", 2022)
    FBDO = Movie("Ferris Bueller's Day Off", "John Hughes",
                 "Comedy", 1986)

    print(f"{EEAAO.director}: {EEAAO.name}, {EEAAO.year}")
    print(f"The Genre of the movie {FBDO.name} is {FBDO.genre}")

if __name__ == "__main__":
    main()