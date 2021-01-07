# Search for lines that contain 'From'
from Exercises.Class03_Access_Web_Data.utils import ExerciseUtils
# from utils import ExerciseUtils


def re_search01(fname, search_str):
    """
    Search for lines that contain 'From'
    """
    exu = ExerciseUtils()
    print('re01 Enter')
    print('Searching for ', "'" + search_str + "'", ' in ', fname)
    count = exu.run_search1(fname, search_str)
    print("Lines found containing '" + search_str + "':", count)
    print('re01 Exit')
    return count


fname = 'mbox-short.txt'
search_str = 'From:'
re_search01(fname, search_str)
