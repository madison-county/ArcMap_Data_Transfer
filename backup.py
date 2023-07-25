import os
from datetime import *
from dotenv import load_dotenv

load_dotenv()

label = datetime.now().strftime('%Y-%m-%d_Time-%H-%M')
PW = os.getenv('ARCGIS_PW')

def main():
    print(f'Hello at {label}')

if __name__ == '__main__':
    main()