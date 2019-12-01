import all


def test_true():
    assert all.all_item([True, True]) == True


def test_false():
    assert all.all_item([True, False]) == False


def test_one_item():
    assert all.all_item([True]) == True