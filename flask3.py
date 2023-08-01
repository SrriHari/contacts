from flask import Flask, render_template, request
import os
import dbServices

app = Flask(__name__)

@app.route('/home', methods = ['POST'])
def home():
    if request.method == 'POST':
        user = request.form['uname']
        password = request.form['upassword']
        if (dbServices.validateUser (user, password) == True):
            return render_template('layout2.html')
        else:
            imgPath = os.path.join('static', 'images')
            app.config ['img'] = imgPath;
            logoImg = os.path.join(app.config['img'], 'login.jpg');
            msg = "Invalid Credentials"
    return render_template('login1.html', user_image = logoImg, message = msg)

@app.route('/home/registeruser')
def registeruser():
    return render_template('loginregist.html')

@app.route('/home/register')
def registeruser1():
    if request.method == 'POST':
        user = request.form['uname']
        password = request.form['upassword']
        uid = request.form['uid']
        dbServices.registeruser(uid, user, password);
    #return render_template('login1.html',data=Todos.query.all())
    return render_template('students.html')


@app.route('/')
def login():
    imgPath = os.path.join('static', 'images')
    app.config ['img'] = imgPath;
    logoImg = os.path.join(app.config['img'], 'login.jpg');
    return render_template('login1.html', user_image = logoImg)

@app.route('/students/create')
def createaddress():
	return render_template('createaddress.html')

@app.route('/Students/search')
def searchStudent():
	return render_template('searchStudent.html')

@app.route('/students/searchResult', methods = ['POST'])
def searchResult():
    iFlag = True;
    nm = request.form['txtName']
    result = dbServices.searchStudentDetails (nm)
    print (result)
    #if (result):
    #    iFlag = True;
    #print (iFlag);
    return render_template('searchStudent.html', results = result, Flag = iFlag)

@app.route('/Students/edit')
def editStudentRecord():
    return render_template('editStudentRecord.html')
    
@app.route('/Students/delete')
def deleteStudentRecord():
    return render_template('deleteStudentRecord.html')

@app.route('/students/deleteRecord', methods = ['POST'])
def deleteRecord():
    name = request.form['txtName']
    result = dbServices.deleteRecord (name)
    if (result == 0):
        message = "No name Found!"
    else:
        message = "Record deleted"        
    return render_template('deleteStudentRecord.html', user_message = message)
 
@app.route('/students/editSearchResult', methods = ['POST'])
def editSearchResult():
    iFlag = True;
    nm = request.form['txtName']
    result = dbServices.editSearchStudentDetails (nm)
    print (result)
    if (result):
        iFlag = True;
    print (iFlag);
    return render_template('editStudent.html', results = result, Flag = iFlag)
    
@app.route('/students/saveEditedRec', methods = ['POST'])
def updateStudentAddress():
    recId = request.form['txtStudentno']
    sName = request.form['txtName']
    pName = request.form['txtParent']
    sClass = request.form['txtClass']
    sec = request.form['txtSection']
    pContact = request.form['txtContact']
    sContact = request.form['txtAltContact']
    email = request.form['txtEmailID']
    retMsg = dbServices.updateAddress (recId, sName, pName, sClass, sec, pContact, sContact, email);
    if (retMsg > 0):
        msg = str(retMsg) + " Record Successfully Updated...";
    else:
        msg = "Error on adding ....."
    return render_template('editStudent.html', message = msg);
    
@app.route('/students/createnew', methods = ['POST'])
def addNewAddress():
    nm = request.form['txtName']
    fname = request.form['txtFName']
    className = request.form['optClass']
    section = request.form['optSection']
    pContact = request.form['txtContact']
    sContact = request.form['txtAltContact']
    email = request.form['txtEmailID']
    retMsg = dbServices.addNewAddr (nm, fname, className, section, pContact, sContact, email);
    if (retMsg > 0):
        msg = str(retMsg) + " Record Successfully added...";
    else:
        msg = "Error on adding ....."
    #print (nm, fname, className, section, pContact, sContact, email);
    return render_template('createaddress.html', message = msg)

@app.route('/students')
def students():
	return render_template('students.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.form
	return render_template("result.html", result = result)

### About link
@app.route('/about')
def about():
	return render_template("about.html")


if __name__ == '__main__':
	app.run(debug = True)
