# Dear programmer:
#When i wrote this code, only god and
#I knew how it worked.
#Now, only god knows it !

#Therefore, if you are trying to optimize
#this routine and it fails (most surely),
#please increase this counter as a 
#warning for the next person:

#total_hours_wasted_here = 57


import tweepy
import config

#Twitter API v2  REFERENCE OAuth 2.0 Bearer Token (App-Only)
client = tweepy.Client(bearer_token=config.bearToken)

#TWITTER API V2 REFERENCE OAuth 1.0a User Context
api = tweepy.Client(
    consumer_key=config.key,
    consumer_secret=config.keySecret,
    access_token=config.accessToken,
    access_token_secret=config.accessTokenSecret
)
FILE_NAME = 'last_seen.text'
tweetId = []

def check(FILE_NAME, tweetId):
    # open file and read the content in a list
    with open(FILE_NAME, 'r') as fp:
        for line in fp:
            # remove linebreak from a current name
            # linebreak is the last character of each line
            x = line[:-1]
            #check if it already exists
            if (str(tweetId) == x):
                return 1
        return 0


def store_last_seen(FILE_NAME, tweetId):
    # open file in write mode
    with open(FILE_NAME, 'a') as fp:
        for item in tweetId:
            # write each item on a new line
            fp.write("%s\n" % item)
    fp.close()
    return


# je recherche tous les tweets recents sur #cmrdev
query = "#CmrDev OR #CaParleDev OR #PHP"

newRequest = client.search_recent_tweets(query=query, max_results= 10)
for tweet in (newRequest.data):
    get = client.get_tweet(tweet.id, expansions="author_id")
    # print(get.includes.get('users')[0].id) #auth id
    # print(tweet.id) #tweet id

    #check if the tweet auth is me
    if get.includes.get('users')[0].id == config.myId: #skip
        continue
    
    see = check(FILE_NAME, tweet.id ) #check if exist: false = 0, true = 1
    if (see == 0):
        try:
            tweetId.insert(0, tweet.id)
            store_last_seen(FILE_NAME, tweetId )
            #tweet
            api.create_tweet(text= tweet.text, quote_tweet_id=tweet.id)
            #follow
            api.follow_user( target_user_id = get.includes.get('users')[0].id)
            #retweet
            # api.retweet(tweet_id=tweet.id) I need elevated access on my twitter dev account
            #like
            # api.like(tweet_id=tweet.id) #I need elevated access on my twitter dev account
        except:
            pass
    #print(tweet.text) #tweet content