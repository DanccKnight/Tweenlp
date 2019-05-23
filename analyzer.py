import json
import pandas as pd
import numpy as np

path = '/home/ansuman/Twitter-NLP/tweets.txt'

tweets_data = []
tweets_file = open(path,"r")
for line in tweets_file:
	try:
		tweet = json.loads(line)
		tweets_data.append(tweet)
	except Exception as e:
		print(str(e))

tweets = pd.DataFrame(data=[tweets_data.text for tweet in tweets_data],columns=['Tweets'])
tweets['Retweet_Count'] = np.array([tweets_data.retweet_count for tweet in tweets_data])

print(df)


