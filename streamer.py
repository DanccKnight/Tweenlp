from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream 
import credentials

class Listener(StreamListener):
	def on_data(self,data):
		try:
			print(data)
			with open(self.fetched_tweets,'a') as tf:
				tf.write(data)
			return True
		except BaseException as e:
			print(str(e))
		return True 

	def on_error(self, status):
		print(status)
		return False 
	
	def __init__(self, fetched_tweets):
		self.fetched_tweets = fetched_tweets
	
class TStreamer():
	
	def stream_tweets(self, fetched_tweets, hashtag):
		listener = Listener(fetched_tweets)
		auth = OAuthHandler(credentials.CONSUMER_KEY,credentials.CONSUMER_SECRET)
		auth.set_access_token(credentials.ACCESS_TOKEN,credentials.ACCESS_TOKEN_SECRET)
		
		stream = Stream(auth,listener)
		stream.filter(track=hashtag)

if __name__ == "__main__":
	
	hashtag = ["Pewdiepie"]
	fetched_tweets = "tweets.json"
	twitter_Streamer = TStreamer()
	twitter_Streamer.stream_tweets(fetched_tweets, hashtag)
