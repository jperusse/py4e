from Exercises.Class03_Access_Web_Data.re01 import re_search01


def test_search_using_re01():
    """
    using search from re module
    """
    count = re_search01('mbox-short.txt', 'From')
    assert count == 54
