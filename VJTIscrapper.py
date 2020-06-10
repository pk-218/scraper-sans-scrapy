from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/', methods=['GET'])
def linkscraper():
    return 'ToScrape'


url_news = "https://www.vjti.ac.in/"

headers = {
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://www.wikipedia.org/',
        'Connection': 'keep-alive',
}

r = requests.get(url=url_news, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")
customs = soup.find_all("div", {"class": "custom"})
for custom in customs:
        try:
                links = custom.find_all("a")
                for link in links:
                        Links = [link.get("href")]
                        print(Links)
        except Exception:
                pass


if __name__ == '__main__':
    app.run(port=5000)

