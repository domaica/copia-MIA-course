from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

# Use PyMongo to connect with MongoDB 
client = pymongo.MongoClient('mongodb://localhost:27017')

# mars_db
db = client.mars_db
# marsdata collection into mars_db
marsdata = db.marsdata

# Create an instance of Flask
app = Flask(__name__)


# Route to render index.html template using data from Mongo
@app.route('/')
def home():
	mars = marsdata.find_one()
	return render_template('index.html', mars=mars)
	# return render_template('index.html')

#Route scrape invoked by pressing button in index.html
@app.route('/scrape')
def scrape():
	scrape_mars.scrape()
	return "Scrapped data done"

 
if __name__ == "__main__":
    app.run(debug=True)