# Search for lines that start with 'From'

from Exercises.Class03_Access_Web_Data.utils import ExerciseUtils


def re_search02(fname, search_str):
    """
    Search for lines that contain 'From'
    """
    exu = ExerciseUtils()
    print('re02 Enter')
    print('Searching for ', "'" + search_str + "'", ' in ', fname)
    count = exu.run_search1(fname, search_str)
    print("Lines found containing '" + search_str + "':", count)
    print('re02 Exit')
    return count


fname = 'mbox-short.txt'
search_str = '^From:'
re_search02(fname, search_str)
