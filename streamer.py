from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream 
import credentials
import pandas as pd
import numpy as np
import json 
from tweepy import API
from tweepy.models import Status

class Authenticator():
		def authenticate_and_get_API(self):
			auth = OAuthHandler(credentials.CONSUMER_KEY,credentials.CONSUMER_SECRET)
			auth.set_access_token(credentials.ACCESS_TOKEN,credentials.ACCESS_TOKEN_SECRET)
			return auth

class Listener(StreamListener):		

	count = 0
	limit = 5

	def on_data(self,raw_data):
		data = json.loads(raw_data)
		if("retweeted_status" not in data):
			status = Status.parse(self.api,data)
			self.on_status(status)
			if(Listener.count < Listener.limit):
				return True
			return False
	
	def on_status(self,status):
		if(status.in_reply_to_status_id is None 
		or status.in_reply_to_user_id is None
		or status.in_reply_to_screen_name is None):
			print(Listener.count,status.text)
			Listener.count+=1
			if(Listener.count < Listener.limit):
				return True
			return False
			
	def on_error(self, status_code):
		if status_code == 420:
			#In case you reach the rate limit
			return False
		print(status)
	
	def stream_tweets(self,hashtag):
		try:
			stream = Stream(auth=Authenticator().authenticate_and_get_API(),listener=stream_listener)
			stream.filter(languages=['en'],track=hashtag)		
		except KeyboardInterrupt:
			print("Got keyboard interrupt")
	
if __name__ == "__main__":
	
	stream_listener = Listener()
	hashtag = ["USA"]
	stream_listener.stream_tweets(hashtag)
