from yahoo_finance import Share
yahoo = Share('AMZN')
print(yahoo.get_price())
# print (yahoo.get_historical('2014-04-25', '2014-04-29'))
