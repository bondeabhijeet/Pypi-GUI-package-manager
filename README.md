<!DOCTYPE html>
<html>

<head>
    PyPI GUI Package Manager
</head>

<body>

<h1>PyPI GUI Package Manager</h1>

<img src="https://img.shields.io/github/stars/bondeabhijeet/Pypi-GUI-package-manager?style=social" alt="GitHub stars"> <img src="https://img.shields.io/github/forks/bondeabhijeet/Pypi-GUI-package-manager?style=social" alt="GitHub forks"> <img src="https://img.shields.io/github/issues/bondeabhijeet/Pypi-GUI-package-manager" alt="GitHub issues"> <img src="https://img.shields.io/github/license/bondeabhijeet/Pypi-GUI-package-manager" alt="GitHub license">

<p>The PyPI GUI Package Manager is a simple and user-friendly graphical interface for managing Python packages from the Python Package Index (PyPI). It provides an intuitive way to search for packages, install, and upgrade them without needing to use the command line.</p>

<h2>Features</h2>

<ul>
    <li><strong>Search Packages:</strong> Easily search for Python packages on PyPI using keywords.</li>
    <li><strong>Install Packages:</strong> Install packages with a single click.</li>
    <li><strong>Upgrade Packages:</strong> Keep your packages up to date by upgrading them with a simple click.</li>
    <li><strong>User-Friendly Interface:</strong> Designed for ease of use and a pleasant user experience.</li>
</ul>

<h2>Getting Started</h2>

<h3>Prerequisites</h3>

<ul>
    <li>Python 3.6 or higher | <a href="https://www.python.org/downloads/"> Download python ↗ </a> </li>
    <li><code>pip</code> and <code>tkinter</code> should be installed with your Python distribution.</li>
</ul>

<h3>Installation</h3>

<ol>
    <li>Clone the repository to your local machine:</li>
</ol>

<pre><code>git clone https://github.com/bondeabhijeet/Pypi-GUI-package-manager.git</code></pre>

<ol start="2">
    <li>Navigate to the project directory:</li>
</ol>

<pre><code>cd Pypi-GUI-package-manager</code></pre>

<ol start="3">
    <li>Install the required dependencies:</li>
</ol>

<pre><code>pip install -r requirements.txt</code></pre>

<h3>Usage</h3>

<p>To launch the PyPI GUI Package Manager, run the following command:</p>

<pre><code>python main.py</code></pre>

<p>The application will open, and you can start searching for, installing, and upgrading Python packages from PyPI with ease.</p>

<h2> Building the .exe (--onefile) or an uncompressed folder (--onedir)</h2>
<p>
    Using PyInstaller to create a standalone executable from a Python script
    <ol>
        <li>PyInstaller Installation: Before you can use PyInstaller, you need to have it installed. You can install it using pip:</li>
    </ol>
    <pre><code>pip install pyinstaller</code></pre>
    <ol start="2">
        <li>Open the terminal or command prompt, navigate to the directory containing your main.py and favicon.ico files, and then run the PyInstaller command:</li>
        <br>
        for onedir (will generate a folder containing a exe and the unpacked files) <a href="https://pyinstaller.org/en/stable/operating-mode.html#how-the-one-file-program-works">refer</a>:
        <pre><code>pyinstaller --name pypi-gui-package-manager --icon=favicon.ico --onedir main.py</code></pre>
        for onefile:
        <pre><code>pyinstaller --name pypi-gui-package-manager --icon=favicon.ico --onefile main.py</code></pre>
    </ol>
    After running this command, PyInstaller will generate a standalone executable in the dist directory within your current working directory. The name of the executable will be "pypi-gui-package-manager".
    You can then distribute this executable to others who can run it without needing to install Python or any additional dependencies.
</p>


<!-- <h2>Screenshots</h2>

<img src="screenshots/screenshot1.png" alt="Screenshot 1">

<img src="screenshots/screenshot2.png" alt="Screenshot 2"> -->

<h2>Contributing/Issues and Support</h2>

<p>Contributions are welcome! If you encounter any issues or have questions about using the PyPI GUI Package Manager, please fork the repository, make your changes, and open a pull request.</p>
<!--
<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
-->
<h2>Acknowledgments</h2>

<ul>
    <li>The PyPI GUI Package Manager is built using Python and the Tkinter library.</li>
    <li>We thank the Python community and PyPI maintainers for providing a robust platform for package management.</li>
</ul>

<h2>Features to be implemented</h2>
<ul>
    <li><strong>Uninstall Packages:</strong> Remove packages you no longer need with ease.</li>
    <li><strong>Package Details:</strong> View detailed information about a package before installation.</li>
    <li><strong>Package Version Selection:</strong> Choose the version of a package to install or upgrade.</li>
    <li><strong>Dependency Resolution:</strong> Automatically resolves and installs package dependencies.</li>
    <li><strong>Virtual Environments:</strong> Option to install packages in a virtual environment for isolation.</li>
</ul>

<p>Happy coding!</p>

</body>

</html>
