from flask import render_template
from flask_basicauth import BasicAuth
from datetime import datetime
from app import app

db_connection = "mongodb+srv://dev01:KKizYFNtsboBQAf2@asa01-jeqsk.mongodb.net/admin"
from pymongo import MongoClient
client = MongoClient(db_connection)
db = client.asa_db_01
quandl_key = 'XzsKV7TBwpzcgjXj4RD3'
import quandl
quandl.ApiConfig.api_key = quandl_key

app.config['BASIC_AUTH_USERNAME'] = 'john'
app.config['BASIC_AUTH_PASSWORD'] = 'matrix'
app.config['BASIC_AUTH_FORCE'] = True
basic_auth = BasicAuth(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

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