from imdb import Cinemagoer, Movie
from os import system, name
from requests import get, Response, exceptions

url: str = "https://vidsrc.xyz/embed/"

def clearScreen() -> None:
    if name == "nt":
        system("cls")
    else:
        system("clear")

def ifConnected() -> bool:
    try:
        get("https://www.google.com/")
        return True
    except exceptions.ConnectionError:
        return False

def get_url(path: str) -> str:
    global url
    _url: str = f"{url}{path}"
    return _url

def checkURL(vid_url: str) -> bool:
    req: Response = get(vid_url)
    if req.status_code == 404:
        return False
    return True

def getResults(query: str) -> list[Movie]:
    if ifConnected():
        cinemagoer: Cinemagoer = Cinemagoer()
        return cinemagoer.search_movie(query, 5)
    else:
        print("No internet connection. Exiting...")
        exit(-2)

def printResults(results: list[Movie]) -> None:
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

def welcome() -> None:
    clearScreen()
    print("Welcome to MoviesSRC CLI service!")
    print("One of the biggest movies database provided by VidSRC, developed by Jaguar000212")
    print("This service is a CLI version of the MoviesSRC GUI service")
    print("You can search for movies and series and get the URL to watch them online")
    print("Let's get started!")
    selectType()

def selectType() -> None:
    print("Select the type of search you want to perform:")
    print("1. Search Movie")
    print("2. Search Series")
    print("3. Exit")
    choice: int = None
    try:
        choice: int = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice!")
        selectType()
    if choice == 1:
        searchMovie()
    elif choice == 2:
        searchSeries()
    elif choice == 3:
        print("Exiting...")
        exit(0)
    else:
        print("Invalid choice!")
        selectType()

def searchMovie() -> None:
    query: str = input("Enter the name of the movie: ")
    results: list[Movie] = getResults(query)
    printResults(results)
    choice: int = None
    while choice is None:
        try:
            choice: int = int(input("Enter the choice: "))
            if choice < 1 or choice > len(results):
                print("Invalid choice!")
                choice = None
        except ValueError:
            print("Invalid choice!")
    get_url(f"movie/tt{results[choice-1].getID()}")

def searchSeries() -> None:
    query: str = input("Enter the name of the series: ")
    results: list[Movie] = getResults(query)
    printResults(results)
    choice: int = None
    while choice is None:
        try:
            choice: int = int(input("Enter the choice: "))
            if choice < 1 or choice > len(results):
                print("Invalid choice!")
                choice = None
        except ValueError:
            print("Invalid choice!")
    get_url(f"tv/tt{results[choice - 1].getID()}")

def finalize(vid_url) -> None:
    if checkURL(vid_url):
        print(f"URL: {vid_url}")
    else:
        print("Movie is not available at the moment. May get updated in future, thank you.")
    retry: str = input("Do you want to search again? (y/n): ")
    if retry == "y":
        clearScreen()
        selectType()
    else:
        print("Exiting...")
        exit()

if __name__ == "__main__":
    welcome()