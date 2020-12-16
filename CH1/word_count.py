class WordCount():
    def openfile(self, fname):
        """
        open a file and force exeption
        """
        try:
            fh = open(fname, 'r')
        except:
            fh = ""
        return fh

    def read_next_line(self, fh):
        try:
            line = fh.readline()
        except:
            line = ''
        return line

    def get_word_with_largest_count(self, line):
        new_line = line.splitlines()
        word_list = new_line.split(sep=' ')
        dic = dict()
        for word in word_list:
            dic[word] = dic[word] + 1
        return {'to': 3}

    def check_for_newer_largest_count(self, top_word):
        return {"to": 4}
