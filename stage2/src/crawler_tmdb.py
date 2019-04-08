import requests
from bs4 import BeautifulSoup as BS


TMDB_MOVIE_LIST_URL = 'https://www.themoviedb.org/movie?page='
TMDB_BASE_URL = 'https://www.themoviedb.org'

total_number = 20 # TODO: change this to 4000
movies_per_page = 20


def get_movie_info(home_url):
    """
    Given a url for a page of a movie, return the movie info as a list
    """
    info = []
    homepage = requests.get(home_url)
    home_soup = BS(homepage.content, 'html.parser')
    # name
    name = home_soup.find('h2').get_text()
    info.append(name)
    # year
    # directors
    # writers
    # actors
    # runtime
    # budget
    # revenue
    # genre
    return info


def get_movies_in_page(movie_list_url):
    """
    Given a url for a page of the movie list in TMDb, returns the movie info
    on that page as a list
    """
    movies = []
    movie_list = requests.get(movie_list_url)
    soup = BS(movie_list.content, 'html.parser')
    for link in soup.find_all('a', class_='title result'):
        url = TMDB_BASE_URL + link.get('href')
        movies.append(get_movie_info(url))
    return movies


if __name__ == '__main__':
    movies = []
    for page_no in range(int(total_number / movies_per_page)):
        movies.extend(get_movies_in_page(TMDB_MOVIE_LIST_URL + str(page_no + 1)))