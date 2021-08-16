import os
import shutil

source=input('Please Enter The Source Folder Name:-')
source=source+'/'
destination=input('Please Enter The Destination Name:-')
destination=destination+'/'
list_of_files=os.listdir(source)
for file in list_of_files:
    shutil.copy((source+file),destination)