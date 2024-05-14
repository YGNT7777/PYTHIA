import praw
from praw.models import MoreComments
import sentiment

def ex_reddit(search,N=50,X='new'):
    reddit = praw.Reddit(
        client_id = "YOUR_CLIENT_ID",
        client_secret = "YOUR_CLIENT_SECRET",
        user_agent = "YOUR_USER_AGENT",

    )

    Redditt_threads = []

    if (X == "controversial"):
        for submission in reddit.subreddit(search).controversial(limit=N):
            Redditt_threads.append(submission.title)
            print(submission.title)
            if isinstance(submission, MoreComments):
                continue

        
    elif (X == "hot"):
        for submission in reddit.subreddit(search).hot(limit=N):
            Redditt_threads.append(submission.title)
            print(submission.title)
            if isinstance(submission, MoreComments):
                continue

    elif (X == "new"):

        for submission in reddit.subreddit(search).new(limit=N):
            Redditt_threads.append(submission.title)
            print(submission.title)
            if isinstance(submission, MoreComments):
                continue

    elif (X == "rising"):
        for submission in reddit.subreddit(search).rising(limit=N):
            Redditt_threads.append(submission.title)
            print(submission.title)
            if isinstance(submission, MoreComments):
                continue

    elif (X == "top"):
        for submission in reddit.subreddit(search).top(limit=N):
            Redditt_threads.append(submission.title)
            print(submission.title)
            if isinstance(submission, MoreComments):
                continue
    return Redditt_threads
