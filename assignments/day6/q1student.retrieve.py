# import mysql connector
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host="127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_dataa",
    use_pure = True
)

# form a query to be executed in mysql
query = "select * from sensor_readings";

# create cursor to execute query
cursor = connection.cursor()

# execute qeury with cursor
cursor.execute(query)

# get required data from cursor
sensor_readings = cursor.fetchall()

# print students data
#print(students)

for iot_data in sensor_readings:
    print(iot_data)
    
# close the cursor
cursor.close()

# close connection with mysql server
connection.close()