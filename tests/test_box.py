import pytest
from py_range import box

def test_box_class():
    """Test box class instantiation."""
    b = box()
    assert isinstance(b, box)
    assert hasattr(b, "docker")


@pytest.mark.skip(reason="Requires Docker implementation")
def test_box_docker():
    """Test creating box from Docker image."""
    b = box.docker("alpine")
    assert isinstance(b, box)
