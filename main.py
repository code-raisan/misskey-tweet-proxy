from tweety.bot import Twitter
from misskey import Misskey
import os
import env

tweet_id_path = f"{os.path.dirname(__file__)}/lasttweet.txt"
mk = Misskey(env.SERVER_HOST, i=env.API_TOKEN)
app = Twitter(env.SCREEN_ID)

with open(tweet_id_path, encoding="utf-8", mode="r") as f:
    last_tweet_id = f.read()

tweets = app.get_tweets()
for tweet in tweets:
    if int(tweet.id) > int(last_tweet_id):
        text = f"https://twitter.com/{tweet.author.username}/status/{tweet.id}"
        mk.notes_create(text=text)

with open(tweet_id_path, encoding="utf-8", mode="w") as f:
    f.write(tweets[0].id)
