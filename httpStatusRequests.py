import csv
from flask import Flask, render_template
from connect import Urls

links = []


app = Flask(__name__)


@app.route('/')
def htmlpage():
    f = open("links.csv", "r")
    csv_f = csv.reader(f, delimiter=',')
    for row in csv_f:
        urls = row[0]
        correct = urls[0:4]
        if correct == "http":
            url_status = Urls(urlcsv=urls)
            links.append(url_status)
        else:
            urls = "http://" + urls
            url_status = Urls(urlcsv=urls)
            links.append(url_status)


def home():
    return render_template('index.html', links=links)


if __name__ == '__main__':
    app.run(debug=True)
