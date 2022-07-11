#!/usr/bin/env python3

import sys
import os
import time

# TO-DO
# 1) Iterate over all folders
# 2) Search for files inside each folder then find and delete files which have size smaller then a specific Bytes

def empty_ovpn_deleter(path):
    for operand in os.scandir(path):
        if(os.stat(path + "/" + operand.name).st_size <= 162):
            os.remove(path + "/" + operand.name)

def lister(path):
    for operand in os.scandir(path):
        sys.stdout.write('|===> ' + str(operand.name) + '  :  ' + str(os.stat(path + "/" + operand.name).st_size) + ' bytes \n' )

def folder_opener(path):
    for operand in os.scandir(path):
        if(operand.is_dir()):
            sys.stdout.write('-> ' + str(operand.name) + '\n')
            empty_ovpn_deleter(operand.name)
            lister(operand.name)

def main():
    path = "."
    folder_opener(path)

if __name__ == '__main__':
    main()
