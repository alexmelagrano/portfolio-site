from flask import Flask, render_template
from services.projects import get_projects
from services.tweets import get_latest_tweet


app = Flask(__name__)


def createApp():
    app = Flask(__name__)

    return app


# Routing
@app.route('/')
@app.route('/index/')
def index():
    projects = get_projects()

    return render_template("portfolio.html",
                           projects=projects)


@app.route('/photography/')
def photography():
    return '<h1 style="width: 100%; text-align: center; padding-top: 50px">Hey! Thanks for the interest in my ' \
           'work!</h1> </br> ' \
           '<h3 style="width: 100%; text-align: center">This page is a work in progress, so check back later.</h3>'


@app.route('/api/get-tweet/')
def get_tweet():
    post_info = get_latest_tweet()

    return post_info


if __name__ == "__main__":
    app.debug = True
    app.run()
