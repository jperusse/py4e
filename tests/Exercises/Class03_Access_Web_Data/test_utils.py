import re

import pytest
from Exercises.Class03_Access_Web_Data.utils import ExerciseUtils

from unittest.mock import MagicMock
import io


class TestExerciseUtils():
    """
    Test all common utility methods from PY4E exercises
    """
    fname = "words.txt"
    firstline = "words.txt contains 23 copies of the word 'to', the largest count of all words found: to to to"
    next_line = ""
    exu = ExerciseUtils()
    mbox_short = "mbox-short.txt"
    mbox_short5 = "mbox-short5.txt"
    mbox_short6 = "mbox-short6.txt"

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

    def test_run_search1_is_empty(self):
        assert self.exu.run_search1(self.mbox_short, "", False) == 0

    def test_run_search1_is_found(self):
        assert self.exu.run_search1(self.mbox_short, "From", False) == 54
        assert self.exu.run_search1(self.mbox_short, "From:", False) == 27
        assert self.exu.run_search1(self.mbox_short, "^From:", False) == 27
        assert self.exu.run_search1(self.mbox_short, "^F..m:", False) == 27
        assert self.exu.run_search1(self.mbox_short, '^From:.+@', False) == 27

    def test_run_search1_is_not_found(self):
        assert self.exu.run_search1(
            self.mbox_short, "JIMBO-missing", False) == 0

    def test_run_findall_is_empty(self):
        assert self.exu.run_findall(self.mbox_short5, "", False) == 0

    def test_run_findall_is_found(self):
        # Sample each of the special regex characters

        assert self.exu.run_findall(
            self.mbox_short5, "^From",         True) == 1  # Matches the beginning of a line
        assert self.exu.run_findall(
            self.mbox_short5, ";$",            True) == 3  # Matches the end of the line
        assert self.exu.run_findall(
            self.mbox_short5, "F...",          True) == 1  # Matches any character
        assert self.exu.run_findall(
            self.mbox_short5, "\\s+for",       True) == 2  # Matches whitespace
        assert self.exu.run_findall(
            self.mbox_short5, "\\S+-Path",     True) == 1  # Matches non-whitespace character
        assert self.exu.run_findall(
            self.mbox_short5, "\\s*[0-9]",     True) == 9  # Repeats a character zero or more times
        assert self.exu.run_findall(
            self.mbox_short5, "\\s*?[0-9]",    True) == 9  # Repeats a character zero or more times (not-greedy)
        assert self.exu.run_findall(
            self.mbox_short5, "\\s+[0-9]+",    True) == 7  # Repeats a character one or more times
        assert self.exu.run_findall(
            self.mbox_short5, "\\s+?[0-9]+?",  True) == 7  # Repeats a character one or more times (not-greedy)
        assert self.exu.run_findall(
            self.mbox_short5, "[aeiou]",       True) == 14  # Matches a single character in the listed set
        assert self.exu.run_findall(
            self.mbox_short5, "[^aeiou;]",     True) == 16  # Matches a single character not in the listed set
        assert self.exu.run_findall(
            self.mbox_short5, "[a-z]",         True) == 14  # The set of characters can include a range
        assert self.exu.run_findall(
            self.mbox_short5, "\\S+@(\\S+)",   True) == 5  # Indicates where string extraction is to start and end

    def test_run_findall_is_not_found(self):
        assert self.exu.run_findall(
            self.mbox_short5, "JIMBO-missing", False) == 0

    def test_run_findall_avg_is_empty(self):
        count, avg = self.exu.run_findall_avg(self.mbox_short, "", True)
        assert count == 0
        assert avg == 0

    def test_run_findall_avg_is_found(self):
        # Sample each of the special regex characters
        # skipped because string is not an number
        count, avg = self.exu.run_findall_avg(self.mbox_short6, "^From", True)
        assert count == 0
        assert avg == 0

        count, avg = self.exu.run_findall_avg(
            self.mbox_short6, "Counting: ([0-9])", True)
        assert count == 12
        assert avg == 2

    def test_run_findall_avg_is_not_found(self):
        count, avg = self.exu.run_findall_avg(
            self.mbox_short6, "JIMBO-missing", False)
        assert count == 0
        assert avg == 0

    def test_open_socket_bad_host(self):
        mysock = self.exu.open_socket("", 80)
        assert mysock == None

    def test_open_socket_bad_port(self):
        mysock = self.exu.open_socket(self.exu.url_base, 0)
        assert mysock == None

    def test_open_socket_for_good_host(self):
        mysock = self.exu.open_socket(self.exu.url_base, 80)  # normal socket
        assert mysock._closed == False

    def test_close_socket_for_good_host(self):
        mysock = self.exu.open_socket(self.exu.url_base, 80)  # normal socket
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

    def test_get_html_input_good_url(self):
        html = self.exu.get_html(self.exu.url_default1)
        assert len(html) > 0

    def test_get_html_input_good_default_url(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO("\n"))
        html = self.exu.get_html(None)
        assert len(html) > 0

    def test_get_html_input_good_default_url_no_parms(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO("\n"))
        html = self.exu.get_html()
        assert len(html) > 0

    def test_get_html_input_no_url(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO("\n"))
        html = self.exu.get_html()
        assert len(html) > 0

    def test_get_html_input_bad_url_entered(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO("badurl"))
        html = self.exu.get_html()
        assert len(html) == 0

    def test_get_html_input_bad_url_passed_in(self):
        html = self.exu.get_html("badurl")
        assert len(html) == 0

    def test_reglinks(self):
        html = self.exu.get_html(self.exu.url_default1)
        links = self.exu.regexlinks(html)
        assert len(links) == 20

    def test_bs4_tags(self):
        html = self.exu.get_html(self.exu.url_default1)
        tags = self.exu.bs4_tags(html)
        assert len(tags) == 48

    def test_bs4_tags2(self):
        html = self.exu.get_html(self.exu.url_default1)
        tags = self.exu.bs4_tags2(html)
        assert len(tags) == 48

    def test_open_url(self):
        fh = self.exu.open_url("romeo.txt", None)
        assert fh != ""
        print(fh)

        url = self.exu.url_prefix + self.exu.url_base
        fh = self.exu.open_url(url, None)
        assert fh != ""
        print(fh)

        ctx = self.exu.ignore_ssl_errors()
        url = "https://docs.python.org"
        html = self.exu.open_url(url, ctx)
        assert html != ""
        print(html)

    def test_open_url_bad_url(self):
        empty = ""
        missing = "fred.txt"
        fh = self.exu.open_url(empty, None)
        assert fh == empty

        fh = self.exu.open_url(missing, None)
        assert fh == empty

        ctx = self.exu.ignore_ssl_errors()
        html = self.exu.open_url(missing, ctx)
        assert html == empty

    def test_get_url_page(self):
        fh = self.exu.open_url("romeo.txt", None)
        assert fh != ""

        page = self.exu.get_url_page(fh)
        assert len(page) > 0

    def test_getwords(self):
        fh = self.exu.openfile("romeo.txt", "r")
        assert fh != ""

        count = self.exu.getwords(fh)
        assert len(count) == 26
        print(count)

    def test_getwords_from_url(self):
        fh = self.exu.open_url("romeo.txt", None)
        assert fh != ""

        page = self.exu.get_url_page(fh)
        assert len(page) > 0

        count = self.exu.getwords(page)
        assert len(count) == 26
        print(count)

    def test_open_url_small_img_and_save(self):
        img = self.exu.open_url_small_img("cover3.jpg", None)
        assert len(img) == 230210

        rc = self.exu.write_file("cover3.jpg", "wb", img)
        assert rc == None

    def test_open_url_large_img_save(self):
        file = "cover3.jpg"
        img = self.exu.open_url(file, None)
        assert img != ""

        count = self.exu.get_url_large_img_and_save(img, file)
        assert count == 230210
        print(count, 'characters copied.')

    def test_buildurl(self):
        """
        Build a full URL from the document proided
        """
        url_doc = "romeo.txt"
        url = self.exu.buildurl(self.exu.url_prefix,
                                self.exu.url_base, url_doc)
        assert url == "http://data.pr4e.org/" + url_doc
        print(url)

    def test_ignore_ssl_errors(self):
        ctx = self.exu.ignore_ssl_errors()
        assert ctx.check_hostname == False

    def test_findlinks_regex(self):
        ctx = self.exu.ignore_ssl_errors()
        html = self.exu.open_url("https://docs.python.org", ctx)
        assert len(html) > 0
        assert type(html) == type(b'')

        links = list()
        regex = 'href="(http[s]?://.*?)"'.encode()
        links = self.exu.findall_html(html, regex)
        assert len(links) > 0
        assert type(links) == type([])

    def test_findlinks_bs4(self):
        ctx = self.exu.ignore_ssl_errors()
        html = self.exu.open_url("https://docs.python.org", ctx)
        assert len(html) > 0
        assert type(html) == type(b'')

        links = list()
        regex = 'href="(http[s]?://.*?)"'.encode()
        links = self.exu.findall_html(html, regex)
        assert len(links) > 0
        assert type(links) == type([])
