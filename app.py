from flask import Flask,render_template,request
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template('result.html')

@app.route("/regsuccess",methods=['POST',"GET"])
def regsuccess():
    if request.method == "POST":
        conn = sqlite3.connect('login.db')
        cur = conn.cursor()
        
        userid = str(request.form.get('email-phone'))
        password = request.form.get('password')

        try:
            cur.execute('''
                INSERT INTO logins VALUES (?,?)
            ''',(userid,password))
            res = {"Success":"registration success"}
        except:
            res = {"Error":"Failed to insert"}

        conn.commit()

        return render_template("success.html",data=res)
    else:
        res = {"Error":"Something wrong has happened"}
        return render_template("success.html",data=res)


@app.route("/success",methods=['POST',"GET"])
def login():
    if request.method == "POST":
        conn = sqlite3.connect('login.db')
        cur = conn.cursor()
        
        userid = str(request.form.get('email-phone'))
        password = request.form.get('password')

        cur.execute('''
            SELECT * FROM logins WHERE email_phone=?
        ''',(userid,))

        if (cur.fetchone() == None):
            res = {'result':'user not found'}
        else:
            res = {"result":"user found welcome"}

        return render_template("success.html",data=res),200
    else:
        return "Method Not Allowed!"