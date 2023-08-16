import sys
import os
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from src import app_start as ko

def test_sum_number():
    assert ko.sum(2,3) == 5

def test_sum_string():
    assert ko.sum("маша", " саша") == "маша саша"