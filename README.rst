pip-pop
=======

Working with lots of ``requirements.txt`` files can be a bit annoying.
Have no fear, **pip-pop** is here!

(work in progress)

Planned Commands
----------------

``$ pip-diff [--fresh | --stale] <reqfile> <reqfile>``

Generates a diff between two given requirements files. Lists either stale or fresh packages.

``$ pip-grep <reqfile> <package>...``

Takes a requirements file, and searches for the specified package (or packages) within it.
Essential when working with included files.


Possible Future Commands
------------------------

- Install with blacklisting support (wsgiref, distribute, setuptools).
