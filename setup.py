#!/usr/bin/env python
"""Setup script for the 'uncompyle6' distribution."""

import setuptools
import sys

SYS_VERSION = sys.version_info[0:2]
if not ((2, 4) <= SYS_VERSION  <= (2, 7)):
    mess = "Python Release 2.4 .. 2.7 are supported in this code branch."
    if ((3, 6) <= SYS_VERSION  < (3, 9)):
        mess += ("\nFor your Python, version %s, use the master code/branch." %
                 sys.version[0:3])
    elif (3, 3) <= SYS_VERSION <= (3, 6):
        mess += (
            "\nFor your Python, version %s, use the python-3.3-3.5 code/branch."
            % sys.version[0:3]
        )
    elif SYS_VERSION < (2, 4):
        mess += (
            "\nThis package is not supported for Python before Python 2.4 version %s." % sys.version[0:3]
        )
    print(mess)
    raise Exception(mess)

from __pkginfo__ import (
    author,
    author_email,
    install_requires,
    license,
    long_description,
    classifiers,
    entry_points,
    modname,
    py_modules,
    short_desc,
    __version__,
    web,
    zip_safe,
)

setuptools.setup(
    author=author,
    author_email=author_email,
    classifiers=classifiers,
    description=short_desc,
    entry_points=entry_points,
    install_requires=install_requires,
    license=license,
    long_description=long_description,
    long_description_content_type="text/x-rst",
    name=modname,
    packages=setuptools.find_packages(),
    py_modules=py_modules,
    test_suite="nose.collector",
    url=web,
    tests_require=["nose>=1.0"],
    version=__version__,
    zip_safe=zip_safe,
)
