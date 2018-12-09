import os

CURRENT_DIR = os.getcwd()
ROOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..','..'))

def get_test_files():
    for root, dirs, files in os.walk(ROOT_DIR):
        print (files)



get_test_files()


