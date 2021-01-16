import pytest
from Exercises.Class03_Access_Web_Data.ex_net_utils import ExerciseUtils


class TestExerciseUtils():
    """
    Test all common utility methods from PY4E exercises
    """
    exu = ExerciseUtils()

    def test_open_socket_bad_host(self):
        mysock = self.exu.open_socket("", 80)
        assert mysock == None

    def test_open_socket_bad_port(self):
        mysock = self.exu.open_socket("data.pr4e.org", 0)
        assert mysock == None

    def test_open_socket_for_good_host(self):
        mysock = self.exu.open_socket("data.pr4e.org", 80)  # normal socket
        assert mysock._closed == False

    def test_close_socket_for_good_host(self):
        mysock = self.exu.open_socket("data.pr4e.org", 80)  # normal socket
        assert mysock._closed == False

        mysock = self.exu.close_socket(mysock)  # normal socket
        assert mysock._closed

    def test_get_page(self):
        mysock, url = self.exu.init_socket("romeo.txt")

        page = self.exu.get_page(mysock, url)
        assert len(page) == 2

        mysock = self.exu.close_socket(mysock)  # normal socket
        assert mysock._closed

        page = self.exu.get_page(mysock, url)
        assert len(page) == 0

    def test_get_jpeg(self):
        ofile = "stuff.jpg"
        mysock, url = self.exu.init_socket("cover3.jpg")

        picture = self.exu.get_jpeg(mysock, url)
        assert len(picture) == 230608

        mysock = self.exu.close_socket(mysock)  # normal socket
        assert mysock._closed

        img = self.exu.stripheaders_img(picture, ofile)
        assert len(img) == 230210

        rc = self.exu.write_file(ofile, "wb", img)
        assert rc == None

    def test_open_url(self):
        fh = self.exu.open_url("romeo.txt")
        assert fh != ""

    def test_open_url_bad_url(self):
        fh = self.exu.open_url("")
        assert fh == ""

        fh = self.exu.open_url("fred.txt")
        assert fh == ""

    def test_get_url_page(self):
        fh = self.exu.open_url("romeo.txt")
        assert fh != ""

        page = self.exu.get_url_page(fh)
        assert len(page) > 0

    def test_getwords(self):
        fh = self.exu.open_url("romeo.txt")
        assert fh != ""

        page = self.exu.get_url_page(fh)
        assert len(page) > 0

        count = self.exu.getwords(page)
        assert len(count) == 26
        print(count)

    def test_open_url_small_img_and_save(self):
        img = self.exu.open_url_small_img("cover3.jpg")
        assert len(img) == 230210

        rc = self.exu.write_file("cover3.jpg", "wb", img)
        assert rc == None

    def test_open_url_large_img_save(self):
        file = "cover3.jpg"
        img = self.exu.open_url(file)
        assert img != ""

        count = self.exu.get_url_large_img_and_save(img, file)
        assert count == 230210
        print(count, 'characters copied.')
