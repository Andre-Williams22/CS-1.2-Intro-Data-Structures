from flask import Flask,render_template,request,jsonify, redirect, url_for
import tweepy
from textblob import TextBlob
import os
import random  
import sys
from histogram import new_histogram
from markov import HigherOrderMarkov
from utils import good_words

# for secrets
from dotenv import load_dotenv
load_dotenv()

# Twitter API setup
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')

access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# setup for markov chain and data 
path = 'trumps_speech.csv'
words = good_words(path)
markov = HigherOrderMarkov(words)
app = Flask(__name__)



@app.route('/')
def home():

    return render_template('home.html')


@app.route('/tweet')
def tweet():
    num = request.args.get('words')
    sentence = markov.walk(int(num))
    return render_template('tweet.html', sentence=sentence)

# @app.route('/contact')
# def contact():
#     # search_tweet = request.form.get("search_query")
   
#     # t = []
#     # tweets = api.search(search_tweet, tweet_mode='extended')
#     # for tweet in tweets:
#     #     polarity = TextBlob(tweet.full_text).sentiment.polarity
#     #     subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
#     #     t.append([tweet.full_text,polarity,subjectivity])
#         # t.append(tweet.full_text)
# #     return jsonify({"success":True,"tweets":t})
#     return render_template('contact.html')

@app.route('/send_tweet', methods=["POST"])
def send_tweet():
    word = request.form.get('tweet_sentence')
    api.update_status(status=word)
    return redirect(url_for('home'))


# @app.route("/")
# def index():
#     return render_template('home.html')

# @app.route("/search",methods=["POST"])
# def search():
#     search_tweet = request.form.get("search_query")
   
#     t = []
#     tweets = api.search(search_tweet, tweet_mode='extended')
#     for tweet in tweets:
#         polarity = TextBlob(tweet.full_text).sentiment.polarity
#         subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
#         t.append([tweet.full_text,polarity,subjectivity])
#         # t.append(tweet.full_text)

#     return jsonify({"success":True,"tweets":t})

if __name__ == '__main__':
    app.run(debug=True, port=8080)


