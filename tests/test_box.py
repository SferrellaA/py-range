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

@pytest.fixture(scope="session")
def b():
    b = box(start=True)
    yield b
    del(b)

def test_run(b):
    assert "bin" in b.run('ls /')
    with pytest.raises(TimeoutError):
        b.run("sleep infinity", timeout=1)

def test_ps(b):
    assert "sleep infinity" in b.ps()
