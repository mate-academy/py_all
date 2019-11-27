import all


def test_true():
    assert all.all_([True, True]) == True


def test_false():
    assert all.all_([True, False]) == False


def test_one_item():
    assert all.all_([True]) == True
