#!/usr/bin/env python
# aptinstall.py

import apt
import sys

pkg_names= [
        "pydf",
        "mc",
        "nano"
            ]

cache = apt.cache.Cache()
cache.update()
cache.open()

for pkg_name in pkg_names:
    pkg = cache[pkg_name]
    if pkg.is_installed:
        print("{pkg_name} already installed".format(pkg_name=pkg_name))
    else:
        pkg.mark_install()
        try:
            cache.commit()
        except Exception as arg:
            print >> sys.stderr, "Sorry, package installation failed [{err}]".format(err=str(arg))
