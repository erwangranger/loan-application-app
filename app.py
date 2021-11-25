from flask import Flask, render_template, request
import sqlite3 as sql

counter = 0

conn = sql.connect('./database.db')
conn.execute('DROP TABLE IF EXISTS LoansTable')
conn.execute('CREATE TABLE LoansTable \
               (name TEXT, \
               LoanID TEXT, \
               LoanAmount TEXT, \
               CreditHistory TEXT, \
               ApprovalAnswer TEXT)'\
               )

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
      #ip_address = request.remote_addr

      try:
         nm = request.form['nm']
         LoanAmount = request.form['LoanAmount']
         CreditHistory = request.form['CreditHistory']
         # addr = request.form['add']
         # city = request.form['city']
         # pin = request.form['pin']

         LoanID =  "LO-" + str(counter).zfill(4)
         print (LoanID)
         # password = "rhodsdemo"
         ApprovalAnswer = '0'

         with sql.connect("database.db") as con:
            cur = con.cursor()

            # cur.execute("INSERT INTO LoansTable (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            # cur.execute("INSERT INTO LoansTable (name,ip,username) VALUES (?,?,?)",(nm,ip_address,username) )
            cur.execute("INSERT INTO LoansTable \
                           (name,\
                           LoanID,\
                           LoanAmount,\
                           CreditHistory,\
                           ApprovalAnswer) \
                           VALUES (?,?,?,?,?)" \
                           , \
                           (nm,\
                           LoanID,\
                           LoanAmount,\
                           CreditHistory,\
                           ApprovalAnswer) \
                           )
            # cur = con.cursor().execute('INSERT INTO LoansTable (name,addr,city,pin) VALUES (?,?,?,?)',(name,addr,city,pin) )

            con.commit()
            msg = "Record successfully added"

      except:
         con.rollback()
         msg = "error in insert operation"

      finally:
         return render_template("result.html",\
               msg = msg, \
               LoanID = LoanID, \
               nm = nm , \
               LoanAmount = LoanAmount , \
               CreditHistory = CreditHistory , \
               ApprovalAnswer = ApprovalAnswer)
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