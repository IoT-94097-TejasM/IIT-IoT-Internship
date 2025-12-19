# import Flask class from flask module
from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

# create a server usinf Flask
server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.route('/sensor_readings', methods=['POST'])
def create_sensor_readings():
    # extract data form form
    id = request.get_json().get('id')
    temperature = request.get_json().get('temperature')
    humidity = request.get_json().get('humidity')
    #location = request.get_json().get('location')
    from datetime import datetime
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 

    # create a query to add student into table
    query = f"insert into sensor_readings values({id}, {temperature}, {humidity}, '{timestamp}');"

    #print(query)
    #execute the query 
    executeQuery(query=query)

    return "sensor reading is added successfully"

@server.route('/sensor_readings', methods=['GET'])
def retrieve_sensor_readings():
    # create a select query
    query = "select * from sensor_readings;"

    # execute select query
    data = executeSelectQuery(query=query)

    return f"sensor_readings   : {data}"

@server.route('/sensor_readings', methods=['PUT'])
def update_sensor_readings():
    # extract data form form
    id = request.get_json().get('id')
    temperature = request.get_json().get('temperature')
    humidity = request.get_json().get('humidity')
    # create a query
    query = f"update sensor_readings SET temperature = {temperature}, humidity = {humidity} where id = {id};"

    # execute the query
    executeQuery(query=query)

    return "sensor reading   is updated successfully"

@server.route('/sensor_readings', methods=['DELETE'])
def delete_sensor_readings():
    # extract data form form
    id = request.get_json().get('id')

    # create a query
    query = f"delete from sensor_readings where id = {id};"

    # execute the query
    executeQuery(query=query)

    return "sensor reading is deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)