import credentials
from tweepy import Cursor
from tweepy import API 
from tweepy import OAuthHandler

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
		for tweet in Cursor(self.twitter_client.user_timeline, id = self.user).items(num_tweets):
			print(tweet)
			with open(user_fetched_tweets,'a') as file:
				file.write(str(tweet))

if __name__ == "__main__":
	
	user_fetched_tweets = "userfetchedtweets.json"
	twitter_client = TwitterClient('pewdiepie')
	print(twitter_client.get_user_tweets(4,user_fetched_tweets))

