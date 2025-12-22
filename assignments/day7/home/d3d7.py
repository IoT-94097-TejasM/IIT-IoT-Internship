# import Flask class from flask module
from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

# create a server usinf Flask
server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.route('/home_readings', methods=['POST'])
def create_student():
    # extract data form form
    id = request.get_json().get('id')
    temperature = request.get_json().get('temperature')
    light_status = request.get_json().get('light_status')
    fan_status = request.get_json().get('fan_status')

    # create a query to add student into table
    query = f"insert into home_readings values({id}, '{temperature}', '{light_status}', '{fan_status}');"

    #print(query)
    #execute the query 
    executeQuery(query=query)

    return "home_data is added successfully"

@server.route('/home_readings', methods=['GET'])
def retrieve_students():
    # create a select query
    query = "select * from home_readings;"

    # execute select query
    data = executeSelectQuery(query=query)

    return f"home_readings : {data}"

@server.route('/home_readings', methods=['PUT'])
def update_student():
    # extract data form form
    id = request.get_json().get('id')
    fan_status = request.get_json().get('fan_status')

    # create a query
    query = f"update home_readings SET fan_status = '{fan_status}' where id = '{id}';"

    # execute the query
    executeQuery(query=query)

    return "email is updated successfully"

@server.route('/home_readings', methods=['DELETE'])
def delete_student():
    # extract data form form
    light_status = request.get_json().get('light_status')

    # create a query
    query = f"delete from home_readings where light_status = '{light_status}';"

    # execute the query
    executeQuery(query=query)

    return "home data is deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)