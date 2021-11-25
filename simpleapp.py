from flask import Flask, render_template, request

app = Flask(__name__)

counter = 0

@app.route('/')
def home():
   return render_template('index.html')

if __name__ == '__main__':
   app.run()

@app.route("/")
def main():

    ip_address2 = request.environ['REMOTE_ADDR']

    # return "<h1> Hey!\n you are coming from IP " + ip_address1 + " and you have been assigned the following student" + counter_3 + "</h1>"
    return render_template('index.html')

@app.route('/response', methods=['POST'])
def response():
    global counter
    counter += 1
    ## counter with 3 digits and leading zeros
    counter_3 = str( str(counter).zfill(3) )

    fname = request.form.get("fname")
    lname = request.form.get("lname")
    FullName = fname + " " + lname
    ip_address1 = request.remote_addr

    return render_template("index.html", FullName=FullName, counter_3=counter_3 , ip_address1=ip_address1 )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
