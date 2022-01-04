import mysql.connector
import dbConfig as cfg

db = mysql.connector.connect(
    host = cfg.mysql['host'],
    user = cfg.mysql['user'],
    password = cfg.mysql['password'],
    database = cfg.mysql['database']
)
        
cursor = db.cursor()
#cursor.execute("CREATE DATABASE datarepresentation1")
#
#print("Database created")


# The SQL is creating the table inside the database and adding the columns needed.
sql = "CREATE TABLE stock (id INT NOT NULL AUTO_INCREMENT, product varchar(255), price float, quantity int, primary key (id))"
cursor.execute(sql)
db.commit()
print("Table created")

sql = "CREATE TABLE shoppingList (product varchar(255), quantity float)"
cursor.execute(sql)
db.commit()
print("Table created")


sql = "INSERT INTO stock (id,product,price,quantity) values(1,'coke can',1.80,20)"
cursor.execute(sql)
db.commit()
print("Value created")