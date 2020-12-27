from CH1.word_count import WordCount
import pytest


class TestWordCount():
    """
    Test all methods from WordCount
    """
    fname = "words.txt"
    firstline = "words.txt contains 23 copies of the word 'to', the largest count of all words found: to to to"
    next_line = ""

    def read_next_line(self, fh):
        try:
            line = fh.readline()
        except:
            line = ''
        return line

    @pytest.fixture(autouse=True)
    def ReadFirstLine(self):
        self.wc = WordCount()
        self.wc.all_words = dict()
        self.fh = self.wc.openfile(self.fname)
        self.next_line = self.read_next_line(self.fh)

    def test_openfile_raises_file_not_found(self):
        fh = self.wc.openfile("missing")
        assert fh == ""

    def test_read_next_line_from_file(self):
        assert self.next_line.strip() == self.firstline

    def test_get_word_with_largest_count(self):
        top_word = self.wc.get_word_with_largest_count(self.next_line)
        assert top_word == {'to': 3}
        
    def test_dict_elem(self):
        value = self.wc.dict_elem_value({'to': 3})
        assert value == 3


    def test_read_2nd_line_and_check_for_largest_count(self):
        top_word = self.wc.get_word_with_largest_count(self.next_line)
        another_line = self.read_next_line(self.fh)
        top_word_another_line = self.wc.get_word_with_largest_count(another_line)
        top_word = self.wc.check_for_newer_largest_count(top_word, top_word_another_line)
        assert top_word == {'to':7}
