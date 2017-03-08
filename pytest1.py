# py.test pytest1.py

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
