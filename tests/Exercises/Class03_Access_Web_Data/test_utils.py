# %%
import io
import json
import os
import sys
import xml.etree.ElementTree as ET
from unittest.mock import MagicMock

import pytest
from Exercises.Class03_Access_Web_Data.utils import ExerciseUtils


class TestExerciseUtils:
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
        except BaseException:
            line = ""
        return line

    @pytest.fixture(autouse=False)
    def ReadFirstLine(self):
        if os.path.exists(self.fname):
            self.fh = open(self.fname, "r")
            self.next_line = self.read_next_line(self.fh)
        else:
            self.fh = ""

    def test_read_next_line_from_file(self, ReadFirstLine):
        assert self.next_line.strip() == self.firstline

    def test_run_search1_is_empty(self):
        assert self.exu.run_search1(self.mbox_short, "", False) == 0

    def test_run_search1_is_found(self):
        assert self.exu.run_search1(self.mbox_short, "From",        False) == 54
        assert self.exu.run_search1(self.mbox_short, "From:",       False) == 27
        assert self.exu.run_search1(self.mbox_short, "^From:",      False) == 27
        assert self.exu.run_search1(self.mbox_short, "^F..m:",      False) == 27
        assert self.exu.run_search1(self.mbox_short, "^From:.+@",   False) == 27

    def test_run_search1_is_not_found(self):
        assert self.exu.run_search1(
            self.mbox_short, "JIMBO-missing", False) == 0

    def test_run_findall_is_empty(self):
        assert self.exu.run_findall(self.mbox_short5, "", False) == 0

    def test_run_findall_is_found(self):
        # Sample each of the special regex characters

        assert (self.exu.run_findall(self.mbox_short5, "^From",         True) == 1)  # Matches the beginning of a line
        assert (self.exu.run_findall(self.mbox_short5, ";$",            True) == 3)  # Matches the end of the line
        assert (self.exu.run_findall(self.mbox_short5, "F...",          True) == 1)  # Matches any character
        assert (self.exu.run_findall(self.mbox_short5, "\\s+for",       True) == 2)  # Matches whitespace
        assert (self.exu.run_findall(self.mbox_short5, "\\S+-Path",     True) == 1)  # Matches non-whitespace character
        # Repeats a character zero or more times
        assert (self.exu.run_findall(self.mbox_short5, "\\s*[0-9]",     True) == 9)
        # Repeats a character zero or more times (not-greedy)
        assert (self.exu.run_findall(self.mbox_short5, "\\s*?[0-9]",    True) == 9)
        # Repeats a character one or more times
        assert (self.exu.run_findall(self.mbox_short5, "\\s+[0-9]+",    True) == 7)
        # Repeats a character one or more times (not-greedy)
        assert (self.exu.run_findall(self.mbox_short5, "\\s+?[0-9]+?",  True) == 7)
        assert (self.exu.run_findall(self.mbox_short5, "[aeiou]",       True) == 14)  # Matches single char in set
        assert (self.exu.run_findall(self.mbox_short5, "[^aeiou;]",     True) == 16)   # Matches single char not in set
        assert (self.exu.run_findall(self.mbox_short5, "[a-z]",         True) == 14)   # range of characters
        # Indicates where string extraction is to start and end
        assert (self.exu.run_findall(self.mbox_short5, "\\S+@(\\S+)", True) == 5)

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
            self.mbox_short6, "Counting: ([0-9])", True
        )
        assert count == 12
        assert avg == 2

    def test_run_findall_avg_is_not_found(self):
        count, avg = self.exu.run_findall_avg(
            self.mbox_short6, "JIMBO-missing", False)
        assert count == 0
        assert avg == 0

    def test_split_url_bad_urls(self):
        url_tuple = self.exu.split_url("")
        assert url_tuple == (None, None, None)

        url_prefix, url_base, url_page = self.exu.split_url("")
        assert url_prefix is None and url_base is None and url_page is None

        url_prefix, url_base, url_page = self.exu.split_url("f")
        assert url_prefix == "f" and url_base is None and url_page is None

        url_prefix, url_base, url_page = self.exu.split_url("fred")
        assert url_prefix == "fred" and url_base is None and url_page is None

        url_prefix, url_base, url_page = self.exu.split_url("http://")
        assert url_prefix == "http:" and url_base == "" and url_page is None

        url_prefix, url_base, url_page = self.exu.split_url("http://d")
        assert url_prefix == "http:" and url_base == "d" and url_page is None

        url_prefix, url_base, url_page = self.exu.split_url("http://data")
        assert url_prefix == "http:" and url_base == "data" and url_page is None

        url_prefix, url_base, url_page = self.exu.split_url("http://data.pr4e")
        assert url_prefix == "http:" and url_base == "data.pr4e" and url_page is None

        url_prefix, url_base, url_page = self.exu.split_url("http://data.pr4e.org")
        assert (
            url_prefix == "http:" and url_base == "data.pr4e.org" and url_page is None
        )

        url_prefix, url_base, url_page = self.exu.split_url(
            "http://data.pr4e.org/")
        assert url_prefix == "http:" and url_base == "data.pr4e.org" and url_page == ""

        url_prefix, url_base, url_page = self.exu.split_url(
            "http://data.pr4e.org/p")
        assert url_prefix == "http:" and url_base == "data.pr4e.org" and url_page == "p"

    def test_open_socket_bad_host(self):
        mysock = self.exu.open_socket("", 80)
        assert mysock is None

    def test_open_socket_bad_port(self):
        mysock = self.exu.open_socket(self.exu.url_base, 0)
        assert mysock is None

    def test_open_socket_for_good_host(self):
        mysock = self.exu.open_socket(self.exu.url_base, 80)  # normal socket
        assert mysock is not None

    def test_close_socket_for_good_host(self):
        mysock = self.exu.open_socket(self.exu.url_base, 80)  # normal socket
        assert mysock is not None

        mysock = self.exu.close_socket(mysock)  # normal socket
        assert mysock is not None

    def test_close_socket_for_bad_host(self):
        mysock = None
        mysock = self.exu.close_socket(mysock)  # normal socket
        assert mysock is None

    def test_init_socket_and_url_using_defaults(self):
        mysock, url = self.exu.init_socket_and_url(
            self.exu.url_prefix, self.exu.url_base, self.exu.url_text_doc
        )
        assert mysock is not None
        assert (url == self.exu.url_prefix + "//" + self.exu.url_base + "/" + self.exu.url_text_doc)

    def test_init_socket_and_url_bad_base(self):
        mysock, url = self.exu.init_socket_and_url(
            self.exu.url_prefix, "", self.exu.url_text_doc
        )
        assert mysock is None
        assert url == self.exu.url_prefix + "///" + self.exu.url_text_doc

        mysock, url = self.exu.init_socket_and_url("http:", "data", None)
        assert mysock is None
        assert url == "http://data/"

    def test_get_page_using_defaults(self):
        mysock, url = self.exu.init_socket_and_url(self.exu.url_prefix, self.exu.url_base, self.exu.url_text_doc)

        page = self.exu.get_page(mysock, url)
        assert len(page) == 2

        mysock = self.exu.close_socket(mysock)  # normal socket

        page = self.exu.get_page(mysock, url)
        assert len(page) == 0

    def test_get_page_using_bad_parms(self):
        mysock, url = self.exu.init_socket_and_url(self.exu.url_prefix, self.exu.url_base, self.exu.url_text_doc)

        page = self.exu.get_page(None, url)
        assert len(page) == 0

        page = self.exu.get_page(mysock, "")
        assert len(page) == 0

    def test_print_page_socket(self):
        for limit in [1, 2, 3000]:
            total_chars = self.exu.print_page_limit(self.exu.url_prefix, self.exu.url_base,
                                                    self.mbox_short, limit)  # normal socket
            assert total_chars == 95000

    def test_print_page_socket_bad_url(self):
        total_chars = self.exu.print_page_limit(self.exu.url_prefix, "",
                                                self.mbox_short, 3000, skipheaders=True)  # normal socket
        assert total_chars == 0

    def test_print_page_socket_skipheaders_default(self):
        total_chars = self.exu.print_page_limit(self.exu.url_prefix, self.exu.url_base, self.exu.url_text_doc,
                                                3000)  # normal socket
        assert total_chars == 536

    def test_print_page_socket_skipheaders_override(self):
        total_chars = self.exu.print_page_limit(self.exu.url_prefix, self.exu.url_base, self.exu.url_text_doc,
                                                3000, skipheaders=True)  # normal socket
        assert total_chars == 167

    def test_get_jpeg(self):
        ofile = "stuff.jpg"
        mysock, url = self.exu.init_socket_and_url(self.exu.url_prefix, self.exu.url_base, "cover3.jpg")
        picture = self.exu.get_jpeg(mysock, url)
        assert len(picture) == 230608

        mysock = self.exu.close_socket(mysock)  # normal socket

        img = self.exu.stripheaders_img(picture, ofile)
        assert len(img) == 230210

        rc = self.exu.write_file(ofile, "wb", img)
        assert rc is None

    # def test_get_html_input_good_url(self):
    #     html = self.exu.get_html(self.exu.url_default1)
    #     assert len(html) == 13862
 
    def test_get_html_input_good_default_url(self, monkeypatch):
        monkeypatch.setattr("sys.stdin", io.StringIO("\n"))
        html = self.exu.get_html(None)
        assert len(html) > 0

    def test_get_html_input_good_default_url_no_parms(self, monkeypatch):
        monkeypatch.setattr("sys.stdin", io.StringIO("\n"))
        html = self.exu.get_html()
        assert len(html) > 0

    def test_get_html_input_no_url(self, monkeypatch):
        monkeypatch.setattr("sys.stdin", io.StringIO("\n"))
        html = self.exu.get_html()
        assert len(html) > 0

    def test_get_html_input_bad_url_entered(self, monkeypatch):
        monkeypatch.setattr("sys.stdin", io.StringIO("badurl"))
        html = self.exu.get_html()
        assert len(html) == 0

    def test_get_html_input_bad_url_passed_in(self):
        html = self.exu.get_html("badurl")
        assert len(html) == 0

    # def test_reglinks(self):
    #     html = self.exu.get_html(self.exu.url_default1)
    #     links = self.exu.regexlinks(html)
    #     assert len(links) == 35

    # def test_bs4_tags(self):
    #     len_a = 68
    #     html = self.exu.get_html(self.exu.url_default1)
    #     tags = self.exu.bs4_tags(html, "a", pflags=[False, True, False, False])
    #     assert len(tags) == len_a

    #     html = self.exu.get_html(self.exu.url_default1)
    #     tags = self.exu.bs4_tags(html, "a", pflags=[False, False, False, False])
    #     assert len(tags) == len_a

    #     html = self.exu.get_html(self.exu.url_default1)
    #     tags = self.exu.bs4_tags(html, "a")
    #     assert len(tags) == len_a

    #     html = self.exu.get_html(self.exu.url_default1)
    #     tags = self.exu.bs4_tags(html, "p")
    #     assert len(tags) == 27

    #     html = self.exu.get_html(self.exu.url_default1)
    #     tags = self.exu.bs4_tags(html, "z")
    #     assert len(tags) == 0

    def test_open_url(self):
        fh = self.exu.open_url(self.exu.url_text_doc, None)
        assert fh != ""
        print(fh)

        url = self.exu.url_prefix + "//" + self.exu.url_base
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
        fh = self.exu.open_url(self.exu.url_text_doc, None)
        assert fh != ""

        page = self.exu.get_url_page(fh)
        assert len(page) > 0

    def test_print_page_urllib(self):
        char_count = self.exu.print_page_urllib(self.mbox_short, 3000)
        assert char_count == 94626

    def test_getwords(self):

        fh = open(self.exu.url_text_doc, "r")
        assert fh != ""

        count = self.exu.getwords(fh)
        assert len(count) == 26
        print(count)

    def test_getwords_from_url(self):
        fh = self.exu.open_url(self.exu.url_text_doc, None)
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
        assert rc is None

    def test_open_url_large_img_save(self):
        file = "cover3.jpg"
        img = self.exu.open_url(file, None)
        assert img != ""

        count = self.exu.get_url_large_img_and_save(img, file)
        assert count == 230210
        print(count, "characters copied.")

    def test_buildurl_with_default_components(self):
        """
        Build a full URL from the document provided
        """
        url_doc = self.exu.url_text_doc
        url = self.exu.buildurl(self.exu.url_prefix,
                                self.exu.url_base, url_doc)
        assert url == "http://data.pr4e.org/" + url_doc
        print(url)

    def test_buildurl_with_bad_values(self):
        """
        Build a full URL from the document provided
        """
        url = self.exu.buildurl("", "", "")
        assert url == "///"
        url = self.exu.buildurl(None, None, None)
        assert url == "///"

        url = self.exu.buildurl("f", "", "")
        assert url == "f///"

        url = self.exu.buildurl("http:", "", "")
        assert url == "http:///"

        url = self.exu.buildurl("http:", None, None)
        assert url == "http:///"

        url = self.exu.buildurl("http:", "data", None)
        assert url == "http://data/"

        url = self.exu.buildurl("http:", "data.pr4e.org", "p")
        assert url == "http://data.pr4e.org/p"

    def test_ignore_ssl_errors(self):
        ctx = self.exu.ignore_ssl_errors()
        assert ctx.check_hostname == False

    def test_findlinks_regex(self):
        ctx = self.exu.ignore_ssl_errors()
        html = self.exu.open_url("https://docs.python.org", ctx)
        assert len(html) > 0
        assert isinstance(html, type(b""))

        links = list()
        regex = 'href="(http[s]?://.*?)"'.encode()
        links = self.exu.findall_html(html, regex)
        assert len(links) > 0
        assert isinstance(links, list)

    def test_findlinks_bs4(self):
        ctx = self.exu.ignore_ssl_errors()
        html = self.exu.open_url("https://docs.python.org", ctx)
        assert len(html) > 0
        assert isinstance(html, type(b""))

        links = list()
        regex = 'href="(http[s]?://.*?)"'.encode()
        links = self.exu.findall_html(html, regex)
        assert len(links) > 0
        assert isinstance(links, list)

    def init_test_xml(self, capsys):
        print()
        # capture all previous print statements
        captured = capsys.readouterr()
        assert captured.out == "\n"

        xml_tree = '''
        <person x="999">
            <name>James</name>
            <phone type="intl">
                +1 734 303 4456
            </phone>
            <email hide="yes" />
        </person>'''
        intr_tree = self.exu.InternetTreeXML(xml_tree)
        intr_tree.create_tree()
        return intr_tree

    def print_elements_xml(self, capsys, field_list):
        intr_tree = self.init_test_xml(capsys)
        count = intr_tree.print_element_tree(field_list)
        assert count == len(field_list)
        captured = capsys.readouterr()
        return captured

    def test_print_element_tree_text(self, capsys):
        field_list = [("Name:", "name", "text", "")]
        captured = self.print_elements_xml(capsys, field_list)
        assert captured.out == 'Number of tuples found:  1\nName: James\n'

    def test_print_element_tree_attr(self, capsys):
        field_list = [("Attr:", "email", "attr", "hide")]
        captured = self.print_elements_xml(capsys, field_list)
        assert captured.out == 'Number of tuples found:  1\nAttr: yes\n'

    def test_print_element_tree_attr_no_field_specified(self, capsys):
        field_list = [("Attr:", "", "attr", "x")]
        captured = self.print_elements_xml(capsys, field_list)
        assert captured.out == 'Number of tuples found:  1\nAttr: 999\n'

    def test_print_element_tree_text_and_attr(self, capsys):
        field_list = [("Name:", "name", "text", ""), ("Attr:", "email", "attr", "hide")]
        captured = self.print_elements_xml(capsys, field_list)
        assert captured.out == 'Number of tuples found:  2\nName: James\nAttr: yes\n'

    def test_print_element_tree_bad_field_data(self, capsys):
        field_list = [("Name:", "name", "text")]
        captured = self.print_elements_xml(capsys, field_list)
        assert captured.out == 'Number of tuples found:  1\nNumber of fields incorrect and will be ignored:  3\n'

    def test_print_element_tree_field_not_found_text(self, capsys):
        field_list = [("Name:", "missing", "text", "")]
        captured = self.print_elements_xml(capsys, field_list)
        assert captured.out == 'Number of tuples found:  1\nField not found:  missing\n'

    def test_print_element_tree_attr_name_missing(self, capsys):
        field_list = [("Attr:", "missing", "attr", "")]
        captured = self.print_elements_xml(capsys, field_list)
        assert captured.out == "Number of tuples found:  1\nAttribute name is missing\n"

    def test_print_element_tree_field_and_attr_name_missing(self, capsys):
        field_list = [("Attr:", "", "attr", "")]
        captured = self.print_elements_xml(capsys, field_list)
        assert captured.out == "Number of tuples found:  1\nAttribute name is missing\n"

    def test_print_element_tree_attr_not_found1(self, capsys):
        field_list = [("Attr:", "email", "attr", "hidden")]
        captured = self.print_elements_xml(capsys, field_list)
        assert captured.out == "Number of tuples found:  1\nAttribute not found: 'hidden'\n"

    def test_print_element_tree_attr_not_found2(self, capsys):
        field_list = [("Attr:", "", "attr", "hidden")]
        captured = self.print_elements_xml(capsys, field_list)
        assert captured.out == "Number of tuples found:  1\nAttribute not found: 'hidden'\n"

    def init_test_json(self):
        json_tree = '''
        [
            {
                "x" : "999"
            } ,
            {
                "name" : "James",
                "phone" : "+1 734 303 4456",
                "phone type" : "intl",
                "email hide" : "yes"
            }
        ]'''
        intr_tree = self.exu.InternetTreeJSON(json_tree)
        intr_tree.create_tree_list()

        return intr_tree

    def print_elements_json(self, capsys, field_list):
        intr_tree = self.init_test_json()
        print()
        # capture all previous print statements
        captured = capsys.readouterr()
        assert captured.out == "\n"

        count = intr_tree.print_element_tree(field_list)
        assert count == len(field_list)
        captured = capsys.readouterr()
        return captured

    def test_print_element_tree_text_json(self, capsys):
        field_list = [("Name:", "name", "text", "")]
        captured = self.print_elements_json(capsys, field_list)
        assert captured.out == 'Number of tuples found:  1\nName: James\n'

    def test_print_element_tree_attr_json(self, capsys):
        field_list = [("Attr:", "email hide", "text", "")]
        captured = self.print_elements_json(capsys, field_list)
        assert captured.out == 'Number of tuples found:  1\nAttr: yes\n'

    def test_print_element_tree_attr_no_field_specified_json(self, capsys):
        field_list = [("Attr:", "x", "text", "")]
        captured = self.print_elements_json(capsys, field_list)
        assert captured.out == 'Number of tuples found:  1\nAttr: 999\n'

    def test_print_element_tree_text_and_attr_json(self, capsys):
        field_list = [("Name:", "name", "text", ""), ("Attr:", "email hide", "text", "")]
        captured = self.print_elements_json(capsys, field_list)
        assert captured.out == 'Number of tuples found:  2\nName: James\nAttr: yes\n'

    def test_print_element_tree_bad_field_data_json(self, capsys):
        field_list = [("Name:", "name", "text")]
        captured = self.print_elements_json(capsys, field_list)
        assert captured.out == 'Number of tuples found:  1\nNumber of fields incorrect and will be ignored:  3\n'

    def test_print_element_tree_field_not_found_text_json(self, capsys):
        field_list = [("Name:", "missing", "text", "")]
        captured = self.print_elements_json(capsys, field_list)
        assert captured.out == 'Number of tuples found:  1\nField not found:  missing\n'

    def test_print_element_tree_attr_not_found1_json(self, capsys):
        field_list = [("Attr:", "email hidden", "text", "")]
        captured = self.print_elements_json(capsys, field_list)
        assert captured.out == "Number of tuples found:  1\nField not found:  email hidden\n"

    def test_print_element_tree_attr_not_found2_json(self, capsys):
        field_list = [("Attr:", "", "text", "")]
        captured = self.print_elements_json(capsys, field_list)
        assert captured.out == "Number of tuples found:  1\nField not found:  \n"

    def test_create_tree_list(self):
        intr_tree = self.init_test_json()
        intr_tree.create_tree_list
        tree_list = intr_tree.tree_list
        assert type(tree_list) == list

    def test_tree_list_count(self):
        intr_tree = self.init_test_json()
        intr_tree.create_tree_list
        assert intr_tree.tree_list_count() == 2

    def test_get_tree_list(self):
        intr_tree = self.init_test_json()
        intr_tree.create_tree_list
        tree_list = intr_tree.tree_list
        assert intr_tree.get_tree_list() == tree_list

    def test_findtext_found(self):
        intr_tree = self.init_test_json()
        intr_tree.create_tree_list
        intr_tree.replace_tree(intr_tree.tree_list[0])
        assert intr_tree.findtext("name") == "James"

    def test_findtext_not_found(self):
        intr_tree = self.init_test_json()
        intr_tree.create_tree_list
        intr_tree.replace_tree(intr_tree.tree_list[0])
        assert intr_tree.findtext("missing") == None
