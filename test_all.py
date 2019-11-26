import all


def test_true():
    assert all.all([True, True]) == True


def test_false():
    assert all.all([True, False]) == False


def test_one_item():
    assert all.all([True]) == True