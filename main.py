# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from inspect import getsourcefile
from os.path import abspath
import inspect, os.path
from sys import *

def print_file_name():
    # print( "Executing the : ",__file__)


    print(sys.argv[0])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_file_name()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
