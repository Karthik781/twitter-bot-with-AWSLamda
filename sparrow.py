#!/usr/bin/env python
import random
import tweepy
from ssm_secrets import get_secret

# Create Twitter client using the credentials stored in SS
client = tweepy.Client(
    consumer_key=get_secret("CONSUMER_KEY"),
    consumer_secret=get_secret("CONSUMER_SECRET"),
    access_token = get_secret("ACCESS_TOKEN_KEY"),
    access_token_secret=get_secret("ACCESS_TOKEN_SECRET")
)


# Sample random tweets
potential_tweets = [
    'This is my first tweet with bot',
    'Wow! Isn\'t Sparrow just the coolest!',
    'Jeez! Everyone should learn about AWS Lambda and Twitter Bots'
]


def send_tweet(potential_tweets):
    """Sends a tweet to Twitter"""
    client.create_tweet(text=potential_tweets,user_auth=True)


def handler(event, context):
    """Sends random tweet from list of potential tweets"""
    send_tweet(random.choice(potential_tweets))

# tweet_id=1546108752168099846
def like_tweet(tweet_id):
    client.like(tweet_id=tweet_id,user_auth=True)

