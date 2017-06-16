# Helper file for retrieving Twitter API data

import twitter
import requests

CONSUMER_KEY = '2QUgq73SXST8pRqjl9s12woox'
CONSUMER_SECRET = '1zkngSxDXT0d5iFqSMEvaPqQYiWgMZ0loBpvCfr4QV6ILuU7jN'
ACCESS_TOKEN = '799290979740217344-cn5Fnb34wkYTqWLFgUlEHjdpHP4gwx0'
ACCESS_TOKEN_SECRET = 'CusyBnvNTm1Vl6BDtMXCnSIq7dDW2JMUjOR7j0v4KUpmL'

api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token_key=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

# Prints credentials - uncomment for debugging purposes if necessary
print(api.VerifyCredentials())


# Gets the most recent tweet, then uses Oembed to get the embedded HTML version
def getLatestTweet():
  lastTweet = api.GetUserTimeline(user_id=799290979740217344, count=1, include_rts=False, exclude_replies=True)
  postID = lastTweet[0].id
  print(lastTweet)

  tweetUrl = 'https://twitter.com/alex_the_melon/status/' + str(postID)
  print(tweetUrl)

  data = api.GetStatusOembed(
                  status_id=None,
                  url=tweetUrl,
                  maxwidth=500,
                  hide_media=True,
                  hide_thread=True,
                  omit_script=False,
                  align=None,
                  related=None,
                  lang=None)


  print(data)

  # tweetInfo = data[7]
  # print(tweetInfo)

  return data


  
# https://dev.twitter.com/rest/reference/get/statuses/oembed
# https://docs.python.org/3/tutorial/modules.html

# getLatestTweet()
