from src.plus_one import func

def test_wrong_add():
    assert func(3) != 5

def test_right_add():
    assert func(3) == 4