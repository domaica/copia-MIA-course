from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# @TODO: setup mongo connection
conn = 'mongodb://localhost:27017'

# @TODO: connect to mongo db and collection
client = pymongo.MongoClient(conn)

db = client.store_inventory_db

db.produce.drop()

db.produce.insert_many([
{
		'type':'apples',
		'cost': .23,
        "stock": 333
	},
	{
		'type':'pineapples',
		'cost': 1.05,
        "stock": 100
	},
	{
		'type':'watermelon',
		'cost': 2.00,
        "stock": 50
	}
])


@app.route('/')
def index():
    # @TODO: write a statement that finds all the items in the db and sets it to a variable
    merchandise = list(db.produce.find())
    print(merchandise)

    # @TODO: render an index.html template and pass it the data you retrieved from the database
    return render_template('index.html', merchandise=merchandise)


if __name__ == "__main__":
    app.run(debug=True)
