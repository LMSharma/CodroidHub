from flask import Flask,render_template,request
#imported request
app = Flask(__name__)

@app.route('/home' ,methods = ['GET'])
def homePage():
   return render_template('home.html')

@app.route('/login' ,methods = ['POST'])
def loginPage():
   if request.method == "POST":
      return "Post method is called"

#Your task is:
   #1.return the login page if the user call the login route.
   #2.return success if the login page was submitted by the user using post method
   #till now don't bother about the page's field values,just return success.

if __name__ == '__main__':
   app.run(debug = False)
