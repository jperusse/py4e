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