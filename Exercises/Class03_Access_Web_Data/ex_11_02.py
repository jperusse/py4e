from utils import ExerciseUtils

print('ex_11_02 - Write a program to look for lines of the form: New Revision: 39772 \n \
    Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.')

files = ["mbox.txt", "mbox-short.txt"]

exu = ExerciseUtils()
for file in files:
    count, avg = exu.run_findall_avg(file, "^New Revision: ([0-9]+)", True)
    print("Found ", str(count), " Average is " + str(avg) + " for file " + file)
