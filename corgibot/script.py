#! usr/bin/env python3
import praw
import urllib
import os

sub = input("What subreddit would you like to search for images of corgis? ")


reddit = praw.Reddit(client_id='NvEWb8zjLdLZWw', \
                     client_secret='WjMmIJ2HXVLJSjUpbxSWxNWVeIaffg', \
                     user_agent='corgibot')

cwd = os.getcwd()
newpath = cwd + '/images'

if not os.path.exists(newpath):
    os.makedirs(newpath)

subreddit = reddit.subreddit(sub)

search_subreddit = subreddit.search("corgi")

print("Searching for images of corgis in /r/" + sub)

for submission in search_subreddit:
    try:
        if 'http://imgur.com/' in submission.url:
            url = submission.url + '.jpg'
            print ('> * ' + url)
            fullfilename = os.path.join(newpath, submission.url+ '.jpg')
            urllib.urlretrieve(submission.url, fullfilename)
        
        else:
            fullfilename = os.path.join(newpath, submission.id+ '.jpg')

            urllib.urlretrieve(submission.url, fullfilename)
            print ('> ' + submission.url)

    except:
            pass

