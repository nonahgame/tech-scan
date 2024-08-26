from flask import Flask, render_template
from patterns import patterns
import yfinance as yf

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", patterns=patterns)

@app.route("/snap")
def snap():
    with open('datasets/companies.csv') as f:
        companies = f.read().splitlines()
        for company in companies:
            symbol = company.split(',')[0]
            #print(symbol)
            DataFrame = yf.download(symbol, start="2024-05-01 ", end="2024-08-24 ")
            #dd.to_csv('datasets/daily.{symbol}.csv')
    return {'number': 'twenthy'}


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
