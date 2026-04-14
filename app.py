from flask import Flask,request,render_template,redirect
import mysql.connector
import os

app = Flask(__name__) # this will start web application

#Connect to Database

db = mysql.connector.connect(
    host=os.getenv("mysql.railway.internal"),
    user=os.getenv("root"),
    password=os.getenv("bGBhFyrjVNmbjmJFEWADAeqStJjPDfvOMYSQLPASSWORD"),
    database=os.getenv("railway"),
    port=int(os.getenv("3306"))
)

#like a tool to run SQL queries
cursor = db.cursor()

#this is our input form page
@app.route("/")
def form():
    return render_template("form.html")

#When user clicks Submit button, this runs
#POST means → sending data (form data)

@app.route("/submit",methods=["POST"])
def submit():
    name = request.form["name"]
    phone = request.form["phone"]
    purpose = request.form["purpose"]
    query = "INSERT INTO visitors(name,phone,purpose) VALUES (%s,%s,%s)"
    values = (name,phone,purpose)

    cursor.execute(query,values)

    db.commit()

    return redirect("/")    

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug=True)
