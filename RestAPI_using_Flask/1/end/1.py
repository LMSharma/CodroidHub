#importing Flask class from flask module
from flask import Flask

#making an instance of Flask class
app = Flask(__name__)


# @app.route is the decorator which is used to make a url
@app.route('/hello')         #here '/hello' is the url
#function relating this url
def hello_world():
    return 'Hello, World!'

# create a new route here for home page i.e url should be '/' only

@app.route('/')         
#function relating this url
def home():
    return """
            <html>
                <head>
                    <title>Hello World with React</title>
                </head>
                <body>
                    <h1>This is my home page</h1>
                </body>
            </html>
            """

if __name__ == "__main__":
    app.run(debug = False)
