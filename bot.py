# Dear programmer:
#When i wrote this code, only god and
#I knew how it worked.
#Now, only god knows it !

#Therefore, if you are trying to optimize
#this routine and it fails (most surely),
#please increase this counter as a 
#warning for the next person:

#total_hours_wasted_here = 28


import tweepy
import config

client = tweepy.Client(bearer_token=config.bearToken)
# client = tweepy.Client(
#     consumer_key=config.key,
#     consumer_secret=config.keySecret,
#     access_token=config.accessToken,
#     access_token_secret=config.accessTokenSecret
# )
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
        print('Done')
    fp.close()
    return


# je recherche tous les tweets recents sur #cmrdev
query = "#CmrDev"
newRequest = client.search_recent_tweets(query=query, max_results= 100)
for tweet in (newRequest.data):
    get = client.get_tweet(tweet.id, expansions="author_id")
    # print(get.includes.get('users')[0].id) #auth id
    # print(tweet.id) #tweet id

    #check if the tweet auth is me
    if get.includes.get('users')[0].id == config.myId: #skip
        continue
    
    see = check(FILE_NAME, tweet.id ) #check if exist: false = 0, true = 1
    if (see == 0):
        tweetId.insert(0, tweet.id)
        store_last_seen(FILE_NAME, tweetId )
        #follow
        # client.follow(get.includes.get('users')[0].id)
        #retweet
        #client.retweet(tweet.id)
        #like
        #client.like(tweet.id)
        #comment
        
    print(tweet.text) #tweet content





# query = 'covid -is:retweet'
# answer = client.get_users_mentions(id=config.myId)
# for tweet in answer.data:
#     get = client.get_tweet(tweet.id, expansions="author_id")
#     print(get.includes.get('users')[0].id) #auth id
#     print(tweet.id) #tweet id
#     print(tweet.text) #tweet content

# je vais suivre tous les tweets sur cmrdev, retwetter, liker , et follow
