#!/usr/bin/python3

import unittest

# Ugly hack to be able to import the modules included
# in the tools folder
import sys, os
sys.path.insert(0, os.path.abspath('../tools'))

if __name__ == "__main__":
    all_tests = unittest.TestLoader().discover('.')
    unittest.TextTestRunner().run(all_tests)