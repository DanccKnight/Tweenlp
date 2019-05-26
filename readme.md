These scripts fetch tweets from the Twitter API using Tweepy. 

streamer.py fetches tweets from the Twitter Streaming API, and performs sentiment analysis on the it. It then displays the average score of the sentiments obtained from the tweets. The number of tweets that are to be fetched is determined by the limit variable in the Listener class. 

usertweets.py fetches a given number of tweets of a specific user. It performs sentiment analysis on the tweets and displays an average score. The score varies between -1 and 1. If the score is towards -1, it's negative. If it's towards 1, it's positve. 
