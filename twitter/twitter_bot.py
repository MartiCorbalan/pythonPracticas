import time

import tweepy

auth = tweepy.OAuthHandler('API key que te da ztmbot', 'secret key que te da ztmbot ')
auth.set_access_token('access_token', ' ')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
user = api.me()

def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)
#generte bot
#for follower in limit_handle(tweepy.Cursor(api.followers).items()):
 #   if follower.name == 'nombre del seguidor':
  #     follower.follow()
   #    break

#buscar los tweets que les dis like con la palabra python en este caso
search_string = 'python'
numberOfTweets = 5

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favourite()
        print('i liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break