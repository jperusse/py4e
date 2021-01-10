from utils import ExerciseUtils

print('ex_11_01 - Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular expression and count the number of lines that matched the regular expression')

regex_list =list()
regex = input("Enter a regular expression: ")
regex_list.append(regex)
if len(regex_list) > 0:
    regex_list = ["^Author", "^X-", "java$"]

exu = ExerciseUtils()
for regex in regex_list:
    count = exu.run_search1('mbox.txt', regex, False)
