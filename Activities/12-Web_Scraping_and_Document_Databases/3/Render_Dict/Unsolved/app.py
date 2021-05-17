# import necessary libraries
from flask import Flask, render_template

# @TODO: Initialize your Flask app here
app = Flask(__name__)


# @TODO: Create a list of dictionaries
animal_dict = [
	{
		'animal':'dog',
		'type':'mammal'
	},
	{
		'animal':'kangaroo',
		'type':'marsupial'
	},
	{
		'animal':'snake',
		'type':'reptile'
	}
]


# @TODO:  Create a route and view function that takes in a dictionary and renders index.html template
@app.route("/")
def index():
    return render_template("index.html", dict=animal_dict)

if __name__ == "__main__":
    app.run(debug=True)
