============
Installation
============

Install an editable version from the source (GitHub)
----------------------------------------------------
::

    $ cd path_to_first_python_github_tutorial_dirctory_with_environment_yml_file

    $ conda env create -f environment.yml

    $ conda activate python_github_tutorial

    $ pip install -e .


Building the HTML documenation files (GitHub)
---------------------------------------------

Building these HTML files locally via sphinx, which will allow you to access them with your 
local internet browsing application or HTML viewer (chrome, safari, VScode, etc.). 
The HTML files will be located in the ``docs/_build/html`` directory after they are built.  

The python_github_tutorial utilizes `sphinx <https://www.sphinx-doc.org/en/master/index.html>`_ to construct the documentation. 
The user can build the documentation locally by executing the following command from the ``docs`` directory::
    
    $ conda activate python_github_tutorial
    
    $ make html


Testing the software installation
----------------------------------

The python_github_tutorial software tests the installation using `pytest <https://docs.pytest.org/en/stable/>`_. 
The unit tests via ``pytest`` ensure that the code is build properly, running correctly and producing 
accurate results.  

To perform these tests (unit tests) for the python_github_tutorial package, please run the following commands 
from the ``python_github_tutorial/tests`` directory::

    $ conda activate python_github_tutorial
    
    $ pytest -v