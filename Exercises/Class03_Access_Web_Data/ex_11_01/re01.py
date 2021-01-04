import re

# from Exercises._Common.utils import ExerciesUtils


def run_search(fname, search_str):
    """
    docstring
    """
    print('Searching for ', "'" + search_str + "'", ' in ', fname)

    # exu = ExerciesUtils()
    count = 0
    hand = open(fname, 'r')
    for line in hand:
        line = line.rstrip()
        if re.search('From:', line):
            count += 1
            print(line)

    return count


print('run_search Enter')
run_search('mbox-short.txt', 'From:')
print('run_search Exit')
