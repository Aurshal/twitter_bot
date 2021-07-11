import os
import tweepy

consumer_key = os.environ.get('tb_consumer_key')
consumer_secret_key = os.environ.get('tb_consumer_secret_key')
access_token = os.environ.get('tb_access_token')
access_token_secret = os.environ.get('tb_access_token_secret')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)

# getting access to my twitter timeline through api authentication
api = tweepy.API(auth)
# print(api.me().screen_name)
# getting my tweets from timeline
public_tweets = api.home_timeline(count=20)
tweets = public_tweets[:19]

for tweet in tweets:
    if api.get_status(tweet.id).favorited == False:
        print(f'Liking tweet {tweet.id} of {tweet.author.name}')
        api.create_favorite(tweet.id)
    else:
        continue

# print(type(public_tweets))

# for tweet in public_tweets:
#     print(tweet.text)

# user = api.get_user('@username')
# print(user.screen_name)
# print(user.followers_count)
# for friend in user.friends():
#     print(friend.screen_name)
