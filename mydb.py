import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'd8l2t5b5',

	)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE yelasbookstack")

print("All Done!")