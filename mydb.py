import mysql.connector

database = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Rabbuni@15',
	auth_plugin = 'mysql_native_password',
	)

#prepare  cursor object
cursorObject = database.cursor()

#create a database
cursorObject.execute("CREATE DATABASE archangel")


print("All Done!")