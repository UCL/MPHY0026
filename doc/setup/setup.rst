.. _PythonSetup:

Python Setup
============

This course assumes some familiarity with Python, and so does not teach the
Python language. However, even for people wanting to run the example
applications, and experiment with the notebooks, some familiarity is required
with how to setup the Python 3 environment.

**This project has been tested with Python 3.9-3.11 (Windows/Mac), and 3.9-3.10 (Linux). Higher versions are not supported and may not function correctly.**

The steps are shown below.

Obtain Code
-----------

Firstly, use git to download the project repository:

::

  git clone https://github.com/UCL/MPHY0026.git


Create a Clean Environment
--------------------------

You should never install Python packages in your default Python installation.
It makes them hard to track, and if you run multiple projects (e.g. tensor flow, pytorch... etc)
then these large projects can depend on many many other smaller python libraries, potentially
leading to version conflict. Each new project, or piece of work should be installed
inside it's own environment.

  - See `how to create and activate a virtual env`_.

If you use a virtualenv, it's best not to create the virtual env folder inside the MPHY0026 folder.

Or you can use conda environments.

  - See `how to create and activate a conda env`_.

Conda manages where to put each new environment, so Conda is probably easier.

Setup This Project
------------------

We suggest 2 options:

  1. Start with a clean conda/virtual env environment, and pip install this project.
  2. Start with a clean conda/virtual env environment, pip install tox, then use tox to install the rest.

Developers typically choose option 2, and option 2 is necessary if you want to run the Jupyter notebooks.

Option 2 is the preferred choice.


Option 1
^^^^^^^^

Given you are inside, (i.e. you have activated) your clean environment, type:

::

    cd MPHY0026
    pip install .


This should download all the dependencies and other projects, such as scikit-surgerybard used in
the :ref:`SummerSchoolCameraCalibration` tutorial, or scikit-surgeryfred used in the :ref:`FidRegistrationTutorial`
should now be available to use. Programs that are included in *this* project can either be run with:

::

  python program_name.py

in the top-level folder of this repository, or just:

::

  program_name

i.e. by typing the just the program_name as the script should be installed properly inside your python environment.



Option 2
^^^^^^^^

::

    cd MPHY0026
    pip install tox
    tox
    source .tox/test/bin/activate

or, if you are on Windows, replace the last line with

::

    .tox\test\Scripts\activate

This option 2 actually creates another virtualenv (in a hidden folder called .tox),
and install all dependencies into that. It may seem a bit over-the-top to create a virtualenv,
inside the original virtualenv, but for things like code development, its often a good thing to
be able to quickly destroy your environment, and starting again if you mess things up.
So developers usually prefer this second option, as you can just destroy the .tox folder, and re-run tox.


Once you have activated the virtual environment inside the .tox folder, you would run
programs from scikit-surgerybard, or scikit-surgeryfred just by typing the program name,
as they are installed inside the current environment. But for programs in the top
level, root folder of *this* repository, you would always type:

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
You will notice that `these instructions for Jupyter Notebooks`_ in this course,
require Option 2 described above. This is another reason to prefer Option 2.


.. _`how to create and activate a virtual env`: https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments
.. _`how to create and activate a conda env`: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
.. _`these instructions for Jupyter Notebooks`: https://mphy0026.readthedocs.io/en/latest/notebooks/running_notebooks.html
