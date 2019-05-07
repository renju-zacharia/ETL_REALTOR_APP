from flask import Flask, render_template, redirect, request
from flask_pymongo import PyMongo
import pymongo
import Get_Details

# Create an instance of Flask
app = Flask(__name__)

@app.route("/")
def home():

    return render_template("index.html")
    # Return template and data
 
# Route that will trigger the scrape function
@app.route("/extract", methods=['POST'])
def extract():

    town = request.form['town']
    school_data, listings_data = Get_Details.extract_data(town)
    
    return render_template("index.html", school_data=school_data, listings_data=listings_data,town=town)
    
    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
