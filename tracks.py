# Adds tracks to a playlist

import pprint
import sys

import spotipy
import spotipy.util as util
import simplejson as json



def getLatestTracks():
    scope = 'user-top-read'
    token = util.prompt_for_user_token('alex3232', scope)

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        results = sp.current_user_top_tracks(time_range='short_term', limit=3)
        for i, item in enumerate(results['items']):
            print
            i, item['name'], '//', item['artists'][0]['name']
        print
        return results

    else:
        print("Can't get token for", 'alex3232')
