<h1>Welcome to <i>Shark<sup>3</sup></i></h1>
<p>Shark<sup>3</sup> is a mac application that runs a local flask web application. It provides basic information about the 8 coil Helmholtz array located in the New College of Florida Pritzker Marine Lab. Additionally, it has a current calculator, which calculates the required current needed in the coils of the array in order to create a local magnetic field of a designed strength. The purpose of <i>Shark<sup>3</sup></i> is to easily allow Marine Biology students at New College of Florida to calculate the current they'd need to create magnetic field for behavioral experiments, as well as provide information about the design of <i>Shark<sup>3</sup></i>.</p>

<h2>Getting Started</h2>
<p><i>Shark<sup>3</sup></i> can be run as either the plan web application, or the sharkcube.spec can be used with pyinstaller to create a standalone applications.</p>

<h4>Prerequisities</h4>
<p>To work with the code, the following is required: 
<pre><code>python 3.5
pip
pyinstaller
virtualenv</code></pre> </p>

<h4>Installing</h4>
<p>Once you have a framework version of <a href=https://www.python.org/downloads/><code>python 3.5</code></a> up and running, <a href=https://pip.pypa.io/en/stable/installing/>install <code>pip</code></a> and then use it to install pyinstaller and virtualenv by typing the following into your terminal:</p> 

<p><code>$ pip install pyinstaller</code></p>
<p><code>$ pip install virtualenv</code>.</p>

<p><a href=https://help.github.com/articles/cloning-a-repository/>Clone</a> a copy of the repository, and navigate to it with the terminal. Create a new virtual environment with</p>

<p><code>$ virtualenv --python=python3 venv_sharks</code></p>

<p>where <code>venv_sharks</code> can be replaced with any name for the environment. Now activate you new virtual environment with the following</p>

<p><code>$ source venv_sharks/bin/activate</code>.</p>

<p>The name of you new virtual environment should now be displayed to the left of you command prompt like <code>(vern_shark) $</code>. Now we must install all the dependencies. This is once again made easy thanks to pip!</p>

<p><code>$ pip install -r requirements.txt</code>.</p>

<p>There! However, there is one problem. The version of python installed isn't the framework one, so <code>matplotlib</code> and <code>pyinstaller</code> will refuse to cooperate. This can be remedied by making two new executable: <code>frameworkpython</code> and <code>frameworkpyinstaller</code> and placing them in <code>verv_shark/bin/</code>. Instructions for this can be found <a href=http://matplotlib.org/faq/virtualenv_faq.html>here</a></p>

<p>Once you have installed frameworkpython, you can run the <i>Shark<sup>3</sup></i> by entering</p>

<p><code>$ frameworkpython sharkcube.py</code>.</p>

<p>Alternativly, you can create an independent executable and .app using</p>

<p><code>$ frameworkpyinstaller sharkcube.spec</code>.</p>

<h4>Installing: Option 2</h4>
<p>If the above sounded overly complicated to you, there is an alternative. After cloning the repository, instead of setting up a virtual environment, you simply run</p>

<p><code>$ pip install -r requirements.txt</code></p>

<p>to install all of the dependencies into your normal python. You can then directly run the application with</p>

<p><code>$ python3 sharkcube.py</code></p>

<p>or create an application with</p>

<p><code>$ pyinstaller sharkcube.spec</code>.</p>

<p><i>Note:</i> Although I would typically recommend <a href=https://www.continuum.io/why-anaconda>Anaconda from Continuum Analytics</a> for most python related purposes, pyinstaller requires a full python framework</p>
<h2>Authors</h2>
<p>
    <ul>
        <li>edelsonc -author</li>
    </ul>
</p>
<h2>License</h2>
<p>This project is licensed under the MIT License - see the <code>LICENSE.txt</code> file for detail</p>