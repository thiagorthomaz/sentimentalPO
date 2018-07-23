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

for tweet in public_tweets:

    text = TextBlob(tweet.text);    
    print(text)

    #Step 4 Perform translation if needed
    #Step 5 Perform Sentiment Analysis on Tweets
    if (text.detect_language() != 'en'):
        translated_tweet = TextBlob(str(text.translate(to='en')))
        analysis = translated_tweet
        print(analysis.sentiment)
    else :
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)

    print("")
    
