#Author: Shane Rylands
#Student id: G00387904

#File contains the RESTful API which uses flask to make my database available online

#------------------------
#import flask and make shopDAO available

from flask import Flask, url_for, request, redirect, abort, jsonify
from shopDao import shopDao

#you direct the server to where the web pages are held
app = Flask(__name__, static_url_path='', static_folder='staticpages')


#------------------------
# index

@app.route('/')
def index():
    return "Hello World\n"
#------------------------

#------------------------
# Get all

@app.route('/stock')
def getAll():
    return jsonify(shopDao.getAll())
#------------------------

#------------------------
# Find by ID

@app.route('/stock/<int:id>')
def findById(id):   
    return jsonify(shopDao.findById(id))
#------------------------

#------------------------
# Create

# Troubleshooting: curl -X POST -d "{\"product\":\"apple\",\"price\":\"0.80\",\"quantity\":30}" -H Content-Type:application/json http://127.0.0.1:5000/stock
# floating points needs to be treated as strings in JSON
@app.route('/stock', methods=['POST'])
def create():
    
    # error handling for when no json
    if not request.json:
        abort(400)
    
    stockItem = {
        "product":request.json["product"],
        "price":request.json["price"],
        "quantity":request.json["quantity"]
    }                                                  
    return jsonify(shopDao.create(stockItem))

#   return "served by Create "
#------------------------

#------------------------
# Update

# Troubleshooting: curl -X PUT -d "{\"product\":\"apple\",\"price\":\"0.80\",\"quantity\":40}" -H Content-Type:application/json http://127.0.0.1:5000/stock/2

@app.route('/stock/<int:id>', methods=['PUT'])
def update(id):
    foundStockItem = shopDao.findById(id)   
    #error handling for find by Id
    if foundStockItem == {}:
        return jsonify({}),404
    currentStockItem = foundStockItem
    if 'product' in request.json:
        currentStockItem['product'] = request.json['product']
    if 'price' in request.json:
        currentStockItem['price'] = request.json['price']
    if 'quantity' in request.json:
        currentStockItem['quantity'] = request.json['quantity']
    shopDao.update(currentStockItem)
          
    return jsonify(currentStockItem)
#------------------------

#------------------------
# Delete

# Troubleshooting: curl -X DELETE http://127.0.0.1:5000/stock/5

@app.route('/stock/<int:id>', methods=['DELETE'])
def delete(id):
    #error handling IF NO BOOK EXISTS
#    foundStockItem = shopDao.findById(id)
#    if foundStockItem == {}:
#        return jsonify({}),404
    shopDao.delete(id)
    return jsonify({"done":True})

#------------------------

#------------------------
#2nd DB tabel

# curl -X POST -d "{\"product\":\"apple\",\"quantity\":5}" -H Content-Type:application/json http://127.0.0.1:5000/shoppingList

@app.route('/shoppingList', methods=['POST'])
def add():
    
    # error handling for when no json
    if not request.json:
        abort(400)
    
    shoppingItem = {
        "product":request.json["product"],
        "quantity":request.json["quantity"]
    }                                                  
    return jsonify(shopDao.add(shoppingItem))
#------------------------



#------------------------
#Main method

if __name__ == "__main__":
    print("in if")
    app.run(debug=True) 
    
#------------------------
    
    
#To Do 
#1. Upload Repo
#2. Fix DB so it auto_increments with continuous id
#3. Add new DB table
#4. message if id already exists in databases
#5. back button for create
#6. Delete not working 
#7. add euro sign 
#8. ajax to reset auto increment 
#9. change creat update heading = grey out when not used 
