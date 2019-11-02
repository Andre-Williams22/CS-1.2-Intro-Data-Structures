from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


consumer_key = '9Ld9t9g9gZxKCOnLMIVPlsVUB'
consumer_secret = 'zXKFx9KIfTDpVXcVtE6I5HfGkcIaAKF7fryXiYvXg4LKkaGfyI'

access_token = '1027940289309286400-s4uhWJQ4Syol3KYDYzPejXR2QUPJiV'
access_token_secret = 'vqgUaJFTj6syYbnTLrlwfAwRnV3wemjAYmp1Yj7R6n1kL'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    # t = [[]]
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})

if __name__ == '__main__':
    app.run(debug=True)