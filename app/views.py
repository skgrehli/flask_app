from flask import Flask
from flask import render_template
from datetime import datetime
from . import app

# how do I get these into a connections.py module instead?
db_connection = "mongodb+srv://dev01:KKizYFNtsboBQAf2@asa01-jeqsk.mongodb.net/admin"
from pymongo import MongoClient
client = MongoClient(db_connection)
db = client.asa_db_01
quandl_key = 'XzsKV7TBwpzcgjXj4RD3'
import quandl
quandl.ApiConfig.api_key = quandl_key

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    positions = db.tickets.find({"status":"open"}) # positions = db.tickets.find_one({"instrument": "tsxv:glxy"})
    return render_template("dashboard.html",
        positions=positions,
        example_list = []) # can be removed

@app.context_processor
def calculators():
    def position_exposure(price, quantity):
        return(price * quantity)
    def convert_fx(currency):
        if currency == 'btc':
            data = quandl.get('GDAX/BTC_EUR', rows=1, returns='numpy')
            for i in data:
                base = (i[1])
                currency = 1 / base
        elif currency == 'eth':
            data = quandl.get('GDAX/ETH_EUR', rows=1, returns='numpy')
            for i in data:
                base = (i[1])
                currency = 1 / base
        elif currency == 'cad':
            data = quandl.get('ECB/EURCAD', rows=1, returns='numpy')
            for i in data:
                currency = (i[1])
        elif currency == 'sek':
            data = quandl.get('ECB/EURSEK', rows=1, returns='numpy')
            for i in data:
                currency = (i[1])
        elif currency == 'usd':
            data = quandl.get('ECB/EURUSD', rows=1, returns='numpy')
            for i in data:
                currency = (i[1])
        else:
            currency = 1
        return(currency)
    def convert_fx_date(currency, date): # why is only EUR/SEK pair listed?
        if currency == 'sek':
            data = quandl.get('ECB/EURSEK', start_date=date, end_date=date, rows=1, returns='numpy')
            for i in data:
                currency = (i[1])
        else:
            currency = 1
        return currency
    return dict(position_exposure=position_exposure, convert_fx=convert_fx, convert_fx_date=convert_fx_date)


# tutorial related pages
@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
