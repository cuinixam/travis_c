#!/usr/bin/python3

import unittest

# Ugly hack to be able to import the modules included
# in the tools folder
import sys, os
currentFileAbsPath = os.path.dirname(os.path.realpath(sys.argv[0]))
sys.path.insert(0, currentFileAbsPath + '/../tools')

if __name__ == "__main__":
    all_tests = unittest.TestLoader().discover('.')
    status = unittest.TextTestRunner().run(all_tests)
    status = str(status)
    if ('errors=0' in status and 'failures=0' in status):
        status = 0
    else:
        status = 1
    sys.exit(status)

#EOF
