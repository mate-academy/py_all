import all


def test_empty():
    assert all.all([True, True]) == True


def test_odd():
    assert all.all([True, False]) == False


def test_string():
    assert all.all([True]) == True