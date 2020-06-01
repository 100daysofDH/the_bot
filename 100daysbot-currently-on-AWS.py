import json
import tweepy # to tweet
import datetime # for day specific tweets
import random # to get varying answers from list using choice()

import account # account.py: file containing the access tokens etc (also hashtags relevant to the account etc)

#-------------------------------------------------------------------------------
def lambda_handler(event, context):
    api = setup_tweepy_with_account()
    follow_followers(api)
    #tweet_stuff(api)
    check_mentions(api, ["#100DaysofDH"])
    retweet_100daysHashtag(api)

    if datetime.datetime.now().hour < 9:
        api.update_status(status=weekday_prompt())
        # with the AWS CloudWatch trigger like it is set, this event should happen
        # once per day in the morning

    # TODO retweet in different ways if secondary hashtags are present
    # TODO use trailing_hashtags?
    # primary_hashtags
    # secondary_hashtags
    # users_to_follow listener

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
#-------------------------------------------------------------------------------

def setup_tweepy_with_account():
    auth = tweepy.OAuthHandler(account.api_key, account.api_secret_key)
    auth.set_access_token(account.access_token, account.access_token_secret)
    api = tweepy.API(auth)
    return api

#-------------------------------------------------------------------------------
# The following function was adapted from: https://realpython.com/twitter-bot-python-tweepy/
def follow_followers(api):
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            follower.follow()


#-------------------------------------------------------------------------------

# mentions listener adapted from: https://realpython.com/twitter-bot-python-tweepy/
def check_mentions(api, keywords):
    for tweet in tweepy.Cursor(api.mentions_timeline).items():
        if any(keyword in tweet.text.lower() for keyword in keywords):
            if not tweet.user.following:
                tweet.user.follow()

            api.update_status(status=random.choice(account.mention_replies),
                              in_reply_to_status_id=tweet.id)
        if tweet.in_reply_to_status_id is not None and \
        not tweet.favorited: # its a reply
            tweet.favorite()
        if tweet.favorited:
            return

#-------------------------------------------------------------------------------
# TODO probably should make some proper error checking because errors appear
# bot seems to be working though, so no harm done so far...

def retweet_100daysHashtag(api):
    # adapted from https://dototot.com/reply-tweets-python-tweepy-twitter-bot/
    twts = api.search(q="100DaysofDH") # q=Search-Phrase

    #list of specific strings we want to check for in Tweets
    t = ['#100daysofDH', '100DaysofDH', '#100Daysofdh', account.main_hashtag]

    for s in twts:
        if s.retweeted:
            return
        if not s.retweeted:
            s.retweet()
        for i in t:
            if i == s.text:
                sn = s.user.screen_name
                m = "Hello @%s!" % (sn)
                msg = m + random.choice(account.mention_replies)
                s = api.update_status(status=msg, in_reply_to_status_id=s.id)

#-------------------------------------------------------------------------------

def tweet_stuff(api):

    """A testing function."""

    #api.update_status(status="This tweet is being posted automatically using Tweepy and an Amazon AWS Lambda function. #100DaysofDH")
    # Create a tweet
    api.update_status("Hello again Tweepy #100DaysofDH")

#-------------------------------------------------------------------------------

def weekday_prompt():
    today = datetime.datetime.today().weekday() # returns 0-6 (monday 0, sunday 6)
    # Return the day of the week as an integer, where Monday is 0 and Sunday is 6.
    return random.choice(account.week[today])
    # check if there already was a #DHchallengeprompt today
    # might become necessary if the AWS Lambda Event Watch were changed
