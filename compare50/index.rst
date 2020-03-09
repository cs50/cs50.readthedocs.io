``compare50``
=============

.. toctree::
   :hidden:
   :maxdepth: 3
   :caption: Contents:

   api

.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`api`
.. * :ref:`modindex`
.. * :ref:`search`

TODO

Installation
************

First make sure you have Python 3.6 or higher installed. You can download Python |download_python|.

.. |download_python| raw:: html

   <a href="https://www.python.org/downloads/ target="_blank">here</a>


To install compare50 under Linux / OS X:

.. code-block:: bash

    pip install compare50

Under Windows, please |install_windows_sub|. Then install compare50 within the subsystem.

.. |install_windows_sub| raw:: html

   <a href="https://docs.microsoft.com/en-us/windows/wsl/install-win10" target="_blank">install the Linux subsystem</a>

Usage
*******

Usage::

    usage: compare50 [-h] [-a ARCHIVE [ARCHIVE ...]] [-d DISTRO [DISTRO ...]]
                     [-p PASSES [PASSES ...]] [-i INCLUDE [INCLUDE ...]]
                     [-x EXCLUDE [EXCLUDE ...]] [--list] [-o OUTPUT] [-v]
                     [-n MATCHES] [--profile] [--debug]
                     submissions [submissions ...]

    positional arguments:
      submissions           Paths to submissions to compare

    optional arguments:
      -h, --help            show this help message and exit
      -a ARCHIVE [ARCHIVE ...], --archive ARCHIVE [ARCHIVE ...]
                            Paths to archive submissions. Archive submissions are
                            not compared against other archive submissions, only
                            against regular submissions.
      -d DISTRO [DISTRO ...], --distro DISTRO [DISTRO ...]
                            Paths to distribution files. Contents of these files
                            are stripped from submissions.
      -p PASSES [PASSES ...], --passes PASSES [PASSES ...]
                            Specify which passes to use. compare50 ranks only by
                            the first pass, but will render views for every pass.
      -i INCLUDE [INCLUDE ...], --include INCLUDE [INCLUDE ...]
                            Globbing patterns to include from every submission.
                            Includes everything (*) by default. Make sure to quote
                            your patterns to escape any shell globbing!
      -x EXCLUDE [EXCLUDE ...], --exclude EXCLUDE [EXCLUDE ...]
                            Globbing patterns to exclude from every submission.
                            Nothing is excluded by default. Make sure to quote
                            your patterns to escape any shell globbing!
      --list                List all available passes and exit.
      -o OUTPUT, --output OUTPUT
                            location of compare50's output
      -v, --verbose         display the full tracebacks of any errors
      -n MATCHES            number of matches to output
      --profile             profile compare50 (development only, requires
                            line_profiler, implies debug)
      --debug               don't run anything in parallel, disable progress bar


TODO
