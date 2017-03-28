# -*- coding:utf-8 -*-
import feedparser
import sys
from flask import Flask

reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)

HUMIDY_FEED = "http://news.ifeng.com/rss/index.xml"


@app.route("/")
def get_news():
    feed = feedparser.parse(HUMIDY_FEED)
    first_article = feed['entries'][1]
    return """<html>
        <body>
            <h1> Humidy RSS 实验室 </h1>
            <b>{0}</b> <br/>
            <i>{1}</i> <br/>
            <p>{2}</p> <br/>
        </body>
    </html>""".format(first_article.get("title"),first_article.get("published"),first_article.get("summary"))


if __name__ == '__main__':
    app.run(port=5000, debug=True)
