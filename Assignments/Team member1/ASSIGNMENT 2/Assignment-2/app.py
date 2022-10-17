# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.

from pickle import TRUE
from flask import Flask,render_template,request
import ibm_db
from prettytable import from_db_cursor
import ibm_db_dbi as db2
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=b1bc1829-6f45-4cd4-bef4-10cf081900bf.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32304;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=mpq60284;PWD=mXVCaT34r4sBlaHV;",'','')


# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/', methods =["GET", "POST"])
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
       
        c=f"insert INTO users(fname,email,pword) values('{name}','{email}','{password}')"
        ibm_db.exec_immediate(conn,c)
        return render_template('home.html')
    else:
        return render_template('index.html')

@app.route('/signin', methods =["GET", "POST"])
# ‘/’ URL is bound with hello_world() function.
def signin():
    if request.method == "POST":
        # name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        sql = "SELECT * FROM users"
        stmt = ibm_db.exec_immediate(conn, sql)
        while ibm_db.fetch_row(stmt) != False:
            if ibm_db.result(stmt, 1)==email and ibm_db.result(stmt, 2)==password:
                print('sucess')
                return render_template('home.html')
            else:
                print('nope')
                
        return render_template('signin.html')
            
                
            
     
            
            
        
        
    else:
        return render_template('signin.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')
    
# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
