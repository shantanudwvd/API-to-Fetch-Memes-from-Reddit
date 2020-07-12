import praw

reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     password='YOUR_PASSWORD',
                     user_agent='YOUR_USER_AGENT',
                     username='YOUR_USER_NAME')


def check_image(urllink):
    ext = urllink[-4:]
    if ext == '.jpg' or ext == '.png':
        return True

    return False


def get_meme(sub, count):
    sub_reddit = reddit.subreddit(sub)
    hot_meme = sub_reddit.hot(limit=count)
    result = []
    for submissions in hot_meme:
        temp = {"Title": submissions.title,
                "Url": submissions.url,
                "Upvotes": submissions.ups,
                "Downvotes": submissions.downs,
                "Redditurl": submissions.shortlink,
                "Subreddit": sub
                }
        result.append(temp)

    return result


def get_text(sub, count):
    sub_reddit = reddit.subreddit(sub)
    hot_meme = sub_reddit.hot(limit=count)
    result = []
    textP = "No selftext Present"
    for submission in hot_meme:
        if submission.selftext:
            temp = {"Title": submission.title,
                    "text": submission.selftext,
                    "Upvotes": submission.ups,
                    "Downvotes": submission.downs,
                    "Redditurl": submission.shortlink,
                    "Subreddit": sub
                    }
        else:
            temp = {"Title": submission.title,
                    "text": textP,
                    "Upvotes": submission.ups,
                    "Downvotes": submission.downs,
                    "Redditurl": submission.shortlink,
                    "Subreddit": sub
                    }

        result.append(temp)
    return result
