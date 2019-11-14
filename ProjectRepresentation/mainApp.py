from random import randint
from time import strftime
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'

class ReusableForm(Form):
    text = TextField('Name:', validators=[validators.required()])


@app.route("/", methods=['GET', 'POST'])
def user_detail():
    form = ReusableForm(request.form)

    if request.method == 'POST':
        text=request.form['text']
        password=request.form['password']
        
        if form.validate() and len(password) > 0:
            flash('Your message has been encrypted successfully.')
        else:
            flash('Error: All Fields are Required')

    return render_template('mainPage.html', form=form)

if __name__ == "__main__":
    app.run()