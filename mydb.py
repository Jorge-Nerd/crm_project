import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'sanches18',
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# prepare a database
cursorObject.execute('CREATE DATABASE sagacine')

print('All done')