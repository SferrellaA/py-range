import pytest
from py_range import box

def test_start_ready():
    # default
    a = box()
    assert a.ready() == False
    a.start()
    assert a.ready() == True
    del(a)

    # start on creation
    b = box(start=True)
    assert b.ready() == True
    del(b)

    # short command on start
    c = box(command="ls")
    assert c.ready() == False
    del(c)

def test_run():
    '''Test running commands.'''
    b = box(start=True)
    output = b.run('ls /')
    print(output)
    assert 'bin' in output
