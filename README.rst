MPHY0026: Computer Assisted Surgery and Therapy
===============================================

.. image:: https://github.com/UCL/MPHY0026/raw/master/project-icon.png
   :height: 128px
   :width: 128px
   :target: https://github.com/UCL/MPHY0026
   :alt: Logo

.. image:: https://github.com/UCL/MPHY0026/badges/master/pipeline.svg
   :target: https://github.com/UCL/MPHY0026/pipelines
   :alt: GitLab-CI test status

.. image:: https://github.com/UCL/MPHY0026/badges/master/coverage.svg
    :target: https://github.com/UCL/MPHY0026/commits/master
    :alt: Test coverage

.. image:: https://readthedocs.org/projects/MPHY0026/badge/?version=latest
    :target: http://MPHY0026.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


Authors: Matt Clarkson, Steve Thompson, Ester Bonmati

This is the git repository of the Computer Assisted Surgery and Therapy (MPHY0026) course
developed at the `Wellcome EPSRC Centre for Interventional and Surgical Sciences`_,
part of `University College London (UCL)`_.

The generated documentation lives on `Read The Docs`_.


Running
-------

For examples demonstrated in class, you must be "inside" the environment created
by tox. Please work through the whole of the `SNAPPY Tutorial`_ to understand
more about Python development, tox and virtualenvs. For those in a hurry,
you can do this to run examples:

::

    # Clone the repository
    git clone https://github.com/UCL/MPHY0026
    
    # Get inside the repository directory
    cd MPHY0026
    
    # Install tox if it is not already installed
    pip install tox
    
    # Run tox commands without any arguments.(The command may take up to 10 minutes)
    tox
    
    # For Mac and Linux users, run the command
    source .tox/py36/bin/activate
    
    # For Windows users, run the the commands
    cd .tox\py36\bin
    activate
    
    # The environment is setup now and you can run any example with the application.


Developing
----------

Cloning
^^^^^^^

You can clone the repository using the following command:

::

    git clone https://github.com/UCL/MPHY0026


Running tests
^^^^^^^^^^^^^

Pytest is used for running unit tests, but you should run using tox,
as per the `Python Template`_ instructions and described in the `SNAPPY Tutorial`_.


Linting
^^^^^^^

This code conforms to the PEP8 standard. Pylint is used to analyse the code.
Again, follow the `SNAPPY Tutorial`_ instructions and run via tox.


Contributing
------------

Please see the `contributing guidelines`_.


Useful links
------------

* `Source code repository`_
* `Documentation`_


Licensing and copyright
-----------------------

Copyright 2019 University College London.
MPHY0026 is released under the BSD-3 license. Please see the `license file`_ for details.


Acknowledgements
----------------

Supported by `Wellcome`_ and `EPSRC`_.


.. _`Wellcome EPSRC Centre for Interventional and Surgical Sciences`: http://www.ucl.ac.uk/weiss
.. _`source code repository`: https://github.com/UCL/MPHY0026
.. _`Documentation`: https://MPHY0026.readthedocs.io
.. _`Read The Docs`: https://MPHY0026.readthedocs.io
.. _`SNAPPY`: https://weisslab.cs.ucl.ac.uk/WEISS/PlatformManagement/SNAPPY/wikis/home
.. _`University College London (UCL)`: http://www.ucl.ac.uk/
.. _`Wellcome`: https://wellcome.ac.uk/
.. _`EPSRC`: https://www.epsrc.ac.uk/
.. _`contributing guidelines`: https://github.com/UCL/MPHY0026/blob/master/CONTRIBUTING.rst
.. _`license file`: https://github.com/UCL/MPHY0026/blob/master/LICENSE
.. _`SNAPPY Tutorial`: https://snappytutorial02.readthedocs.io/en/latest/
.. _`Python Template`: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/PythonTemplate
