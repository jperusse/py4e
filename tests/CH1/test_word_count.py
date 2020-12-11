from CH1.word_count import WordCount
import pytest
from pytest import raises
import os


class TestWordCount():
    """
    Test all methods from WordCount
    """
    fname = "words.txt"
    firstline = "words.txt contains 23 copies of the word 'to', the largest count of all words found: to; to; to"
    next_line = ""

    @pytest.fixture(autouse=False)
    def ReadFirstLine(self):
        self.wc = WordCount()
        fh = self.wc.openfile(self.fname)
        self.next_line = self.wc.read_next_line(fh)

    def test_openfile_raises_file_not_found(self):
        wc = WordCount()
        try:
            wc.openfile("missing.txt")
            assert False
        except:
            assert True

    def test_read_next_line_from_file(self, ReadFirstLine):
        assert self.next_line == self.firstline

    def test_get_word_with_largest_count(self, ReadFirstLine):
        top_word = self.wc.get_word_with_largest_count(self.next_line)
        assert top_word == ["to", 3]

    def test_check_for_newer_largest_count(self):
        fname = "words.txt"
        wc = WordCount()
        fh = wc.openfile(fname)
        line = wc.read_next_line(fh)

        top_word = wc.get_word_with_largest_count(line)
        check_for_newer_largest_count(self)
