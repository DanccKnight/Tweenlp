from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream 
import credentials
import pandas as pd
import numpy as np
import json 
from tweepy import API

class Authenticator():
		def authenticate(self):
			auth = OAuthHandler(credentials.CONSUMER_KEY,credentials.CONSUMER_SECRET)
			auth.set_access_token(credentials.ACCESS_TOKEN,credentials.ACCESS_TOKEN_SECRET)
			return auth 

class Listener(StreamListener):

	def on_data(self,data):
		try:
			#print(data)
			with open(self.fetched_tweets,'a') as file:
				file.write(data)
			return True
		except BaseException as e:
			print(str(e))
		return True 

	def on_error(self, status_code):
		if status_code == 420:
			#In case you reach the rate limit
			return False
		print(status)
	
	def __init__(self, fetched_tweets):
		self.fetched_tweets = fetched_tweets
	
class TStreamer():
	
	def stream_tweets(self, fetched_tweets, hashtag):
		listener = Listener(fetched_tweets)		
		stream = Stream(Authenticator().authenticate(),listener)
		stream.filter(languages=['en'], track=hashtag)

if __name__ == "__main__":

	twitter_Streamer = TStreamer()
	hashtag = ["Modi"]
	fetched_tweets = "tweets.txt"
	tweets = twitter_Streamer.stream_tweets(fetched_tweets, hashtag)
