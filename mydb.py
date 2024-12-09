import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'weetikniet',
	)

#Prepare a cursor object

cursorObject = dataBase.cursor()

#Create a database

cursorObject.execute("CREATE DATABASE dcrm_database")

print('it work')