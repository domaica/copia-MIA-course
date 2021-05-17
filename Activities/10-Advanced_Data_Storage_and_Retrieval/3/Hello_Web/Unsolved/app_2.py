from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print("Server request for 'Home' page executing...")
    return("Welcome to Domaica's API!")

@app.route("/about")
def about():
    print("Server request for 'About' page executing...")
    return("Iñaki Domaica is in Miami")

if __name__ == "__main__":
    app.run(debug=True)