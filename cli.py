from imdb import Cinemagoer
from imdb import Movie

url: str = "https://vidsrc.xyz/embed/"

def welcome():
    print("Welcome to MoviesSRC CLI service!")
    print("One of the biggest movies database provided by VidSRC, developed by Jaguar000212")
    print("This service is a CLI version of the MoviesSRC GUI service")
    print("You can search for movies and series and get the URL to watch them online")
    print("Let's get started!")
    selectType()

def selectType():
    print("Select the type of search you want to perform:")
    print("1. Search Movie")
    print("2. Search Series")
    print("3. Exit")
    choice: int = int(input("Enter your choice: "))
    if choice == 1:
        searchmovie()
    elif choice == 2:
        searchSeries()
    elif choice == 3:
        print("Exiting...")
        exit()
    else:
        print("Invalid choice!")
        selectType()

def searchmovie():
    cinemagoer: Cinemagoer = Cinemagoer()
    query: str = input("Enter the name of the movie: ")
    results: list[Movie] = cinemagoer.search_movie(query, 5)
    if len(results) == 0:
        print("No results found!")
        selectType()
    else:
        print("Results:")
        for i, result in enumerate(results):
            try:
                print(f"{i+1}. {result['title']} ({result['year']})")
            except KeyError:
                print(f"{i+1}. {result['title']}")
        choice: int = int(input("Enter the choice: "))
        if choice < 1 or choice > len(results):
            print("Invalid choice!")
            searchmovie()
        else:
            get_url(f"movie/tt{results[choice-1].getID()}")

def searchSeries():
    cinemagoer: Cinemagoer = Cinemagoer()
    query: str = input("Enter the name of the series: ")
    results: list[Movie] = cinemagoer.search_movie(query, 5)
    if len(results) == 0:
        print("No results found!")
        selectType()
    else:
        print("Results:")
        for i, result in enumerate(results):
            try:
                print(f"{i+1}. {result['title']} ({result['year']})")
            except KeyError:
                print(f"{i+1}. {result['title']}")
        choice: int = int(input("Enter the choice: "))
        if choice < 1 or choice > len(results):
            print("Invalid choice!")
            searchSeries()
        else:
            get_url(f"tv/tt{results[choice-1].getID()}")

def get_url(path: str):
    global url
    _url: str = f"{url}{path}"
    print(f"URL: {_url}")
    retry: str = input("Do you want to search again? (y/n): ")
    if retry == "y":
        selectType()
    else:
        print("Exiting...")
        exit()

if __name__ == "__main__":
    welcome()