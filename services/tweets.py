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


# Gets the most recent tweet, then uses Oembed to get the embedded HTML version
def get_latest_tweet():
    last_tweet = api.GetUserTimeline(user_id=799290979740217344, count=1, include_rts=False, exclude_replies=True)
    post_id = last_tweet[0].id

    tweet_url = 'https://twitter.com/alex_the_melon/status/' + str(post_id)

    data = api.GetStatusOembed(
        status_id=None,
        url=tweet_url,
        maxwidth=500,
        hide_media=True,
        hide_thread=True,
        omit_script=False,
        align=None,
        related=None,
        lang=None)

    return data['html']
