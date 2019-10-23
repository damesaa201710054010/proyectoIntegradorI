import mysql.connector as mysql
cnx = mysql.MySQLConnection(
    host = "evergreenadmin.mysql.database.azure.com",
    port = 3306,
    user = "evergreenadmin@evergreenadmin",
    password = "EAFITintegrador1",
    database= "evergreen",  
)