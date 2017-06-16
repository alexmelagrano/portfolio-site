# Helper file for retrieving Spotify API data

import sys
import requests
import spotipy
import spotipy.util as util

CLIENT_ID = '...'
CLIENT_SECRET = '...'
ACCESS_TOKEN = '...'

SCOPE = 'user-top-read'

# if len(sys.argv) > 1:
#     username = sys.argv[1]
# else:
#     print "Usage: %s username" % (sys.argv[0],)
#     sys.exit()
#
# token = util.prompt_for_user_token(username, scope)
#
# if token:
#     sp = spotipy.Spotify(auth=token)
#     results = sp.current_user_saved_tracks()
#     for item in results['items']:
#         track = item['track']
#         print track['name'] + ' - ' + track['artists'][0]['name']
# else:
#     print "Can't get token for", username


# Gets the most recent tweet, then uses Oembed to get the embedded HTML version
def getLatestTracks():
    sp = spotipy.Spotify(auth=ACCESS_TOKEN)

    tracks = sp.current_user_top_tracks(3, 0, 'short_term')

    print(tracks)
    # current_user_top_tracks(limit=20, offset=0, time_range='medium_term')

