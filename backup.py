from datetime import *
import os

label = datetime.now().strftime('%Y-%m-%d_Time-%H-%M')

def main():
    print(f'Hello at {label}')

if __name__ == '__main__':
    main()