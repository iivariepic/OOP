from Task6 import Movie

def movies_of_genre(movies:list[Movie], genre:str) -> list[Movie]:
    return [movie for movie in movies if genre.casefold() == movie.genre.casefold()]

def main() -> None:
    john_woo  = Movie(name="A Better Tomorrow", director="John Woo", genre="action", year=1986)
    kungfu = Movie(name="Chinese Odyssey", director="Stephen Chow", genre="comedy", year=1993)
    jet_li = Movie(name="The Legend", director="Corey Yuen", genre="comedy", year=1993)
    movies = [john_woo, kungfu, jet_li,
              Movie(name="Hero", director="Yimou Zhang", genre="action", year=2002)]

    print("Movies in the Action genre:")
    for movie in movies_of_genre(movies, "action"):
        print(f"{movie.director}:  {movie.name}")

if __name__ == '__main__':
    main()