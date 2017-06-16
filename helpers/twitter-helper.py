# Helper file for retrieving Twitter API data

import twitter

CONSUMER_KEY = '2QUgq73SXST8pRqjl9s12woox'
CONSUMER_SECRET = '1zkngSxDXT0d5iFqSMEvaPqQYiWgMZ0loBpvCfr4QV6ILuU7jN'
ACCESS_TOKEN = '799290979740217344-cn5Fnb34wkYTqWLFgUlEHjdpHP4gwx0'
ACCESS_TOKEN_SECRET = 'CusyBnvNTm1Vl6BDtMXCnSIq7dDW2JMUjOR7j0v4KUpmL'

api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token_key=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

# Prints credentials - uncomment for debugging purposes if necessary
#print(api.VerifyCredentials())

def getLatestTweet():
  lastTweet = api.GetUserTimeline(user_id=799290979740217344, count=1, include_rts=False, exclude_replies=True)
  print(lastTweet)
  
getLatestTweet()