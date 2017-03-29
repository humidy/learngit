# -*- coding:utf-8 -*-
import feedparser
import sys
from flask import Flask

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
# def ifeng():
#     return get_news(feed_address="ifeng")
#
#
# # @app.route("/geek")
# def geek():
#     return get_news(feed_address="geek")
#
#
# # @app.route("/songshu")
# def songshu():
#     return get_news(feed_address="songshu")
#
#
# # @app.route("/mtime")
# def mtime():
#     return get_news(feed_address="mtime")

def get_news(feed_address="ifeng"):
    feed = feedparser.parse(RSS_FEEDS[feed_address])
    # print(feed)
    first_article = feed['entries'][0]
    # print(first_article)
    return """<html>
        <body>
            <h1> Humidy RSS 实验室 </h1>
            <b>{0}</b> <br/>
            <i>{1}</i> <br/>
            <p>{2}</p> <br/>
            <i>{3}</i> <br/>
            <i>{4}</i> <br/>
        </body>
    </html>""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"),
                      feed.get('feed').get('subtitle'), "Humidy DreamWorks")


if __name__ == '__main__':
    app.run(port=5000, debug=True)
