from flask import Flask
from textblob import TextBlob

app = Flask(__name__)


@app.route('/')
def index():
	return '<h1>Hello, world!</h1>'


@app.route('/sentiment/<frase>')
def sentiment(frase):
	tb = TextBlob(frase)
	return f'Sentiment: {tb.sentiment.polarity}'


app.run()