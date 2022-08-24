import sqlite3


class ItemModel:
    def __int__(self, _name, _price):
        self.name = _name
        self.price = _price

    def json(self):
        return {"name": self.name, "price": self.price}


    def insert_item(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ? )"
        cursor.execute(query, (self.name, self.price))

        connection.commit()
        connection.close()

    @classmethod
    def find_item(cls, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            #return cls(row[0], row[1])
            return cls(*row)      #argument unpacking


    def update(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "UPDATE items SET price=? WHERE name=? "
        cursor.execute(query, (self.price, self.name))

        connection.commit()
        connection.close()