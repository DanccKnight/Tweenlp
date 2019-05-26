import credentials
from tweepy import Cursor
from tweepy import API 
from tweepy import OAuthHandler
import numpy as np
import pandas as pd
from textblob import TextBlob
import re

class Authenticator():
	def authenticate(self):
		auth = OAuthHandler(credentials.CONSUMER_KEY,credentials.CONSUMER_SECRET)
		auth.set_access_token(credentials.ACCESS_TOKEN,credentials.ACCESS_TOKEN_SECRET)
		return auth 

class TwitterClient():
	def __init__(self, user=None):
		self.auth = Authenticator().authenticate()
		self.twitter_client = API(self.auth)

	def get_twitter_client_api(self):
		return self.twitter_client
	
class Analyzer():
	def tweet_to_dataframe(self,tweets):
		df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
		df['date'] = np.array([tweet.created_at for tweet in tweets])
		df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
		df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
		return df
	
	def clean_tweet_text(self,tweet):
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

	def get_sentiment(self,tweet):
		analysis = TextBlob(self.clean_tweet_text(tweet))
		#print(analysis)
		return analysis.sentiment.polarity		

if __name__ == "__main__":
	tweet_analyzer = Analyzer()
	twitter_client = TwitterClient()

	api = twitter_client.get_twitter_client_api()
	tweets = api.user_timeline(screen_name="pewdiepie",count=20)
	df = tweet_analyzer.tweet_to_dataframe(tweets)
	df['sentiment'] = np.array([tweet_analyzer.get_sentiment(tweet) for tweet in df['Tweets']])
	print(df)
	print("Average sentiment score:",np.mean(df['sentiment']))	
