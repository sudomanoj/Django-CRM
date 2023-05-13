import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    
)

# Prepare Cursor Object

cursorObject = dataBase.cursor()

# Create a Database
cursorObject.execute('CREATE DATABASE elderco')

print('Database Created!')