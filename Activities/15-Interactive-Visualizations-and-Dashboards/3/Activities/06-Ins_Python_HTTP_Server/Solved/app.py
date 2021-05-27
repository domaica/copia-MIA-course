from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    # df = pd.read_csv('...')
    df = pd.read_json('data/data.json')
    return render_template('index.html', df=df.to_json(orient='records'))
    # return render_template('index.html', mars=mars)

if __name__ == "__main__":
    app.run()