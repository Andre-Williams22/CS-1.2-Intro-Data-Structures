from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob
import os
from sample import sample_by_frequency
from markov import Markogram
from utils import good_words

consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')

access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

app = Flask(__name__)

path = 'trump.csv'
words = good_words(path)
markov = Markogram(words)
@app.route("/")
def index():

    return render_template('index.html')

# @app.route("/search",methods=["POST"])
# def search():
#     search_tweet = request.form.get("search_query")
   
#     t = []
#     tweets = api.search(search_tweet, tweet_mode='extended')
#     for tweet in tweets:
#         polarity = TextBlob(tweet.full_text).sentiment.polarity
#         subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
#         t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    # return jsonify({"success":True,"tweets":t})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT', 5000))