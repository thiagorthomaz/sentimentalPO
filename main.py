import configparser
import tweepy
from textblob import TextBlob

config = configparser.ConfigParser()
config.read('config.ini')

# Step 1 - Authenticate

consumer_key= config['TWITTER_TOKEN']['CONSUMER_KEY']
consumer_secret= config['TWITTER_TOKEN']['CONSUMER_SECRET']

access_token=config['TWITTER_TOKEN']['ACCESS_TOKEN']
access_token_secret=config['TWITTER_TOKEN']['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
   