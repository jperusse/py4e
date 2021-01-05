# Search for lines that contain 'From'

# from Exercises._Common.utils import ExerciseUtils

fname = 'mbox-short.txt'
search_str = 'From:'

exu = ExerciseUtils()
print('run_search Enter')
print('Searching for ', "'" + search_str + "'", ' in ', fname)
exu.run_search(fname, search_str)
print('run_search Exit')
