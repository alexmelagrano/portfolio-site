# Helper file for retrieving Twitter API data

import twitter

CONSUMER_KEY = '...'
CONSUMER_SECRET = '...'
ACCESS_TOKEN = '...'
ACCESS_TOKEN_SECRET = '...'

api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)


# Prints credentials - uncomment for debugging purposes if necessary
# print(api.VerifyCredentials())

def getLatestTweet():
    lastTweet = api.GetUserTimeline(user_id=799290979740217344, count=1, include_rts=False, exclude_replies=True)
    print(lastTweet)


getLatestTweet()