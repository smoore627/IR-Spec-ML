import imagehash
from PIL import Image
import numpy as np
import os 
import hashlib
from pathlib import Path

directory = 'IR Spec Images/'

list_of_files = os.walk(directory)

unique_files = dict()
  
for root, folders, files in list_of_files:
  
    # Running a for loop on all the files
    for file in files:
  
        # Finding complete file path
        file_path = Path(os.path.join(root, file))
  
        # Converting all the content of
        # our file into md5 hash.
        Hash_file = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
  
        # If file hash has already #
        # been added we'll simply delete that file
        if Hash_file not in unique_files:
            unique_files[Hash_file] = file_path
        else:
            os.remove(file_path)
            print(f"{file_path} has been deleted")

                    
            
        