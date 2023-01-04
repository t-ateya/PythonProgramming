

class Stock:
    def __init__(self, symbol,date_, open_, high, low, close, volume) -> None:
        self.symbol = symbol
        self.date = date_
        self.open = open_
        self.high = high
        self.low = low 
        self.close = close
        self.volume = volume 

class Trade:
    def __init__(self, symbol, timestamp, order, price, volume, commission) -> None:
        self.symbol = symbol
        self.timestamp = timestamp 
        self.order = order
        self.price = price 
        self.volume = volume 
        self.commission = commission 





"""
                        Exercise 1
    Given the above class, write a custom JSONEncoder class to serialize dictionaries that contain instances of these particular classes. Keep in mind
    that you will want to deserialize the data too-so you will you will need some techniques to indicate the object type in your serialization

    For example you may hve an object such as this one that needs to be serialized

    Hint: You can modify the classes if you need to

"""
from datetime import date, datetime
from decimal import Decimal

activity = {
    "quotes": [
        Stock('TSLA', date(2018, 11, 22), Decimal('338.19'), Decimal('337.68'), Decimal('337.68'), Decimal('338.19'), 365_607),
        Stock('AAPL', date(2018, 11, 22), Decimal('177.25'), Decimal('176.64'), Decimal('176.78'), Decimal('338.19'), 3_699_184),
        Stock('MSFT', date(2018, 11, 22), Decimal('103.48'), Decimal('103.08'), Decimal('103.07'), Decimal('103.11'), 4_493_689)

    ],
    "trades": [
        Trade('TSLA', datetime(2018, 11, 22, 10, 5,12), 'buy', Decimal('338.25'), 100, Decimal('9.99')),
        Trade('AAPL', datetime(2018, 11, 22, 10, 5,5), 'sell', Decimal('177.01'), 20, Decimal('9.99'))
        ]
}


"""
                Exercise 2
    Write code to reverse the the serialization you just created. Write a custom decoder that can deserialize  a JSON structure containing Stock
    and Trade objections

                Exercise 3
    Do the same serialization and deserialization but using Marsmallow
    
"""
        
        #Exercise 1 Solution
class Stock:
    def __init__(self, symbol,date, open_, high, low, close, volume) -> None:
        self.symbol = symbol
        self.date = date
        self.open = open_
        self.high = high
        self.low = low 
        self.close = close
        self.volume = volume 

    def as_dict(self):
        return dict(
            symbol = self.symbol,
            date = self.date,
            open = self.open,
            high = self.high,
            low = self.low,
            close = self.low,
            volume = self.volume
        )

    def __eq__(self, other) -> bool:
        return isinstance(other, Stock) and other.as_dict() == self.as_dict()



class Trade:
    def __init__(self, symbol, timestamp, order, price, volume, commission) -> None:
        self.symbol = symbol
        self.timestamp = timestamp 
        self.order = order
        self.price = price 
        self.volume = volume 
        self.commission = commission 

    def as_dict(self):
        return dict(
            symbol = self.symbol,
            timestamp = self.timestamp,
            order = self.order, 
            price = self.price, 
            volume = self.volume, 
            commission= self.commission

        )


    def __eq__(self, other) -> bool:
        return isinstance(other, Trade) and other.as_dict() == self.as_dict()

"""
from json import JSONEncoder, dumps

class CustomEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Stock) or isinstance(obj, Trade):
            result = obj.as_dict()
            result["object"] = obj.__class__.__name__
            return result
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%S')
        elif isinstance(obj, Decimal):
            return str(obj)
        else:
            super().default(obj)

encoded = dumps(activity, cls=CustomEncoder, indent=2)
print(encoded)

def decode_stock(d):
    s = Stock(
        d['symbol'],
        datetime.strptime(d['date'], '%Y-%m-%d').date(),
        Decimal(d['open']),
        Decimal(d['high']),
        Decimal(d['low']),
        Decimal(d['close']),
        int(d['volume']),
    )
    return s

d = {
    "symbol": "MSFT",
    "date":"2018-11-22",
    "open": "103.25",
    "high": "103.48",
    "low": "103.07",
    "close": "103.11",
    "volume": 4493689,
    "object": "Stock"
}

s = decode_stock(d)

def decode_trade(d):
    t = Trade(d["symbol"],
        datetime.strptime(d['timestamp'], '%Y-%m-%dT%H:%M:%S'),
        d['order'],
        Decimal(d['price']),
        int(d['volume']),
        Decimal(d['comission'])
    )
    return t


def decode_financials(d):
    object_type = d.get("object", None)
    if object_type == "Stock":
        return decode_stock(d)
    elif object_type == "Trade":
        return decode_trade(d)
    else:
        return d 
"""



#Exercise 2 Solution
"""
from json import JSONDecodeError, loads

class CustomDecoder(JSONDecodeError):
    def decode(self, arg):
        data = loads(arg)
        return self.parse_financial(data)
    def parse_financial(self, obj):
        if isinstance(obj, dict):
            obj = decode_financials(obj)
            if isinstance(obj, dict):
                for key, value in obj.items():
                    obj[key] = self.parse_financial(value)
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                obj[index] = self.parse_financial(item)
        else:
            return obj 

encoded = dumps(activity, cls=CustomEncoder, indent=2)
decoded = loads(encoded, cls=CustomDecoder)
activity == decoded
"""



#Exercise 3 Solution

from marshmallow import Schema, fields

class StockSchema(Schema):
    symbol = fields.Str()
    date = fields.Date()
    open = fields.Decimal(as_string=True)
    high = fields.Decimal(as_string=True)
    low = fields.Decimal(as_string=True)
    close = fields.Decimal(as_string=True)
    volume = fields.Integer()

stock = StockSchema().dumps(Stock('TSLA', date(2018, 11, 22), Decimal('338.19'), Decimal('337.68'), Decimal('337.68'), Decimal('338.19'), 365_607))
#print(stock)
from marshmallow import post_load

class TradeSchema(Schema):
    symbol = fields.Str()
    timestamp = fields.DateTime()
    order = fields.Str()
    price = fields.Decimal(as_string=True)
    commission = fields.Decimal(as_string=True)
    volume = fields.Integer()

    @post_load
    def make_trade(self, data):
        return Trade(**data)





trade = TradeSchema().dumps(Trade('AAPL', datetime(2018, 11, 22, 10, 5,5), 'sell', Decimal('177.01'), 20, Decimal('9.99')))
#print(trade)
class ActiviySchema(Schema):
    quotes = fields.Nested(StockSchema, many=True)
    trades = fields.Nested(TradeSchema, many=True)

result = ActiviySchema().dumps(activity, indent=2).data

print(type(result))
print(result)

activity_deser = ActiviySchema().loads(result).data 

