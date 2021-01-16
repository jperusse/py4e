import pytest
from Exercises.Class03_Access_Web_Data.ex_utils import ExerciseUtils


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

    @pytest.fixture(autouse=False)
    def ReadFirstLine(self):
        self.fh = self.exu.openfile(self.fname, 'r')
        self.next_line = self.read_next_line(self.fh)

    def test_openfile_raises_file_not_found(self, ReadFirstLine):
        fh = self.exu.openfile("missing", 'r')
        assert fh == ""

    def test_read_next_line_from_file(self, ReadFirstLine):
        assert self.next_line.strip() == self.firstline

