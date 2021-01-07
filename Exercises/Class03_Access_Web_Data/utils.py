import re


class ExerciseUtils():
    """
    Test methods common to PY4E exercises
    """

    def openfile(self, fname, mode):
        """
        open a file and do error handling
        """
        try:
            fh = open(fname, mode)
        except:
            # Couldn't open the file
            fh = ""
        return fh

    def run_search1(self, fname, search_str, debug):
        """
        Use re.search to count number of lines containing search_str in fname
        """
        count = 0
        hand = self.openfile(fname, 'r')
        if search_str == "" or hand == "":
            return count

        for line in hand:
            line = line.rstrip()
            if re.search(search_str, line):
                count += 1
                if debug: print(line)
        
        print(count, ' lines found')

        return count


print("re01 - Search for lines that contain 'From'")
exu = ExerciseUtils()
count = exu.run_search1('mbox-short.txt', 'From:', False)
assert count == 27



print("re02 - Search for lines that start with 'From'")
exu = ExerciseUtils()
count = exu.run_search1('mbox-short.txt', '^From:', False)
assert count == 27

