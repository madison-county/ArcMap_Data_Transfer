import os
import shutil
from datetime import *
from dotenv import load_dotenv

load_dotenv()

BACKUP_PATH = r'//madco-gnas/GIS-SSD/01_Working-Data/04_Backup/02-Data/2023_Backup-Broad'

current_date = datetime.now().strftime('%Y-%m-%d_')
PW = os.getenv('ARCGIS_PW')
#BACKUP_PATH = os.getenv('BACKUP_PATH')

label = current_date + 'Scripted-Backup/'

FULL_PATH = os.path.join(BACKUP_PATH, label)

def main():
    print(f'{label, FULL_PATH}')
    os.mkdir(FULL_PATH)

if __name__ == '__main__':
    main()