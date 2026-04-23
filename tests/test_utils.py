import pytest
from py_range import random_name
from re import match

def test_random_name():
    # check that the name is valid for a docker container
    name = random_name()
    assert(name)
    assert(len(name) < 255)
    assert(match(r'^[a-zA-Z0-9_.-]+$', name))
