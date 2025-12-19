# import Flask class from flask module
from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

# create a server usinf Flask
server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.route('/soil_moisture', methods=['POST'])
def create_soil_moisture():
    # extract data form form
    id = request.get_json().get('id')
    moisture = request.get_json().get('moisture')
    #humidity = request.get_json().get('humidity')
    #location = request.get_json().get('location')
    from datetime import datetime
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 

    # create a query to add student into table
    query = f"insert into soil_moisture values({id}, {moisture}, '{timestamp}');"

    #print(query)
    #execute the query 
    executeQuery(query=query)

    return "sensor reading is added successfully"

@server.route('/soil_moisture', methods=['GET'])
def retrieve_soil_moisture():
    # create a select query
    query = "select * from soil_moisture;"

    # execute select query
    data = executeSelectQuery(query=query)

    return f"soil_moisture   : {data}"

@server.route('/soil_moisture', methods=['PUT'])
def update_soil_moisture():
    # extract data form form
    id = request.get_json().get('id')
    moisture = request.get_json().get('moisture')
    # create a query
    query = f"update soil_moisture SET moisture = {moisture} where id = {id};"

    # execute the query
    executeQuery(query=query)

    return "sensor reading   is updated successfully"

@server.route('/soil_moisture', methods=['DELETE'])
def delete_soil_moisture():
    # extract data form form
    id = request.get_json().get('id')

    # create a query
    query = f"delete from soil_moisture where id = {id};"

    # execute the query
    executeQuery(query=query)

    return "sensor reading is deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)