import mysql.connector

# connect to database
cnx = mysql.connector.connect(user="root", password="orange55", host="localhost", port=3306, database="addrbook")

mycursor = cnx.cursor();
mycursor.execute("SELECT * FROM applicationuser")
myresult = mycursor.fetchall();
for rec in myresult:
    print("%d  %s" % (rec[0],rec[1]));

# close connection with database
mycursor.close();
cnx.close();

