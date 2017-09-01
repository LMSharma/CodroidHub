from flask import Flask,render_template,request,jsonify
#imported jsonify
app = Flask(__name__)

@app.route('/home' ,methods = ['GET'])
def homePage():
   return render_template('home.html')

@app.route('/login' ,methods = ['POST'])
def loginPage():
   if request.method == "POST":
      return jsonify(msg = "Post method is called")


@app.route('/form' ,methods = ['POST'])
def submitForm():
   if request.method == "POST":
      name        = str(request.form['userName'])
      address     = str(request.form['address'])
      contact     = str(request.form['contact'])
      emailId     = str(request.form['emailId'])
      print(name,address,contact,emailId)
      return jsonfiy(user = name)
   else:
      return "Hello"



#Your task is:
   #1.return the login page if the user call the login route.
   #2.return name of the user in json format if the login page was submitted by the user using post method.
   #else return the login page.


if __name__ == '__main__':
   app.run(debug = False)
