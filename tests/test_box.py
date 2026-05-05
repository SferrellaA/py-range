import pytest
from py_range import box
from subprocess import run

def test_start_ready():
    # default
    a = box(start=False)
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
    b = box()
    yield b
    del(b)

def test_run(b):
    assert "bin" in b.run('ls /')
    with pytest.raises(TimeoutError):
        b.run("sleep infinity", timeout=1)

def test_ps(b):
    assert "sleep infinity" in b.ps()

def test_dir(b):
    assert "bin" in b.dir("/")

def test_put_get(b, tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("test")
    b.put(str(test_file), "/")
    assert "test.txt" in b.dir("/")
    output_file = tmp_path / "test2.txt"
    b.get("/test.txt", str(output_file))
    assert output_file.read_text() == "test"

def list_containers() -> str:
    output = run("docker ps -a", shell=True, capture_output=True)
    output = str(output.stdout)
    return output

def test_attach(b):
    b.run("touch /asdf")
    a = box.attach(b.name)
    assert "asdf" in a.run("ls /")