import pytest
from py_range import segment, box

@pytest.fixture(scope="session")
def s():
    s = segment()
    yield s
    del(s)

@pytest.fixture(scope="session")
def b1():
    b1 = box()
    yield b1
    del(b1)

@pytest.fixture(scope="session")
def b2():
    b2 = box()
    yield b2
    del(b2)

def test_containers(s, b1):
    assert len(s.containers()) == 0
    s += b1
    assert len(s.containers()) == 1
    assert b1 in s.containers()

def test_add_remove(s, b1, b2):
    assert b1 not in s.containers()
    s.add(b1)
    assert b1 in s.containers()
    s.remove(b1)
    assert b1 not in s.containers()
    s.add(b1, b2)
    assert b1 in s.containers()
    assert b2 in s.containers()

def test_iadd_isub_len(s, b1):
    assert len(s) == 0
    s += b1
    assert len(s) == 1
    s -= b1
    assert len(s) == 0

def test_iter_slice(s, b1, b2):
    s.add(b1, b2)
    names = []
    for b in s:
        names.append(b.name)
    assert b1.name in names
    assert b2.name in names
    assert len(names) == 2

def test_str(s):
    assert str(s) == s.name