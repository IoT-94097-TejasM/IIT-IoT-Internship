# import mysql connector
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_dataa",
    use_pure = True
)

# form a query to be executed
id = input("Enter id whose temperature to be updated : ")
temperature = input("Enter new temperature : ")

query = f"update sensor_readings SET temperature = '{temperature}' where id = '{id}';"

# create a cursor to execute a query
cursor = connection.cursor()

# execute a query
cursor.execute(query)

# commit your changes on mysql server
connection.commit()

# close the cursor
cursor.close()

# close the connection with mysql server
connection.close()