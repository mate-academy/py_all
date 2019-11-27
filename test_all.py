import all


def test_true():
    assert all.new_all([True, True]) == True


def test_false():
    assert all.new_all([True, False]) == False


def test_one_item():
    assert all.new_all([True]) == True