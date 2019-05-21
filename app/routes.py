from flask import render_template, request, redirect, url_for # request, redirect_url, url_for and bson line not part of my code
from flask_basicauth import BasicAuth
from bson import ObjectId
from datetime import datetime
from app import app

db_connection = "mongodb+srv://dev01:KKizYFNtsboBQAf2@asa01-jeqsk.mongodb.net/admin"
from pymongo import MongoClient
client = MongoClient(db_connection)
db = client.asa_db_01
quandl_key = 'XzsKV7TBwpzcgjXj4RD3'
import quandl
quandl.ApiConfig.api_key = quandl_key

app.config['BASIC_AUTH_USERNAME'] = 'hello'
app.config['BASIC_AUTH_PASSWORD'] = 'there'
app.config['BASIC_AUTH_FORCE'] = True
basic_auth = BasicAuth(app)

import feedparser
BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"


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

@app.route('/create-ticket')
def create_ticket():
    return render_template("ticket.html")

@app.route('/edit-ticket')
def edit_ticket():
    return render_template("ticket.html")

@app.route('/close-ticket')
def close_ticket():
    return render_template("ticket.html")

@app.route("/feed")
def get_news():
     feed = feedparser.parse(BBC_FEED)
     first_article = feed['entries'][0]
     return """<html>
       <body>
           <h1> BBC Headlines </h1>
           <a href="{3}" target="_blank"><b style="color:#000">{0}</b></a> <br/>
           <i>{1}</i> <br/>
           <p>{2}</p> <br/>
       </body>
   </html>""".format(first_article.get("title"), first_article.
   get("published"), first_article.get("summary"), first_article.get("link"))


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