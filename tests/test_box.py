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


@pytest.fixture
def local_file(tmp_path):
    p = tmp_path / 'local.txt'
    p.write_text('hello')
    return str(p)


@pytest.fixture
def docker_box():
    '''Fixture for box.docker alpine w/ cleanup.'''
    b = box.docker('alpine')
    yield b
    b.close_box()


def test_box_docker():
    '''Test creating box from Docker image.'''
    b = box.docker('alpine')
    assert isinstance(b, box)
    processes = b.ps()
    assert len(processes) > 0


def test_ports(docker_box):
    '''Test ports management.'''
    b = docker_box
    b.open(22)
    assert 22 in b.ports()
    b.open(80)
    assert 22 in b.ports()
    assert 80 in b.ports()
    b.close(22)
    assert 22 not in b.ports()
    assert 80 in b.ports()
    b.close([80])
    assert 80 not in b.ports()
    b.open([22, 8080])
    assert set(b.ports()) == {22, 8080}


def test_put(local_file, docker_box):
    '''Test putting files into box.'''
    b = docker_box
    b.put(local_file, '/app.txt')
    assert 'app.txt' in b.dir('/')


def test_dir(local_file, docker_box):
    '''Test directory listing.'''
    b = docker_box
    files = b.dir('/', recurse=True)
    assert isinstance(files, list)
    b.put(local_file, '/app.txt')
    files = b.dir('/')
    assert 'app.txt' in files


def test_run(docker_box):
    '''Test running commands.'''
    b = docker_box
    output = b.run('ls /', background=False)
    assert isinstance(output, str)
    assert 'bin' in output
    pid = b.run('sleep 10', background=True)
    assert isinstance(pid, (int, str))  # PID/handle


def test_ps(docker_box):
    '''Test process listing.'''
    b = docker_box
    b.run('sleep inf', background=True)
    processes = b.ps()
    assert isinstance(processes, list)
    assert any('sleep' in str(p) for p in processes)
