from flask import Flask, render_template, request
import sqlite3 as sql

counter = 0

conn = sql.connect('./database.db')
conn.execute('DROP TABLE IF EXISTS LoansTable')
conn.execute('CREATE TABLE LoansTable (name TEXT, LoanID TEXT, password TEXT, ip TEXT)')

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()


app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/newloan')
def new_student():
   return render_template('newloan.html')

@app.route('/addloan',methods = ['POST', 'GET'])
def addloan():
   if request.method == 'POST':
      global counter
      counter += 1
      ip_address = request.remote_addr

      try:
         nm = request.form['nm']
         # addr = request.form['add']
         # city = request.form['city']
         # pin = request.form['pin']

         LoanID =  "LO00" + str(counter)
         print (LoanID)
         password = "rhodsdemo"

         with sql.connect("database.db") as con:
            cur = con.cursor()

            # cur.execute("INSERT INTO LoansTable (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            # cur.execute("INSERT INTO LoansTable (name,ip,username) VALUES (?,?,?)",(nm,ip_address,username) )
            cur.execute("INSERT INTO LoansTable (name,LoanID,password,ip) VALUES (?,?,?,?)" , (nm,LoanID,password,ip_address) )
            # cur = con.cursor().execute('INSERT INTO LoansTable (name,addr,city,pin) VALUES (?,?,?,?)',(name,addr,city,pin) )

            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"

      finally:
         return render_template("result.html",msg = msg, LoanID = LoanID, nm = nm )
         con.close()

@app.route('/listloans')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from LoansTable")

   rows = cur.fetchall();
   return render_template("listloans.html",rows = rows)



# if __name__ == '__main__':
#    app.run(debug = True)
if __name__ == '__main__':
    app.run(host='0.0.0.0')