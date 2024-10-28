import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PassCheck import check_password


def test_pass():
    assert check_password("Thispasswordis1@") is True


def test_capital():
    assert check_password("dponiumonqweD1@#") is True

def test_lower():
    assert check_password("ALLUPPERCASE12@@") is False

def test_special():
    assert check_password("Passwordhasnospecialcharacters%") is False

def test_short():
    assert check_password("lengthnotvalid") is False









