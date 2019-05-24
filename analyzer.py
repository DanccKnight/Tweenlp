import json
import pandas as pd
import numpy as np

path = '/home/ansuman/Twitter-NLP/tweets.txt'

def isReply(tweet):
	if(tweet['in_reply_to_status_id']): 
	#or tweet['in_reply_to_status_id_str'] 
	#or tweet['in_reply_to_user_id'] 
	#or tweet['in_reply_to_user_id_str']
	#or tweet['in_reply_to_screen_name']):
		return 1
	else: 
		return 0

tweets_data = []
tweets_text = []
tweets_file = open(path,"r")
for line in tweets_file:
	try:
		tweet = json.loads(line)
		tweets_data.append(tweet)
	except Exception as e:
		print(str(e))

for i in range(len(tweets_data)):
		if(isReply(tweets_data[i])):
			tweets_text.append(tweets_data[i]['text'])

for i in range(len(tweets_text)):
	print(tweets_text[i])

#tweets = pd.DataFrame(data=[tweets_text['text'] for tweet in tweets_text],columns=['Tweets'])
#tweets['Retweet_Count'] = np.array([tweets_data['retweet_count'] for tweet in tweets_data])
#print(pd)
