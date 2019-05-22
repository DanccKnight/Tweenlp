from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream 
import credentials
from tweepy import API
from tweepy import Cursor 

class Authenticator():
		def authenticate(self):
			auth = OAuthHandler(credentials.CONSUMER_KEY,credentials.CONSUMER_SECRET)
			auth.set_access_token(credentials.ACCESS_TOKEN,credentials.ACCESS_TOKEN_SECRET)
			return auth 

class TwitterClient():
	def __init__(self, user=None):
		self.auth = Authenticator().authenticate()
		self.twitter_client = API(self.auth)
		self.user = user

	def get_user_tweets(self, num_tweets, user_fetched_tweets):
		for tweet in Cursor(self.twitter_client.user_timeline, id=self.user).items(num_tweets):
			print(tweet)
			with open(user_fetched_tweets,'a') as file:
				file.write(str(tweet))

class Listener(StreamListener):
	def on_data(self,data):
		try:
			print(data)
			with open(self.fetched_tweets,'a') as file:
				file.write(data)
			return True
		except BaseException as e:
			print(str(e))
		return True 

	def on_error(self, status):
		if status == 420:
			#In case you reach the rate limit
			return False
		print(status)
	
	def __init__(self, fetched_tweets):
		self.fetched_tweets = fetched_tweets
	
class TStreamer():

	def __init__(self):
		self.twitter_authenticator = Authenticator()	
	
	def stream_tweets(self, fetched_tweets, hashtag):
		listener = Listener(fetched_tweets)
		
		stream = Stream(Authenticator().authenticate(),listener)
		stream.filter(languages=['en'], track=hashtag)

if __name__ == "__main__":
	
	hashtag = ["PewdiePie","Tati Westbrook","James Charles"]
	fetched_tweets = "tweets.json"
	user_fetched_tweets = "userfetchedtweets.json"	

# If you want to fetch tweets of a person only, comment the last two statements only.
# If you want to fetch tweets in general, comment the following two statements only.
# For the argument in TwitterUser(), enter the username of the person following @
	
	twitter_client = TwitterClient('realDonaldTrump')
	print(twitter_client.get_user_tweets(4,user_fetched_tweets))
				
#	twitter_Streamer = TStreamer()
#	twitter_Streamer.stream_tweets(fetched_tweets, hashtag)
