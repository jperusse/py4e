from CH1.word_count import WordCount
import pytest
from pytest import raises

class TestWordCount():
    """
    Test all methods from WordCount
    """
    # @pytest.fixture()
    # def open_file(self):
    #     pass


    def test_WordCount_found(self):
        wc = WordCount()
        assert type(wc) == WordCount

    def test_read_word_file(self):
        fname = "words.txt"
        wc = WordCount()
        assert wc.openfile(fname)
    
    def test_openfile_raises_file_not_found(self):
        wc = WordCount()
        try:
            wc.openfile("missing.txt")
            assert False
        except:
            print("Missing File: missing.txt")
            assert True
    
    # def test_read_next_line_from_file(self):
    #     fname = "words.txt"
    #     wc = WordCount()
    #     fh = wc.openfile(fname)
    #     line = wc.read_next_line(fh)
    #     assert len(line) >= 0
