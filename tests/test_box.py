import pytest
from py_range import box


def test_box_class():
    '''Test box class instantiation.'''
    b = box()
    assert isinstance(b, box)
    assert hasattr(b, 'open')
    assert hasattr(b, 'close')
    assert hasattr(b, 'put')
    assert hasattr(b, 'dir')
    assert hasattr(b, 'run')
    assert hasattr(b, 'ports')
    assert hasattr(b, 'ps')


@pytest.mark.skip(reason='Requires Docker implementation')
def test_box_docker():
    '''Test creating box from Docker image.'''
    b = box.docker('alpine')
    assert isinstance(b, box)
    # TODO check that the alpine container b wraps is actually present


def test_ports():
    '''Test ports management.'''
    b = box()
    b.open(22)
    assert 22 in b.ports()
    b.open(80)
    assert 22 in b.ports()
    assert 80 in b.ports()
    b.close(22)
    assert 22 not in b.ports()
    assert 80 in b.ports()
    # TODO add support for opening and closing more than one port at a time


def test_put():
    '''Test putting files into box.'''
    b = box()
    b.put('local.txt', '/app.txt') # TODO local.txt should be a real file that pytest can actually reach during testing
    assert 'app.txt' in b.dir('/')


def test_dir():
    '''Test directory listing.'''
    b = box()
    files = b.dir('/', recurse=True)
    assert isinstance(files, list)
    # TODO have this call test_put and then check dir again and confirm that the new file is present


def test_run():
    '''Test running commands.'''
    b = box()
    output = b.run('ls /')
    assert isinstance(output, str)
    assert 'bin' in output 
    # TODO checck that run works correctly with background set to both true or false


def test_ps():
    '''Test process listing.'''
    b = box()
    processes = b.ps()
    assert isinstance(processes, list)
    # TODO run a command before and check that it is present when ps is called
