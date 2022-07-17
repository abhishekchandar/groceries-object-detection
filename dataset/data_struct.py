import shutil
import os

base_folder = "images"

#List of dir inside images folder
listFolder = [x[0] for x in os.walk(base_folder)]
for s in listFolder:
    source_folder = s
    destination_folder = "imagess"

    # fetch all files
    for file_name in os.listdir(source_folder):
        # construct full file path
        source = os.path.join(source_folder,file_name)
        print(source)
        destination = os.path.join(destination_folder,file_name)
        print(destination)
        # copy only files
        if os.path.isfile(source):
            shutil.copy(source, destination)
            print('copied', file_name)
