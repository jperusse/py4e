from Exercises.Class03_Access_Web_Data.utils import ExerciseUtils
import pytest


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
        assert self.exu.run_search1("mbox-short.txt", "") == 0

    def test_run_search1_is_found(self):
        assert self.exu.run_search1("mbox-short.txt", "From") == 54

    def test_run_search1_is_not_found(self):
        assert self.exu.run_search1("mbox-short.txt", "JIMBO-missing") == 0
