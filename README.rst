pip-pop: tools for managing requirements files
==============================================

Working with lots of ``requirements.txt`` files can be a bit annoying.
Have no fear, **pip-pop** is here!

(work in progress)

Planned Commands
----------------

``$ pip-diff [--fresh | --stale] <reqfile> <reqfile> [output]``

Generates a diff between two given requirements files. Lists either stale or fresh packages.

``$ pip-flatten [--unsorted] <reqfile> [output]``

Takes a single requirements file, and expands it. Essential when working with included files.
Will potentially support blacklisting modules (wsgiref, distribute, setuptools).


Possible Future Commands
------------------------

- ``pip-where``