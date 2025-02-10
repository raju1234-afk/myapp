# Task1: Demo flask application
# Date:21/03/2024
# File Name: app.py
# Author_Name: Write the developer’s name(M. Venkateswarl)
# Import the Flask and OS python modules 
from flask import Flask, render_template
import os
# Create the application object by calling Flask constructor
app = Flask(__name__)
# map the url request to the respone
@app.route('/')
# define the function to generate the response for the request.
def home(): 
    #generate html response to the user from templates folder.
  return render_template('Demo.html')
# Control and start the execution of the application with __name__ dunder method which is    # always has the fixed value __main__
if __name__ == "__main__":
#get the port number of the web server as 5000 using os module and assign the value to 
# port variable
    port = int(os.environ.get('PORT', 5000))
# Run the application by calling the run method which invokes the execution of web server
    app.run(debug=True, host='0.0.0.0', port=port)
