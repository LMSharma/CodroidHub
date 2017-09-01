from flask import Flask,render_template
#imported render_template to render the html pages
app = Flask(__name__)

@app.route('/home')
def homePage():
   return render_template('home.html')

# your task is to make a route for login and return the login page

if __name__ == '__main__':
   app.run(debug = False)
