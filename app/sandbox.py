# Code needs to be run in external terminal cd ~/Documents/Systems/Gem/gem, python3 sandbox.py

# Current sandbox dependencies
from bs4 import BeautifulSoup # bit.ly/2a8B2K3, bit.ly/2L45ESt
from requests import get

# Test document (underlying: 14000/11, derivative: 50400/11*5.91)
position = {
"entries_underlying": {
    "1":
        {
        "date": "2019-04-17 09:12:22",
        "quantity": 500,
        "price": 10
        },
    "2":
        {
        "date": "2019-04-23 09:33:17",
        "quantity": 600,
        "price": 15
        }
    },
"entries_derivative": {
    "1":
        {
        "date": "2019-04-17 09:12:22",
        "quantity": 1800,
        "price": 12.50
        },
    "2":
        {
        "date": "2019-04-23 09:33:17",
        "quantity": 1800,
        "price": 15.50
        }
    },
"quantity_multiplier": 5.91
}

# Working multiplication loop
instrument_exposure = []
instrument_multiplier = 0

# checks if derivative is used
if position['quantity_multiplier'] > 1:
    instrument_multiplier = position['quantity_multiplier']
    for k, v in position['entries_derivative'].items():
        calculation = (v['price'] * v['quantity']) / 11 # swap to currency converter module
        instrument_exposure.append(calculation)
# if not, then underlying
else:
    instrument_multiplier = 1
    for k, v in position['entries_underlying'].items():
        calculation = (v['price'] * v['quantity']) / 11 # swap to currency converter module
        instrument_exposure.append(calculation)

print(sum(instrument_exposure) * instrument_multiplier)


# Scrape current price
# https://www.tradingview.com/symbols/NYMEX-CL1%21/, tv-symbol-price-quote__value

