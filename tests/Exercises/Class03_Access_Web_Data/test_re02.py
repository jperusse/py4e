from Exercises.Class03_Access_Web_Data.re02 import re_search02


def test_search_using_re02():
    """
    using search from re module
    """
    count = re_search02('mbox-short.txt', '^From:')
    assert count == 27
