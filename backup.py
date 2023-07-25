import os
from datetime import *
from dotenv import load_dotenv

load_dotenv()

label = datetime.now().strftime('%Y-%m-%d_')
PW = os.getenv('ARCGIS_PW')
BACKUP_PATH = os.getenv('BACKUP_PATH')

FULL_PATH = BACKUP_PATH + label + 'Scripted-Backup'

def main():
    print(f'{label, FULL_PATH}')

if __name__ == '__main__':
    main()