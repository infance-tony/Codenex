#pip install mysql-connector-python
from mysql.connector import connection

dict = {
  'user': 'root',
  'host': 'localhost',
  'database': 'College'
}
# Connecting to the server
mydb = connection.MySQLConnection(**dict)

print(conn)

# Disconnecting from the server
mydb.close()
print("Connection closed.")