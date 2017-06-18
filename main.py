from flask import Flask, render_template
import json

# from tracks import getLatestTracks


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


@app.route('/api/get-tracks/')
def getTracks():
    # latestTracks = getLatestTracks()

    latestTracks = json.dumps({'track1': '5wTVNpi5WDByxBgKgUE6MU',
                               'track2': '0Kz9aGVgFvndWkcaiylIt5',
                               'track3': '3oUSdLtRYOSvXcLMrHctv7'
                               })

    return app.response_class(latestTracks, content_type='application/json')


if __name__ == "__main__":
    app.debug = True
    app.run()
