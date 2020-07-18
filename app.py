from flask import Flask, jsonify
import random, logging
from main import get_meme, check_image, get_text

app = Flask(__name__)
count = 0
randommeme = ['meme', 'dankmeme', 'wholesomeme', 'memes']


@app.route('/')
def welcome():
    return "Welcome To API"


@app.route('/givememe')
def random_meme():  # Random and one
    sub = random.choice(randommeme)
    r = get_meme(sub, 100)
    requested = random.choice(r)

    while not check_image(requested["Url"]):
        requested = random.choice(r)

    return jsonify({
        'Title': requested["Title"],
        'Url': requested["Url"],
        'Upvotes': requested["Upvotes"],
        'Downvotes': requested["Downvotes"],
        'Redditurl': requested["Redditurl"],
        'Subreddit': requested["Subreddit"]
    })


@app.route('/givememe/<sub>')
def custom_meme(sub):
    try:
        r = get_meme(sub, 100)
    except:
        return jsonify({
            'Status_code': 404,
            'Message': 'Invalid Subreddit'
        })

    requsted = random.choice(r)

    while not check_image(requsted["Url"]):
        count = count + 1
        requsted = random.choice(r)
        if count == 100:
            break

    return jsonify({
        'Title': requsted["Title"],
        'Url': requsted["Url"],
        'Upvotes': requsted["Upvotes"],
        'Downvotes': requsted["Downvotes"],
        'Redditurl': requsted["Redditurl"],
        'Subreddit': requsted["Subreddit"]
    })


@app.route('/givememe/<int:c>')
def multiple(c):
    sub = random.choice(randommeme)

    if c >= 50:
        return jsonify({
            'status_code': 400,
            'message': 'Ensure that the Count is less than 50'
        })

    requested = get_meme(sub, 100)

    random.shuffle(requested)

    memes = []
    for post in requested:
        if check_image(post["Url"]) and len(memes) != c:
            t = {
                'Title': post["Title"],
                'Url': post["Url"],
                'Upvotes': post["Upvotes"],
                'Downvotes': post["Downvotes"],
                'Redditurl': post["Redditurl"],
                'Subreddit': post["Subreddit"]
            }
            memes.append(t)

    return jsonify({
        'memes': memes,
        'count': len(memes)
    })


@app.route('/givememe/<sub>/<int:c>')
def multiple_from_sub(sub, c):
    if c >= 50:
        return jsonify({
            'status_code': 400,
            'message': 'Ensure that the Count is less than 50'
        })

    requested = get_meme(sub, 100)

    random.shuffle(requested)

    memes = []
    for post in requested:
        if check_image(post["Url"]) and len(memes) != c:
            t = {
                'Title': post["Title"],
                'Url': post["Url"],
                'Upvotes': post["Upvotes"],
                'Downvotes': post["Downvotes"],
                'Redditurl': post["Redditurl"],
                'Subreddit': post["Subreddit"]
            }
            memes.append(t)

    return jsonify({
        'memes': memes,
        'count': len(memes)
    })


@app.route('/givetext/<sub>')
def text_meme(sub):  # showerthoughts or quotes
    r = get_text(sub, 100)
    requsted = random.choice(r)

    return jsonify({
        'Title': requsted["Title"],
        'Selftext': requsted["text"],
        'Upvotes': requsted["Upvotes"],
        'Downvotes': requsted["Downvotes"],
        'Redditurl': requsted["Redditurl"],
        'Subreddit': requsted["Subreddit"]
    })


@app.route('/givetext/<sub>/<int:count>')
def text_count_meme(sub, count):
    if count >= 50:
        return jsonify({
            'status_code': 400,
            'message': 'Please ensure the count is less than 50'
        })

    requested = get_text(sub, 100)
    random.shuffle(requested)

    textmeme = []
    for post in requested:
        if len(textmeme) != count:
            t = {
                'Title': post["Title"],
                'Selftext': post["text"],
                'Upvotes': post["Upvotes"],
                'Downvotes': post["Downvotes"],
                'Redditurl': post["Redditurl"],
                'Subreddit': post["Subreddit"]
            }
            textmeme.append(t)

    return jsonify({
        'sub': textmeme,
        'count': len(textmeme)
    })


@app.errorhandler(404)
@app.route('/<lol>')
def not_found(lol):
    return "<h1git >Are You Lost?<h1>"


if __name__ == '__main__':
    app.run()
