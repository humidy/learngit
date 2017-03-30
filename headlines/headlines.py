# -*- coding:utf-8 -*-
from argparse import _ActionsContainer

import feedparser
import sys
from flask import Flask
from flask import render_template

reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)

RSS_FEEDS = {"ifeng": "http://news.ifeng.com/rss/index.xml",
             "geek": "http://www.geekonomics10000.com/feed",
             "songshu": "http://songshuhui.net/feed",
             "mtime": "http://feed.mtime.com/my/seemovie/feed.rss"
             }


@app.route("/")
@app.route("/<feed_address>")
def get_news(feed_address="ifeng"):
    feed = feedparser.parse(RSS_FEEDS[feed_address])
    # print(feed)
    # first_article = feed['entries'][0]
    # print(first_article)
    return render_template("home.html", articles=feed['entries'])


if __name__ == '__main__':
    app.run(port=5000, debug=True)
