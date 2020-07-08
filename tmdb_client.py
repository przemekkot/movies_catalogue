import json
import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MTE4Y2NkODY1MWUyMDczOWZhYTRlMzU4Y2I2ZDIwZCIsInN1YiI6IjVmMDU2OGQwMjBhZjc3MDAzNWU3N2IzOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.VnK58vvU8DOSdgzhlxiHt-PfHTwIVpsXelEW4k47kgA"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

#print(get_popular_movies())

def get_poster_url(poster_api_path, size="w780"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

#print(get_poster_url("/db32LaOibwEliAmSL2jjDF6oDdj.jpg"))

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]
