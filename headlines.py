import feedparser
from flask import Flask, render_template

app = Flask(__name__)

BBC_FEEDS = {
    "bbc": "http://feeds.bbci.co.uk/news/rss.xml",
    "cnn": "http://rss.cnn.com/rss/edition.rss",
    "fox": "http://feeds.foxnews.com/foxnews/latest",
    "iol": "http://www.iol.co.za/cmlink/1.640"
}


@app.route('/')
@app.route('/<source>')
def get_news(source="bbc"):
    feed = feedparser.parse(BBC_FEEDS[source])
    articles = feed['entries']
    return render_template("home.html", articles=articles)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
