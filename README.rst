MPHY0026
===============================

.. image:: https://weisslab.cs.ucl.ac.uk/WEISSTeaching/MPHY0026/raw/master/project-icon.png
   :height: 128px
   :width: 128px
   :target: https://weisslab.cs.ucl.ac.uk/WEISSTeaching/MPHY0026
   :alt: Logo

.. image:: https://weisslab.cs.ucl.ac.uk/WEISSTeaching/MPHY0026/badges/master/build.svg
   :target: https://weisslab.cs.ucl.ac.uk/WEISSTeaching/MPHY0026/pipelines
   :alt: GitLab-CI test status

.. image:: https://weisslab.cs.ucl.ac.uk/WEISSTeaching/MPHY0026/badges/master/coverage.svg
    :target: https://weisslab.cs.ucl.ac.uk/WEISSTeaching/MPHY0026/commits/master
    :alt: Test coverage

.. image:: https://readthedocs.org/projects/MPHY0026/badge/?version=latest
    :target: http://MPHY0026.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status



Author: Matt Clarkson

MPHY0026 is part of the `SNAPPY`_ software project, developed at the `Wellcome EPSRC Centre for Interventional and Surgical Sciences`_, part of `University College London (UCL)`_.

MPHY0026 supports Python 2.7 and Python 3.6.

MPHY0026 is currently a demo project, which will add/multiply two numbers. Example usage:

::

    python mphy0026.py 5 8
    python mphy0026.py 3 6 --multiply

Please explore the project structure, and implement your own functionality.

Developing
----------

Cloning
^^^^^^^

You can clone the repository using the following command:

::

    git clone https://weisslab.cs.ucl.ac.uk/WEISSTeaching/MPHY0026


Running tests
^^^^^^^^^^^^^
Pytest is used for running unit tests:
::

    pip install pytest
    python -m pytest


Linting
^^^^^^^

This code conforms to the PEP8 standard. Pylint can be used to analyse the code:

::

    pip install pylint
    pylint --rcfile=tests/pylintrc mphy0026


Installing
----------

You can pip install directly from the repository as follows:

::

    pip install git+https://weisslab.cs.ucl.ac.uk/WEISSTeaching/MPHY0026



Contributing
^^^^^^^^^^^^

Please see the `contributing guidelines`_.


Useful links
^^^^^^^^^^^^

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
.. _`source code repository`: https://weisslab.cs.ucl.ac.uk/WEISSTeaching/MPHY0026
.. _`Documentation`: https://MPHY0026.readthedocs.io
.. _`SNAPPY`: https://weisslab.cs.ucl.ac.uk/WEISS/PlatformManagement/SNAPPY/wikis/home
.. _`University College London (UCL)`: http://www.ucl.ac.uk/
.. _`Wellcome`: https://wellcome.ac.uk/
.. _`EPSRC`: https://www.epsrc.ac.uk/
.. _`contributing guidelines`: https://weisslab.cs.ucl.ac.uk/WEISSTeaching/MPHY0026/blob/master/CONTRIBUTING.rst
.. _`license file`: https://weisslab.cs.ucl.ac.uk/WEISSTeaching/MPHY0026/blob/master/LICENSE

