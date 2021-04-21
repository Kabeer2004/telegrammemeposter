# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 15:00:43 2021

@author: Kabeer Ahmed
"""

import praw
import requests
import time
import schedule

# -1001299298185

reddit = praw.Reddit(client_id='your-client-id', client_secret='your-client-secret', user_agent='your-user-agent')


# get 10 hot posts from subreddit
def post_memes():
    hot_posts = reddit.subreddit('dankmemes').hot(limit=23)
    for post in hot_posts:
       post_string = post.title + "\n" + post.url
       base_url = 'https://api.telegram.org/your-bot-id-here/sendMessage?chat_id=-1001299298185&text="{}"'.format(post_string)
       requests.get(base_url)
       time.sleep(3600)
       
schedule.every().day.at("00:00").do(post_memes)       

while True:
    schedule.run_pending()
    time.sleep(60)
