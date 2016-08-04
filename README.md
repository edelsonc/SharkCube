<h1>Welcome to <i>Shark<sup>3</sup></i></h1>
<p>Shark<sup>3</sup> is a mac application that runs a local flask web application. It provides basic information about the 8 coil Helmholtz array located in the New College of Florida Pritzker Marine Lab. Additionally, it has a current caclulator, which calculateds the required current needed in the coils of the array in order to create a local magnetic field of a desiged strength. The purpose of <i>Shark<sup>3</sup></i> was to easily allow Marine Biology students at New College of Florida to caclulated the current they'd need to create magnetic field for behavioral experiments, as well as provide information about the design of <i>Shark<sup>3</sup></i>.</p>

<h2>Getting Started</h2>
<p>To use <i>Shark<sup>3</sup></i> as an application, simple copy the <code>SharkCube.app</code> application located in the <code>dist</code> directory.</p>
<p>This project is under the MIT License, so feel free to poke around the source code! The flask application is all in the sharkcube.py, while pycoil.py contains the physics related functions. CSS and images can be found in <code>static</code>, while HTML will be located in <code>templates</code>.</p>

<h4>Prerequisities</h4>
<p>To work with the code, the following is required: 
<pre><code>python 3.5
virtualenv</code></pre> </p>

<h4>Installing</h4>
<p>Once you have a working copy of <code>python 3.5</code> and <code>virtualenv</code> and have <a href=https://help.github.com/articles/cloning-a-repository/>cloned</a> a copy of <i>Shark<sup>3</sup></i>, you will need to create a new vitual environment.</p>

<p>Using the terminal, navigate to the new <code>SharkCube</code> directory and create a new vitual environtment</p>

<p><code>$ virtualenv name_of_your_new_venv</code></p>

<p>replacing <code>name_of_your_new_venv</code> with a name of your choise (I like <code>venv_shark).</code>. Now you can activate you new virtual environment with</p>

<p><code>$ source name_of_your_new_venv/bin/activate</code>.</p>

<p>The name of your new virtual environment should now be diplayed to the left of the command prompt, like <code>(name_of_your_new_venv) $</code>. All that's left to do is install the appropriate packages. This is done using pip and the <code>requirements.txt</code> as follows:</p>

<p><code>pip install -r requirement.txt</code>.</p>

<p>Now you're ready to go! Begin messing around as you please :)</p>

<p><i>Note:</i> Although I would typically recommend <a href=https://www.continuum.io/why-anaconda>Anaconda from Continuum Analytics</a> for most python related purposes, pyinstaller requires a full python framework</p>
<h2>Authors</h2>
<p>
    <ul>
        <li>edelsonc -author</li>
    </ul>
</p>
<h2>License</h2>
<p>This project is licensed under the MIT License - see the <code>LICENSE.txt</code> file for detail</p>