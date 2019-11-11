from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob
import os
import random 
import requests
from datetime import datetime 
import sys
from histogram import new_histogram
from sampler import sample_by_frequency
from markov import Markogram
#import tweeter 

consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')

access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

app = Flask(__name__)

class Display:
    def __init__(self, *args, **kwargs):
        self.message = ''
        self.count = 10

    def contact(self):
        return render_template('contact.html')

    def tweet_page(self):
        '''Renders the home page'''
        file = "trump.csv"
        with open(file, 'r') as f:
            words = f.read().split()
        self.count = int(request.args.get('words')) # takes the number of words the user wants in the sentence

        m = Markogram(words)
        self.message = m.get_string(self.count)


        return render_template('tweet.html', tweet=self.message, time=datetime.now())




    # def send_tweet(self):
    #     message = self.message
    #     tweeter.tweet(message)
    #     return redirect(url_for('home'))

    def home(self):
        return render_template('home.html')



disp = Display()
@app.route('/')
def home():
    return disp.home()


@app.route('/tweet')
def tweet():
    disp.message = ""
    disp.count = 7 #default
    return disp.tweet_page()

# @app.route('/send_tweet', methods=['POST'])
# def send_tweet():
#     return disp.send_tweet()

@app.route('/contact')
def contact():
    return disp.contact()

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

#     app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT', 80))


