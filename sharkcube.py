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

template_folder = os.path.join(sys._MEIPASS, 'templates')
static = os.path.join(sys._MEIPASS, 'static')
app = Flask(__name__, template_folder=template_folder, static_folder=static)


@app.route('/')
def home_page():
    """Renders the homepage of the application"""
    return render_template('SharkCube.html')

@app.route('/field_calc', methods=['POST'])
def field_calc():
    """Render the page calculated magnetic field strength"""
    B_field = float(request.form['field'])
    I, I_in = pycoil.calculate_current(B_field*10**-4)
    pycoil.plot_central_field(I)
    return render_template('calculator.html', field=B_field,
        current=round(I,2), inner_current=round(I_in, 2))


@app.route('/quit', methods=['POST'])
def quit():
    if request.form["quit"] == "Quit Application":
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RunTimeError("Not running with the Werkzeug server")
        func()
        return 'Server shutting down...'

    else:
        return None
        

if __name__ == "__main__":
    url = 'http://127.0.0.1:5000'
    webbrowser.open(url)
    app.run()
