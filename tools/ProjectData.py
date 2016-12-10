import os

class ProjectData(object):
    """
    a. Scans the project folder structure and updates the list with the
    productive code files.
    """
    def __init__(self,root_folder=None):
        self.productiveCodeNoFiles = 0
        self.rootFolderAbsPath = None
        
        if (root_folder and os.path.isdir(root_folder)):
            self.rootFolderAbsPath = root_folder
            self.productiveCodeNoFiles = self._getAllFiles()
    
    def _getAllFiles(self):
        """
        Parse the whole project folder and update the list with
        all existing files (relative paths to the root folder).
        The file list is sorted!
        Return the number of found files
        """
        self.productiveCodeFiles = sorted(list(self._recursiveFolderScan()))
        return len(self.productiveCodeFiles)
    
    def _recursiveFolderScan(self):
        """
        Recursively parse the project folder and return the found files
        This function is a generator.
        """
        root_folder = self.rootFolderAbsPath+'/'
        for dirpath, dirnames, filenames in os.walk(root_folder):
            for filename in filenames:
                yield os.path.join(dirpath.replace(root_folder, ''),filename)
                
                
# EOF
