import pytest
from Exercises.Class03_Access_Web_Data.utils import ExerciseUtils


class TestExerciseUtils():
    """
    Test all common utility methods from PY4E exercises
    """
    fname = "words.txt"
    firstline = "words.txt contains 23 copies of the word 'to', the largest count of all words found: to to to"
    next_line = ""
    exu = ExerciseUtils()

    def read_next_line(self, fh):
        try:
            line = fh.readline()
        except:
            line = ''
        return line

    @pytest.fixture(autouse=True)
    def ReadFirstLine(self):
        self.fh = self.exu.openfile(self.fname, 'r')
        self.next_line = self.read_next_line(self.fh)

    def test_openfile_raises_file_not_found(self):
        fh = self.exu.openfile("missing", 'r')
        assert fh == ""

    def test_read_next_line_from_file(self):
        assert self.next_line.strip() == self.firstline

    def test_run_search1_is_empty(self):
        assert self.exu.run_search1("mbox-short.txt", "", False) == 0

    def test_run_search1_is_found(self):
        assert self.exu.run_search1("mbox-short.txt", "From", False) == 54
        assert self.exu.run_search1("mbox-short.txt", "From:", False) == 27
        assert self.exu.run_search1("mbox-short.txt", "^From:", False) == 27
        assert self.exu.run_search1("mbox-short.txt", "^F..m:", False) == 27
        assert self.exu.run_search1('mbox-short.txt', '^From:.+@', False) == 27

    def test_run_search1_is_not_found(self):
        assert self.exu.run_search1("mbox-short.txt", "JIMBO-missing", False) == 0


    def test_run_findall_is_empty(self):
        assert self.exu.run_findall("mbox-short5.txt", "", False) == 0

    def test_run_findall_is_found(self):
        assert self.exu.run_findall("mbox-short5.txt", "\\S+@\\S+", False) == 5
        # Sample each of the special regex characters
        assert self.exu.run_findall("mbox-short5.txt", "^From",     True) == 1  # Matches the beginning of a line
        # assert self.exu.run_findall("mbox-short5.txt", ";$",        True) == 5  # Matches the end of the line
        # assert self.exu.run_findall("mbox-short5.txt", "F...:",     True) == 5  # Matches any character
        # assert self.exu.run_findall("mbox-short5.txt", "\\s+for",   True) == 5  # Matches whitespace
        # assert self.exu.run_findall("mbox-short5.txt", "\\S+-Path", True) == 5  # Matches non-whitespace character
        # assert self.exu.run_findall("mbox-short5.txt", ".*for",     True) == 5  # Repeats a character zero or more times
        # assert self.exu.run_findall("mbox-short5.txt", "\\s*?for",  True) == 5  # zero or more characters (not-greedy)
        # assert self.exu.run_findall("mbox-short5.txt", "\\s+for",   True) == 5  # Repeats a character one or more times
        # assert self.exu.run_findall("mbox-short5.txt", "\\s+?for",  True) == 5  # Repeats a character one or more times (non-greedy)
        # assert self.exu.run_findall("mbox-short5.txt", "[aeiou]",   True) == 5  # Matches a single character in the listed set
        # assert self.exu.run_findall("mbox-short5.txt", "^XYZ",      True) == 5  # Matches a single character not in the listed set
        # assert self.exu.run_findall("mbox-short5.txt", "[a-z0-9]",  True) == 5  # The set of characters can include a range
        # assert self.exu.run_findall("mbox-short5.txt", "(from.+@.+",True) == 5  # Indicates where string extraction is to start and end

    def test_run_findall_is_not_found(self):
        assert self.exu.run_findall("mbox-short5.txt", "JIMBO-missing", False) == 0
