from flask import Flask, render_template
from tracks import getLatestTracks


app = Flask(__name__)


# Routing
@app.route('/')
@app.route('/index/')
def index():
    return render_template("portfolio.html")


@app.route('/photography/')
def photography():
    return '<h1 style="width: 100%; text-align: center; padding-top: 50px">Hey! Thanks for the interest in my ' \
           'work!</h1> </br> ' \
           '<h3 style="width: 100%; text-align: center">This page is a work in progress, so check back later.</h3>'


@app.route('/get-tracks/')
def getTracks():
    latestTracks = getLatestTracks()

    return latestTracks

if __name__ == "__main__":
    app.debug = True
    app.run()
