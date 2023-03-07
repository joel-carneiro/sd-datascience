from flask import Flask
from textblob import TextBlob

app = Flask(__name__)


@app.route('/')
def index():
	return '<h1>Hello, world!</h1>'


@app.route('/sentimento/<frase>')
def sentiment(frase):
	tb = TextBlob(frase)
	return f"polaridade: {tb.sentiment.polarity}"


app.run(debug=True)