from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = []
    for x in range(8):
        movies.append(x)
    return render_template("homepage.html", movies=movies)

