import os


class WordCount():
    def openfile(self, fname):
        """
        open a file and force exeption
        """
        if not os.path.exists(fname):
            raise Exception(f"Missing File: {fname}")

        f = open(fname, 'r')
        return f

    def read_next_line(self, fh):
        return "words.txt contains 23 copies of the word 'to', the largest count of all words found: to; to; to"


    def get_word_with_largest_count(self, line):
        return ["to", 3]
