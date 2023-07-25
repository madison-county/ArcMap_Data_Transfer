import os
import shutil
from datetime import *
from arcgis.gis import *
from dotenv import load_dotenv

load_dotenv()

BACKUP_PATH = r'//madco-gnas/GIS-SSD/01_Working-Data/04_Backup/02-Data/2023_Backup-Broad'
PW = os.getenv('ARCGIS_PW')

current_date = datetime.now().strftime('%Y-%m-%d_')
label = current_date + 'Scripted-Backup/'

full_path = os.path.join(BACKUP_PATH, label)

def main():
    print(f'{label, full_path}')
    if os.path.isdir(full_path):
        print('Directory Found')
    else:
        os.mkdir(full_path)

def create_directory(path):
    if not os.path.isdir(path):
        os.mkdir(path)
    else:
        print('Directory Found')

if __name__ == '__main__':
    main()