import pandas as pd
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    df = pd.read_csv("data_fullstack.csv")
    return df.to_html()


if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)
