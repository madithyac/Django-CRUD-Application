import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'

)

#prepare cursor object
cursorObject = dataBase.cursor()

#Create database
cursorObject.excute("CREATE DATBASE database_db")
print("All Done")
