from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)


mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")


@app.route("/")
def home():


    destination = mongo.db.scrape_mars.find_one()

    return render_template("index.html", mars_data=destination)


@app.route("/scrape")
def scrape():

    mars_data = mongo.db.scrape_mars
    mars_data = scrape_mars.scrape_mars_news()
    mars_data = scrape_mars.scrape_mars_images()
    mars_data = scrape_mars.scrape_mars_facts()
    mars_data = scrape_mars.scrape_mars_weather()
    mars_data = scrape_mars.scrape_mars_hemispheres()
    mars_info.update({}, mars_data, upsert=True)

    
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)