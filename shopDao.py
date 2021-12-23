import mysql.connector

#classes start with capitals in python need to change 
class shopDao:
    db = ''
    
    # https://docs.python.org/3/tutorial/classes.html
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'datarepresentation'
        )
        
        
    def create(self, stockItem):
        cursor = self.db.cursor()
        sql = "insert into stock( product, price, quantity) values ( %s, %s, %s)"
        values = [
                  stockItem['product'],
                  stockItem['price'],
                  stockItem['quantity']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid
        
    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from stock'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
#       print(results) 
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)       
        return returnArray  
    
    def findById(self, id):
        cursor = self.db.cursor()
#       needs to be %s not %d as it is a json that is returned 
        sql = 'select * from stock where id = %s'
        values = [id]
        cursor.execute(sql, values)
        result = cursor.fetchone()        
        return self.convertToDict(result)   
    
    def update(self, stockItem):
        cursor = self.db.cursor()
        sql = 'update stock set product = %s, price = %s, quantity = %s where id = %s'
        values = [
                  stockItem['product'],
                  stockItem['price'],
                  stockItem['quantity'],
                  stockItem['id']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return stockItem
#        return cursor.lastrowid

#database doesnt update 
    def delete(self, id):
        cursor = self.db.cursor()
        sql = 'delete from stock where id = %s'
        values = [id]
        cursor.execute(sql, values)
        self.db.commit()
        return{}
    
    def convertToDict(self,result):
        colnames = ['id','product','price','quantity']
        stock = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                stock[colName] = value
        return stock

    
#--------

    def add(self, shoppingItem):
        cursor = self.db.cursor()
        sql = "insert into shoppingList( product, quantity) values ( %s, %s)"
        values = [
                  shoppingItem['product'],
                  shoppingItem['quantity']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    
shopDao = shopDao()