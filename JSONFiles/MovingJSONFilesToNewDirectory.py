import os
import glob
import json
import shutil

def main():
        #SET THE SOURCE & DESTINATION FOLDERS                
        src = 'C:\OriginFolder'
        dst = 'C:\DestinationFolder'

        #CHANGE DIRECTORY TO SOURCE FOLDER
        os.chdir('C:\OriginFolder')

        #SELECT ONLY JSON FILES IN SOURCE FOLDER
        filelist = glob.glob('*.json')

        #TRANSFER JSON FILES FROM SOURCE TO DESTINATION FOLDER
        for i in filelist:        
                shutil.move(os.path.join(i), os.path.join(dst, i))

main()
