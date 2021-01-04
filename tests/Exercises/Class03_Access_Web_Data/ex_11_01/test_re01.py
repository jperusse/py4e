from Exercises.Class03_Access_Web_Data.ex_11_01.re01 import run_search

def test_search_using_re():
    """
    using search from re module
    """
    count = run_search('mbox-short.txt', 'From:')
    assert count == 27
