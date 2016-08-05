#!/Users/edelsonc/anaconda/bin/python
"""
This script runs the SharkCubed web applications

author: edelsonc
"""
import sys
import os
import webbrowser
import pycoil
import jinja2.ext
from flask import Flask, render_template, request, redirect

# checks if the file is running as an app or in normal Python and directs flask
# to the correct templates and static files
if getattr(sys, 'frozen', False):
    template = os.path.join(sys._MEIPASS, 'templates')
    static = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template, static_folder=static)
else:
    template = "./templates"
    static = "./static"
    app = Flask(__name__)


@app.route('/')
def home_page():
    """
    Renders the homepage of the application. This section contains all of the
    important information for the users of application, as well as the form to
    calculate the current desired for a certain magnetic field strength.
    """
    return render_template('SharkCube.html')

@app.route('/field_calc', methods=['POST'])
def field_calc():
    """
    This function waits for information from the form in the html homepage,
    calculated the specified current, and then redirects the user to the new
    page. It makes use of the plot_central_field and calculate_current
    functions located in the pycoil module. Static is passed to
    plot_central_field in order to make sure the plot is saved in the correct
    location.
    """
    B_field = float(request.form['field'])
    I, I_in = pycoil.calculate_current(B_field*10**-4)
    fig = pycoil.plot_central_field(I, static)
    return render_template('calculator.html', field=B_field,
        current=round(I,2), inner_current=round(I_in, 2), temp=fig)


@app.route('/quit', methods=['POST'])
def quit():
    """
    This function is used to shutdown the server. This was done because the
    intended audiance of SharkCube may not be used to working with the terminal
    as well as the fact that I find it a pain to always quit using ctrl+c.
    """
    if request.form["quit"] == "Quit Application":
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RunTimeError("Not running with the Werkzeug server")
        func()
        return 'Server has shutdown...feel free to close the window'

    else:
        return None
        

if __name__ == "__main__":
    url = 'http://127.0.0.1:5000'
    webbrowser.open(url)
    app.run()
