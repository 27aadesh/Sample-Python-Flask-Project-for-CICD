
# Importing flask module in the project is mandatory 
# An object of Flask class is our WSGI application. 
from flask import Flask 
  
# Flask constructor takes the name of  
# current module (__name__) as argument. 
app = Flask(__name__) 
  
# The route() function of the Flask class is a decorator,  
# which tells the application which URL should call  
# the associated function. 
@app.route('/') 
# ‘/’ URL is bound with hello_world() function. 
def hello_world(): 
    return '<h1>Hello World from CloudDevOpsTV!<h1><br /><h4>If you see this message that means you have successfully deployed the code</h4>'
@app.route('/users')
def users():
    return '/Users Path Invoked.'
      
# main driver function 
if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run() 