import requests
from flask import Flask, render_template, redirect, request
import os

API_KEY = os.environ.get("API_KEY")
URL = "http://api.marketstack.com/v2/"
SELECT = "eod"



app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        stock = request.form.get("stocks")
        print(stock)
        response = requests.get(URL + f"{SELECT}?access_key={API_KEY}&symbols={stock}")
        info = response.json()
        data = info['data']
        # print(data[0])
        return render_template('index.html', data=data)
    return render_template("index.html")






if __name__ == "__main__":
    app.run(debug=True)