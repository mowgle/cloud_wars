
import tweepy
import pandas as pd

# define API Keys and Access tokens as variables
api_key = "6hLFaYyDGmkPmBwoXKctOoSYi"
api_key_secret = "Fpy9Zz0kH1CTwEdbaDJgdXWTwteePLSfbGwz1WstHZvyzOiplg"
access_token = "2785943655-y2zvUthJViU6mjaWvJ7Ksnk4T4W4dkTkLgQNEdZ"
access_tokent_secret = "6dQYJV3Oz8QFdQZUt9cuEabNs67fs2FE2sw5fkby40oqP"

# authenticate using 0Auth
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_tokent_secret)
api = tweepy.API(auth)

# create five variables, one for each hashtag of interest
lst_hashtags_res = "#Resolution2020"
lst_hashtags_voi = "#VoiceForThePlanet"
lst_hashtags_eco = "#EcoFriendly"
lst_hashtags_zer = "#ZeroWaste"
lst_hashtags_cli = "#ClimateEmergency"

# set the number of tweets you wish to pull from each hashtag. The resulting dataframe will contain this number of records *5
max_tweets = 100

# create variables that return the number of tweets specified in max_tweets, per hashtag
relevant_tweets_res = tweepy.Cursor(api.search, q=lst_hashtags_res).items(max_tweets)
relevant_tweets_voi = tweepy.Cursor(api.search, q=lst_hashtags_voi).items(max_tweets)
relevant_tweets_eco = tweepy.Cursor(api.search, q=lst_hashtags_eco).items(max_tweets)
relevant_tweets_zer = tweepy.Cursor(api.search, q=lst_hashtags_zer).items(max_tweets)
relevant_tweets_cli = tweepy.Cursor(api.search, q=lst_hashtags_cli).items(max_tweets)

# initialise a list variable
list = []

# loop through each of the above variables made, pulling relevant information from each tweet and storing it in list
for tweet in relevant_tweets_res:
    twit = [tweet.user.name, tweet.user.location, tweet.text]
    list.append(twit)

for tweet in relevant_tweets_voi:
    twit =[tweet.user.name, tweet.user.location, tweet.text]
    list.append(twit)

for tweet in relevant_tweets_eco:
    twit =[tweet.user.name, tweet.user.location, tweet.text]
    list.append(twit)

for tweet in relevant_tweets_zer:
    twit =[tweet.user.name, tweet.user.location, tweet.text]
    list.append(twit)

for tweet in relevant_tweets_cli:
    twit =[tweet.user.name, tweet.user.location, tweet.text]
    list.append(twit)

# write results to a Pandas dataframe
tweet_df = pd.DataFrame(list)
print(tweet_df.head())

# Get the number of rows in the resulting dataframe (should be max_tweets * 5)
print(len(tweet_df.index))
