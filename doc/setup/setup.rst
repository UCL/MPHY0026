.. _PythonSetup:

Python Setup
============

This course assumes some familiarity with Python, and does not teach the
Python language. You do need to have some familiarity in managing Python environments.

**This project has been tested with Python 3.9-3.11 (Windows/Linux/Mac). Higher versions are not supported and may not function correctly.**

To setup this project, to be able to run the code, please follow the steps below.

Obtain Code
-----------

Firstly, use git to download the project repository:

::

  git clone https://github.com/UCL/MPHY0026.git


Create a Clean Environment
--------------------------

You should never install Python packages in your default Python installation.
It makes them hard to track, and if you run multiple projects (e.g. you have different pieces of coursework
with different versions of libraries like pytorch etc.)
then these large projects can depend on many many other smaller python libraries, potentially
leading to version conflict. Each new project, or piece of work should be installed
inside it's own environment.

**These instructions assume you have installed `conda/anaconda`_ **, as this seems to be fairly popular for most students.

At a terminal window:

::

    # Change directory, to ensure the current working directory is the root folder of the MPHY0026 project
    cd MPHY0026

    # Create a new environment, called MPHY0026, running python version 3.10.
    conda create -n MPHY0026 python=3.10

    # Activate this environment, so that all future pip installs only install into this environment.
    conda activate MPHY0026

    # Install tox, a package for automating testing and building environments.
    pip install tox

    # Installs all the right libraries into a virtualenv
    tox


If any of the commands failed, speak to a lab assistant. Assuming tox ran successfully,
you can activate a virtual env built by the tox command.

For Mac and Linux, activate the virtual environment using command

::

  source .tox/test/bin/activate

For Windows, activate the virtual environment using command
::

  .tox\test\Scripts\activate

If all goes well the prompt should be preceded by (test), which is the name of the virtual environment created by tox.

This above process should download all the dependencies and other projects, such as scikit-surgerybard used in
the :ref:`SummerSchoolCameraCalibration` tutorial, or scikit-surgeryfred used in the :ref:`FidRegistrationTutorial`
should now be available to use. Programs that are included in *this* project can be run with:

::

  python program_name.py

as *this* project itself has not been installed.


A Note About Terminals
----------------------

Windows/Linux/Mac all have different terminals to run commands. Furthermore,
people will often be familiar with running shell commands inside a terminal
that is run within their code editor like PyCharm or VS Code.

Here is a list of caveats and proposed work arounds:

* Windows Powershell - restricts use to webcam. Use Anaconda shell, or simple cmd.exe
* Mac OSX 10.15 and above - restricts access to webcam if using shells launched by PyCharm/VS Code. Use default Terminal application.


Jupyter Notebooks
-----------------

Once you have an active Python environment, extra steps are required to get
code in this repository running nicely within Jupyter Notebooks.
See `these instructions for Jupyter Notebooks`_.

.. _`these instructions for Jupyter Notebooks`: https://mphy0026.readthedocs.io/en/latest/notebooks/running_notebooks.html
.. _`conda/anaconda`: https://www.anaconda.com/