import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.
    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.
    There are no limit to the depth of the subdirectories can be.
    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system
    Returns:
       a list of paths
    """

    if (suffix=='' or len(os.listdir(path))==0): # Handling the edge cases
        return []

    pElements = os.listdir(path) # List of all the directories (and files) in the present directory (i.e. given path)
    
    pFiles = [file for file in pElements if '.'+suffix in file] # Files in the present directory ending with the given suffix
    
    pFolders = [file for file in pElements if '.' not in file] # All the folders in the present directory

    for folder in pFolders:
        pFiles+=find_files(suffix, path + '/' + folder) # Using recursion to find the required file in all the sub folders and sub sub folders and so on..

    return pFiles


#Getting the Path
path = os.getcwd() + '/testdir' # This file is present in the same folder as this .py file

## Test Cases:

# Edge Cases:
print(find_files('', path))
# []

#General Cases

print(find_files('c', path))
# ['t1.c', 'a.c', 'a.c', 'b.c']

print(find_files('h', path))
# ['t1.h', 'a.h', 'a.h', 'b.h']

print(find_files('sid', path))
# []

