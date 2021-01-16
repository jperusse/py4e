from ex_re_utils import ExerciseUtils

print("re01 - Search for lines that contain 'From'")
exu = ExerciseUtils()
count = exu.run_search1('mbox-short.txt', 'From:', False)
assert count == 27

print("re02 - Search for lines that start with 'From'")
exu = ExerciseUtils()
count = exu.run_search1('mbox-short.txt', '^From:', False)
assert count == 27

print("re03 - Search for lines that start with 'F', followed by 2 characters, followed by 'm:'")
exu = ExerciseUtils()
count = exu.run_search1('mbox-short.txt', '^F..m:', False)
assert count == 27

print("re04 - Search for lines that start with From and have an '@' sign")
exu = ExerciseUtils()
count = exu.run_search1('mbox-short.txt', '^From:.+@', False)
assert count == 27

print("re05 - Search for an address")
exu = ExerciseUtils()
count = exu.run_findall('mbox-short5.txt', '\\S+@\\S+', False)
assert count == 5

print("re06 - Search for lines that have an at sign between characters")
exu = ExerciseUtils()
count = exu.run_findall('mbox-short.txt', '\\S+@\\S+', False)
assert count == 336

print("re07 - Search for lines that have an at sign between characters")
exu = ExerciseUtils()
count = exu.run_findall(
    'mbox.txt', '[a-zA-Z0-9][a-zA-Z0-9.]*@[a-zA-Z][a-zA-Z.]*', False)
assert count == 22009

print("re10 - Search for lines that start with 'X' followed by any non whitespace characters and ':' followed by a space and any number. The number can include a decimal.")
exu = ExerciseUtils()
count = exu.run_search1('mbox-short.txt', 'X\\S*: [0-9.]+', False)
assert count == 54

print("re11 - Search for lines that start with 'X' followed by any non whitespace characters and ':' followed by a space and any number. The number can include a decimal.")
exu = ExerciseUtils()
count = exu.run_findall('mbox-short.txt', 'X\\S*: ([0-9.]+)', False)
assert count == 54

print("re13 - Search for lines that start with From and a character followed by a two digit number between 00 and 99 followed by ':'. Then print the number if it is greater than zero.")
exu = ExerciseUtils()
count = exu.run_findall('mbox-short.txt', '^From .* ([0-9][0-9]):', False)
assert count == 27
