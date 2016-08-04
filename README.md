<h1>Welcome to <i>Shark<sup>3</sup></i></h1>
Shark<sup>3</sup> is a mac application that runs a local flask web application. It provides basic information about the 8 coil Helmholtz array located in the New College of Florida Pritzker Marine Lab. Additionally, it has a current caclulator, which calculateds the required current needed in the coils of the array in order to create a local magnetic field of a desiged strength. The purpose of <i>Shark<sup>3</sup></i> was to easily allow Marine Biology students at New College of Florida to caclulated the current they'd need to create magnetic field for behavioral experiments, as well as provide information about the design of <i>Shark<sup>3</sup></i>.

<h2>Getting Started</h2>
To use <i>Shark<sup>3</sup></i> as an application, simple copy the <code>SharkCube.app</code> application located in the <code>dist</code> directory.

This project is under the MIT License, so feel free to poke around the source code! The flask application is all in the sharkcube.py, while pycoil.py contains the physics related functions. CSS and images can be found in <code>static</code>, while HTML will be located in <code>templates</code>.

<h3>Prerequisities</h3>

<pre><code>
python 3.5
flask
matplotlib
numpy
scipy
pyinstaller
</code></pre>

<i>Note:</i> <u>Although I would typically recommend <a href=https://www.continuum.io/why-anaconda>Anaconda from Continuum Analytics</a> for most python related purposes, pyinstaller requires a full python framework</u>

<h2>Authors</h2>
<ul>
    <li>edelsonc -author</li>
</ul>

<h2>License</h2>
This project is licensed under the MIT License - se the <code>LICENSE.txt</code> file for detail