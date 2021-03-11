"""
pip-pop manages your requirements files.
"""
from setuptools import setup


setup(
    name='pip-pop',
    version='0.1.0',
    url='https://github.com/kennethreitz/pip-pop',
    license='MIT',
    author='Kenneth Reitz',
    author_email='me@kennethreitz.org',
    description=__doc__.strip('\n'),
    #packages=[],
    scripts=['bin/pip-diff', 'bin/pip-grep'],
    #include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['docopt', 'pip>=1.5.0'],
    tests_require=['tox'],
    classifiers=[
        # As from https://pypi.python.org/pypi?%3Aaction=list_classifiers
        #'Development Status :: 1 - Planning',
        #'Development Status :: 2 - Pre-Alpha',
        #'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        #'Development Status :: 5 - Production/Stable',
        #'Development Status :: 6 - Mature',
        #'Development Status :: 7 - Inactive',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: System :: Systems Administration',
    ]
)