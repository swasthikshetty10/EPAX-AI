import praw
import random
REDDIT_CLIENT_ID="REDDIT_CLIENT_ID"
REDDIT_CLIENT_SECRET="REDDIT_APP_SECRET"
REDDIT_USER_AGENT="Nurd Bot"

reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,client_secret=REDDIT_CLIENT_SECRET,user_agent=REDDIT_USER_AGENT)

def get_meme(subreddit):
  sr = reddit.subreddit(subreddit)
  posts = sr.new(limit=100)
  memes = []
  for m in posts:
    memes.append([m.title , m.url])
  return memes
  
