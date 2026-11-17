from calculator import add


def test_add():
    assert add(10, 20) == 30


def test_add_negative_numbers():
    assert add(-5, -5) == -10