"""
docstring
"""
import all


def test_true():
    """

    :return:
    """
    assert all.all_([True, True]) == True


def test_false():
    """

    :return:
    """
    assert all.all_([True, False]) == False


def test_one_item():
    """

    :return:
    """
    assert all.all_([True]) == True
