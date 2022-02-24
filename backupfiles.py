import os
import shutil
source=input("Enter the source file name")
destination=input("ENter the destination file name")
source=source+'/'
destination=destination+'/'
listoffiles=os.listdir(source)
for file in listoffiles:
    shutil.copy((source+file),destination)