import unittest

import ProjectData

class ProductiveCode(unittest.TestCase):
    """
    Check if the productive code is detected properly
    while parsing the folder structure.
    """
    def test_ClassExists(self):
        self.assertTrue(ProjectData, 'The class ProjectData should exist')