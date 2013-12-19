Pasty
=====

Pasty is a library to provide applications with "serverless" state management.



Getting Started
===============

Requirements
------------

* Python 3: http://www.python.org/download/releases/3.3.3/#download


Installation
------------

Pasty can be installed with ``pip`` or ``easy_install``:

    pip install Pasty

Or directly from the source code:

    python setup.py install



Basic Usage
===========

After installation, abstract base classes can be imported from the package:

    python
    >>> import pasty
    pasty.__version__


For Developers
==============

Requirements
------------
* Python 3: http://www.python.org/download/releases/3.3.3/#download
* GNU Make:
    * Windows: http://cygwin.com/install.html
    * Mac: https://developer.apple.com/xcode
    * Linux: http://www.gnu.org/software/make (likely already installed)
* virtualenv: https://pypi.python.org/pypi/virtualenv#installation
* Pandoc: http://johnmacfarlane.net/pandoc/installing.html


Environment
-----------

Create a virtualenv:

    make develop

Run static analysis:

    make doc
    make pep8
    make pylint
    make check  # all of the above

Run the tests:

    make test
    make tests  # includes integration tests
