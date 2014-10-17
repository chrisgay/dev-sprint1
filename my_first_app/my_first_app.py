# This is whre you can start you python file for your week1 web app
# Name: 

from flask import Flask, flash #import Flask class (classes are templates for creating objects through inheritance, e.g., an child object inherits the traits (functions and attributes) of its parent class)
import flask.views
import os

app = Flask('my_first_app') # create instance of Flask object (a WSGI application to handle client requests)
# the my_first_app parameter is used to look-up resources in the file system.  In a single module (like our example) __name__ is also a correct value.   

app.secret_key = "Apple"

class View(flask.views.MethodView) :
    def get(self) : # HTTP Request to Get data from sever (in this case index.html file)
    		return flask.render_template('index.html') # use jinja templates, which are part of Flask, to render templates/index.html file, note file path in templates folder is default path

    def post(self) : # HTTP Request to Post (posting may involve a variety of tasks including update data displayed on page, sending and email etc.), post method triggered on form submission as declared in method property
    # Note - make sure there's no extra spaces at the end of each line or you'll throw an indention error
    	    result = eval(flask.request.form['expression']) #evaluate 'expression' data and read in output to result variable
            flask.flash(result) # create flash session to view result variable in loop defined in index.html
            return self.get() # update view of index.html with flash variable 

# evaluate text in 'expression' field from index.html file

app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])

app.run() #launch app object