from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream 
import credentials
import pandas as pd
import numpy as np
import json 
from tweepy import API
from tweepy.models import Status
from textblob import TextBlob
import re

class Authenticator():
		def authenticate_and_get_API(self):
			auth = OAuthHandler(credentials.CONSUMER_KEY,credentials.CONSUMER_SECRET)
			auth.set_access_token(credentials.ACCESS_TOKEN,credentials.ACCESS_TOKEN_SECRET)
			return auth

class Listener(StreamListener):		

	count = 0
	limit = 7
	lst = []
	
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
		or status.in_reply_to_status_id_str is None
		or status.in_reply_to_user_id is None
		or status.in_reply_to_user_id_str is None 
		or status.in_reply_to_screen_name is None):
			#print(Listener.count,status.text)
			Listener.lst.append(status.text)
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
	
class Analyzer():
	def tweet_to_dataframe(self,tweets):
		df = pd.DataFrame()
		df['Tweets'] = [tweets[i] for i in range(len(tweets))]
		return df

	def clean_tweet_text(self,tweet):
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

	def get_sentiment(self,tweet):
		analysis = TextBlob(self.clean_tweet_text(tweet))
		#print(analysis)
		return analysis.sentiment.polarity		

if __name__ == "__main__":
	
	tweet_analyzer = Analyzer()
	stream_listener = Listener()
	track = ["Elections"]
	stream_listener.stream_tweets(track)
	df = tweet_analyzer.tweet_to_dataframe(Listener.lst)
	df['sentiment'] = np.array([tweet_analyzer.get_sentiment(tweet) for tweet in df['Tweets']])
	print(df)	
	print("\nAverage sentiment score from received tweets:",np.mean(df['sentiment']))
