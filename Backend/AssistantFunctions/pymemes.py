import praw
import random

import environ
config = environ.Env()
# reading .env file
environ.Env.read_env()
REDDIT_CLIENT_ID = config("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = config("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = config("REDDIT_USER_AGENT")

reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                     client_secret=REDDIT_CLIENT_SECRET, user_agent=REDDIT_USER_AGENT)


def get_meme(subreddit):
    sr = reddit.subreddit(subreddit)
    posts = sr.new(limit=100)
    memes = []
    for m in posts:
        memes.append([m.title, m.url])
    return memes
