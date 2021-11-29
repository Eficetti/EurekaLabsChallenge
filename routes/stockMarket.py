from flask import Flask, request, jsonify, blueprints
from requests import get
from flask_jwt_extended import jwt_required

# BLUEPRINT FOR STOCK MARKET #

market = blueprints.Blueprint('market', __name__)

# For it to work, the token obtained previously is required #
@market.route('/stockMarket', methods=['GET'])
@jwt_required
def stockMarket():
    # Gets the symbol recived and save it in a var(stockMarketSymbol) and create the request for it #
    data = request.get_json()
    stockMarketSymbol = data['Symbol']
    response = get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=FB&outputsize=compact&apikey=X86NOH6II01P7R24').json()

    # We get the keys to iterate between the dates to get the second day used to get the variation #
    date_keys = response['Time Series (Daily)'].keys()
    date = list(date_keys)

    # We save the 2 closes prices to get the variation #
    closePrice = response['Time Series (Daily)'][date[0]]['4. close']
    closedPricePrevious = response['Time Series (Daily)'][date[1]]['4. close']
    # The way to get the variation is to substract the last closing price from the previous one #
    variation = float(closePrice) - float(closedPricePrevious)
    # We return the data and the symbol #
    return jsonify({
        'Symbol': response['Meta Data']['2. Symbol'],
        'open': response['Time Series (Daily)'][date[0]]['1. open'],
        'high': response['Time Series (Daily)'][date[0]]['2. high'],
        'low': response['Time Series (Daily)'][date[0]]['3. low'],
        'close': response['Time Series (Daily)'][date[0]]['4. close'],
        'variation': variation
    })

        

