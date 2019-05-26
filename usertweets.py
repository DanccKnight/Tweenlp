import credentials
from tweepy import Cursor
from tweepy import API 
from tweepy import OAuthHandler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Authenticator():
	def authenticate(self):
		auth = OAuthHandler(credentials.CONSUMER_KEY,credentials.CONSUMER_SECRET)
		auth.set_access_token(credentials.ACCESS_TOKEN,credentials.ACCESS_TOKEN_SECRET)
		return auth 

class TwitterClient():
	def __init__(self, user=None):
		self.auth = Authenticator().authenticate()
		self.twitter_client = API(self.auth)
#		self.user = user

	def get_twitter_client_api(self):
		return self.twitter_client
	
#	def get_user_tweets(self, num_tweets, user_fetched_tweets):
#		for tweet in Cursor(self.twitter_client.user_timeline, id = self.user).items(num_tweets):
#			print(tweet)
#			with open(user_fetched_tweets,'a') as file:
#				file.write(str(tweet))

class Analyzer():
	def tweet_to_dataframe(self,tweets):
		df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
		df['date'] = np.array([tweet.created_at for tweet in tweets])
		df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
		df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
		return df

if __name__ == "__main__":
	tweet_analyzer = Analyzer()
	twitter_client = TwitterClient()

#	user_fetched_tweets = "userfetchedtweets.json"
#	print(twitter_client.get_user_tweets(4,user_fetched_tweets))
	api = twitter_client.get_twitter_client_api()
	tweets = api.user_timeline(screen_name="pewdiepie",count=20)
	df = tweet_analyzer.tweet_to_dataframe(tweets)
	#print(df)
	print("Average no. of retweets:",np.mean(df['retweets']))
	print("Highest liked tweet:",np.max(df['likes'])) 

	time_likes = pd.Series(data=df['likes'].values,index=df['date'])
	time_likes.plot(figsize=(16,4),label="likes",legend=True)
	time_retweet = pd.Series(data=df['retweets'].values,index=df['date'])
	time_retweet.plot(figsize=(16,4),label="retweets",legend=True)
	plt.show()
	
