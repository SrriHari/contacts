# module to connect and communicate with MySQL database
import mysql.connector

HOSTNAME = "localhost"
USERNAME = "root"
USERPASSWORD = "orange55"
DATABASENAME = "addrbook"

def validateUser (login, password):
    bValidUser = False;
    
    # connect to database
    cnx = mysql.connector.connect(user=USERNAME, password=USERPASSWORD, host=HOSTNAME, port=3306, database=DATABASENAME)
    mycursor = cnx.cursor();
    mycursor.execute("SELECT * FROM applicationuser WHERE loginid=%s AND password=%s", (login, password))
    myresult = mycursor.fetchone();
    if (myresult):
        bValidUser = True;
    else:
        bValidUser = False;

    # close connection with database
    mycursor.close();
    cnx.close();

    return bValidUser

def registeruser(uid, login, passwor):
    iCount = 0;
    insQuery = "INSERT INTO APPLICATIONUSER (userid, loginid, password)"
    insQuery = insQuery + "VALUES ('" + uid + "','" + login + "','" + passwor + "')"
    
    # connect to database
    cnx = mysql.connector.connect(user=USERNAME, password=USERPASSWORD, host=HOSTNAME, port=3306, database=DATABASENAME)
    mycursor = cnx.cursor();
    mycursor.execute(insQuery)
    cnx.commit ();
    iCount = mycursor.rowcount
    print (iCount)
    mycursor.close ();
    cnx.close();
    #print (insQuery)
    return iCount
    
    
def addNewAddr (Name, FName, sClass, sSection, pContact, sContact, email):
    iCount = 0;
    insQuery = "INSERT INTO STUDENT (NAME, FNAME, CLASSNAME, SECTION, PARENTCONTACT, ALTERNATECONTACT, EMAIL)"
    insQuery = insQuery + "VALUES ('" + Name + "','" + FName + "','" + sClass + "','" + sSection + "','" + pContact + "','" + sContact + "','" + email + "')"
    
    # connect to database
    cnx = mysql.connector.connect(user=USERNAME, password=USERPASSWORD, host=HOSTNAME, port=3306, database=DATABASENAME)
    mycursor = cnx.cursor();
    mycursor.execute(insQuery)
    cnx.commit ();
    iCount = mycursor.rowcount
    print (iCount)
    mycursor.close ();
    cnx.close();
    #print (insQuery)
    return iCount
    
def searchStudentDetails (Name):
    if (len(Name.strip())) == 0:
        searchQuery = "select * from student"
    else:
        searchQuery = "select * from student where name like '" + Name.strip() + "%'"
    print (searchQuery);
    
    # connect to database
    cnx = mysql.connector.connect(user=USERNAME, password=USERPASSWORD, host=HOSTNAME, port=3306, database=DATABASENAME)
    mycursor = cnx.cursor();
    mycursor.execute(searchQuery)
    myresult = mycursor.fetchall();

    return myresult
    # close connection with database
    #  mycursor.close();
    # cnx.close();
    
def editSearchStudentDetails (Name):
    searchQuery = "select * from student where name = '" + Name.strip() + "'"
    print (searchQuery);
    
    # connect to database
    cnx = mysql.connector.connect(user=USERNAME, password=USERPASSWORD, host=HOSTNAME, port=3306, database=DATABASENAME)
    mycursor = cnx.cursor();
    mycursor.execute(searchQuery)
    myresult = mycursor.fetchone();

    return myresult
    # close connection with database
    #  mycursor.close();
    # cnx.close();
    
def deleteRecord (name):
    iCount = 0;
    delQuery = "DELETE FROM STUDENT WHERE name='" + name + "'"
    print (delQuery)
    
    # connect to database
    cnx = mysql.connector.connect(user=USERNAME, password=USERPASSWORD, host=HOSTNAME, port=3306, database=DATABASENAME)
    mycursor = cnx.cursor();
    mycursor.execute(delQuery)
    cnx.commit ();
    iCount = mycursor.rowcount
    print (iCount)
    mycursor.close ();
    cnx.close();
    #print (insQuery)
    return iCount
    
def updateAddress (recId, sName, pName, sClass, sec, pContact, sContact, email):
    iCount = 0;
    updQuery = "UPDATE STUDENT SET NAME='" + sName + "',FNAME='" + pName + "',CLASSNAME='" + sClass + "',SECTION='" + sec + "',PARENTCONTACT='" + pContact + "',ALTERNATECONTACT='" + sContact + "',EMAIL='" + email + "' where id=" + str(recId)
    print (updQuery)
    
    # connect to database
    cnx = mysql.connector.connect(user=USERNAME, password=USERPASSWORD, host=HOSTNAME, port=3306, database=DATABASENAME)
    mycursor = cnx.cursor();
    mycursor.execute(updQuery)
    cnx.commit ();
    iCount = mycursor.rowcount
    print (iCount)
    mycursor.close ();
    cnx.close();
    #print (insQuery)
    return iCount