from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET'])
def linkScraper():

        d = []  # TODO: Change list to dictionary with keys as [1]th index of the Links (on splitting Links at '/')
        # Keys could be DEGREE, DIPLOMA, Exam_Section and so on

        url_news = "https://www.vjti.ac.in"         # link to scrape links from

        # headers for complying with GET request
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
                                Links = url_news + link.get("href")    # adding URI to source IDs of links to get URL
                                print(Links)
                                d.append(Links)
                except Exception:
                        links = None

        d.pop(-1)       # removing last item for list which is not required

        return jsonify(d)       # to decode JSON later in Flutter, converting obtained data to JSON


if __name__ == '__main__':
    app.run(port=5000)
    # TODO: Upload FLask app on server to support backend and provide URL to be used on Flutter app

