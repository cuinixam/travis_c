import unittest

from ProjectData import ProjectData

import os
import sys
currentFileAbsPath = os.path.dirname(os.path.realpath(sys.argv[0]))
oneFileProjectPath = currentFileAbsPath + '/data/projects/one_file'
simpleProjectPath  = currentFileAbsPath + '/data/projects/simple'
moreFoldersProjectPath  = currentFileAbsPath + '/data/projects/more_folders'

class ProductiveCode(unittest.TestCase):
    """
    Check if the productive code is detected properly
    while parsing the folder structure.
    """
    def test_ClassExists(self):
        self.assertTrue(ProjectData, 'The class ProjectData should exist')
    
    def test_RootFolderArgument(self):
        # Invalid root folder
        my_project_data = ProjectData(root_folder='pa96htgex4dzhkGJ')
        self.assertTrue(my_project_data, 'The ProjectData object should be created')
        self.assertFalse(my_project_data.rootFolderAbsPath,'Root folder must exist!')
        self.assertEqual(my_project_data.productiveCodeNoFiles, 0, 'Default: no files found')
        # Valid root folder
        my_project_data = ProjectData(root_folder=oneFileProjectPath)
        self.assertTrue(my_project_data.rootFolderAbsPath,'Root folder exists!')
        
    def test_OneProjectFile(self):
        my_project_data = ProjectData(root_folder=oneFileProjectPath)
        self.assertEqual(my_project_data.productiveCodeNoFiles, 1, 'One file was found')
        self.assertEqual(my_project_data.productiveCodeFiles, ["main.c"], 'The file  main.c should be found!')
    
    def test_SimpleProject(self):
        my_project_data = ProjectData(root_folder=simpleProjectPath)
        self.assertEqual(my_project_data.productiveCodeNoFiles, 3, 'All files must be found')
        self.assertEqual(len(my_project_data.productiveCodeFiles),
                         my_project_data.productiveCodeNoFiles,
                         'The number of files should correspond to the file list length')
        self.assertEqual(sorted(my_project_data.productiveCodeFiles),
                         sorted(["main.c","module.h","module.c"]),
                         'All files should be found')
        
    def test_MoreFoldersProject(self):
        my_project_data = ProjectData(root_folder=moreFoldersProjectPath)
        self.assertEqual(my_project_data.productiveCodeNoFiles, 9, 'All files must be found')
        self.assertEqual(len(my_project_data.productiveCodeFiles),
                         my_project_data.productiveCodeNoFiles,
                         'The number of files should correspond to the file list length')
        self.assertEqual(sorted(my_project_data.productiveCodeFiles),
                         sorted(["a/a.c","a/a.h","b/a.c","b/b.h","c/c.c","c/b.h",
                                 "main.c","module.c","module.h"]),
                         'All files should be found')
    
##    def test_ParseFolderPerformance(self):
##        """
##        Parsing 732112 file and return a list with all files ABSOLUTE path to the folder root
##        Ran in 9.876s
##        
##        Parsing 754567 file and return a list with all files RELATIVE path to the folder root
##        Ran in 5.632s
##        
##        """
##        my_project_data = ProjectData(root_folder='/')
##        self.assertEqual(my_project_data.productiveCodeNoFiles, 1, 'One file was found')
        

# EOF
