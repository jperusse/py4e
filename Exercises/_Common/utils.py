class ExerciesUtils():
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
            fh = None
        return fh