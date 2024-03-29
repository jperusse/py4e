from asyncio.windows_events import NULL
import json
import os
import re
import socket
import ssl
import time
import urllib.request
import xml.etree.ElementTree as ET

# import requests  # requests is more advanced than urllib and does automatic decoding
from bs4 import BeautifulSoup


class ExerciseUtils():
    """
    Utility methods common to PY4E exercises
    """
    url_prefix = "http:"
    url_base = "data.pr4e.org"
    url_default1 = "https://docs.python.org"
    url_default2 = "http://www.dr-chuck.com/page1.htm"
    url_default3 = "http://data.pr4e.org/mbox-short.txt"
    url_default4 = "http://data.pr4e.org/"
    # url_default4 = "https://www.py4e.com/html3/12-network"

    url_text_doc = "romeo.txt"

    mbox_trace = "mbox_trace.txt"

    #
    # Base utility methods
    #
    def write_file(self, file, mode, list):
        fhand = open(file, mode)
        fhand.write(list)
        rc = fhand.close()
        return rc

    def getwords(self, fhand):
        count = dict()
        for line in fhand:
            lines = line.split()
            for word in lines:
                count[word] = count.get(word, 0) + 1
        return count
#
# Regex methods
#

    def split_url(self, url):
        errmsg = "Bad URL"
        url_list = [None, None, None, None]

        if len(url) == 0:
            print(errmsg)
        else:
            # valid URL pattern
            url_list_new = url.split("/")
            print("Trying URL:", url)
            for idx in range(len(url_list_new)):
                url_list[idx] = url_list_new[idx]
            print(url_list)

        return url_list[0], url_list[2], url_list[3]

    def run_search1(self, fname, search_str, debug):
        """
        Use re.search to count number of lines containing search_str in fname
        """
        count = 0
        if search_str == "" or not os.path.exists(fname):
            return count

        hand = open(fname, 'r')
        for line in hand:
            line = line.rstrip()
            if re.search(search_str, line):
                count += 1
                if debug:
                    print(line)

        print(fname + " had " + str(count) +
              " lines that matched '" + search_str + "'")

        return count

    def run_findall(self, fname, search_str, debug):
        """
        Use re.findall to extract a list with matching elements to count number of lines containing search_str in fname
        """
        count = 0
        wh = None
        hand = open(fname, 'r')
        if search_str == "" or hand == "":
            return count

        if debug:
            wh = open(self.mbox_trace, "w")

        for line in hand:
            line = line.rstrip()
            lst = re.findall(search_str, line)

            if len(lst) > 0:
                count += 1
                if debug:
                    print(lst, file=wh)

        print(count, " lines found for regex '" + search_str + "'")
        return count

    def run_findall_avg(self, fname, search_str, debug):
        """
        Use re.findall to extract a list with matching elements to count number of lines containing search_str in fname
        """
        count = 0
        total = 0
        wh = None
        hand = open(fname, 'r')
        if search_str == "" or hand == "":
            return [0, 0]

        if debug:
            wh = open(self.mbox_trace, "w")

        for line in hand:
            line = line.rstrip()
            lst = re.findall(search_str, line)

            if len(lst) > 0:
                value = lst[0]
                try:
                    value = int(value)
                except:
                    continue

                count += 1
                total = total + value
                if debug:
                    print(lst, file=wh)

        if count > 0:
            avg = total // count  # use integer division
        else:
            avg = 0

        return [count, avg]

#
#   Network methods
#
    def get_html(self, url=None):
        ctx = self.ignore_ssl_errors()
        if url is None:
            url = input("Enter url(default:" + self.url_default1 + "): ")
            if url == "":
                url = self.url_default1

        html = self.open_url(url, ctx)
        return html

    def regexlinks(self, html):
        links = list()
        regex = 'href="(http[s]?://.*?)"'.encode()
        links = self.findall_html(html, regex)
        for link in links:
            print(link.decode())
        return links

    def bs4_tags(self, html, tag_type, pflags=[True, True, True, True]):
        tags = list()
        valid_tags = ["a", "p"]
        if tag_type in valid_tags:
            soup = BeautifulSoup(html, 'html.parser')

            # Retrieve all of the anchor tags
            tags = soup(tag_type)
            for tag in tags:
                self.tag_func(tag, pflags)
        return tags

    def tag_func(self, tag, pflags):

        # Look at the parts of a tag
        if pflags[0]:
            if tag is not None:
                print('TAG:', tag)
        if pflags[1]:
            tag_print = tag.get('href', None)
            if tag_print is not None:
                print('URL:', tag_print)
        if pflags[2]:
            tag_print = tag.contents
            tag_contents_count = len(tag.contents)
            if (tag_contents_count > 0):
                print('Contents:', tag.contents[0])
            else:
                print('Contents:')
        if pflags[3]:
            tag_print = tag.attrs
            if tag_print is not None:
                print('Attrs:', tag_print)

    def findall_html(self, html, regex):
        # bytes_regex = regex.encode()

        # ctx = ssl.create_default_context()
        # ctx.check_hostname = False
        # ctx.verify_mode = ssl.CERT_NONE

        # # lst = re.findall(b'href="(http[s]?://.*?)"', html)
        # html = urllib.request.urlopen(url, context=ctx).read()

        lst = re.findall(regex, html)

        return lst

    def ignore_ssl_errors(self):
        """
        Return an object used to ignore SSL errors when opening an HTTPS url
        """
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        return ctx

    def open_url(self, url_page, ctx=None):
        if url_page == "":
            return ""
        elif url_page.strip().startswith("http"):
            url = url_page
        else:
            url = self.buildurl(self.url_prefix, self.url_base, url_page)

        if ctx is None:
            try:
                fh = urllib.request.urlopen(url)
            except:
                print("Failed to open ", url)
                return ""

        else:
            try:
                fh = urllib.request.urlopen(url, context=ctx).read()
            except:
                print("Failed to open ", url)
                return ""

        return fh

    def open_url_small_img(self, url_page, ctx):
        if url_page == "":
            return ""

        url = self.buildurl(self.url_prefix, self.url_base, url_page)
        try:
            img = urllib.request.urlopen(url, context=ctx).read()
        except:
            print("Failed to open ", url)
            return ""

        return img

    def buildurl(self, url_prefix, url_base, url_page):
        if url_prefix is None:
            url_prefix = ""
        if url_base is None:
            url_base = ""
        if url_page is None:
            url_page = ""
        url = url_prefix + "//" + url_base + "/" + url_page
        return url

    def get_url_page(self, fhand):
        '''
        Get and decode a URL page returning it as a string
        '''
        page = ""
        for line in fhand:
            print(line.decode().strip())
            page = page + line.decode()

        return [page]

    def get_url_large_img_and_save(self, img, ofile):
        """
        retrieve web page using a buffer for large files and save to disk
        """
        ofhand = open(ofile, 'wb')
        size = 0
        while True:
            info = img.read(100000)
            if len(info) < 1:
                break
            size = size + len(info)
            ofhand.write(info)

        ofhand.close()
        return size

    def init_socket_and_url(self, url_prefix, url_base, url_page):
        url = self.buildurl(url_prefix, url_base, url_page)
        mysock = self.open_socket(url_base, 80)  # normal socket
        return mysock, url

    def open_socket(self, host, port):
        """
        open a socket for host on port
        """
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            mysock.connect((host, port))
        except:
            print("Could not connect to ", port, " on host '" + host + "'")
            mysock = None

        return mysock

    def close_socket(self, mysock):
        """
        close a socket
        """
        try:
            mysock.close()
        except:
            print("Bad Socket")
            mysock = None
        return mysock

    def get_page(self, mysock, url):
        """
        get  a text document from a socket
        """
        page = list()

        cmd = self.encode_get(url)
        try:
            mysock.sendall(cmd)
        except:
            print('SEND failed for ', url)
            return page

        First_time = True
        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break

            page_data = data.decode()

            if First_time:
                First_time = False
                page_data_list = page_data.split()
                if page_data_list[1] != "200":
                    print("Opening socket failed with code:",
                          page_data_list[1])
                    break

            page.append(page_data)
            print(page_data, end='')

        return page

    def print_page_limit(self, url_prefix, url_base, url_page, limit, skipheaders=False):
        mysock, url = self.init_socket_and_url(url_prefix, url_base, url_page)
        total_chars = 0

        if mysock is None:
            return total_chars

        print("\n")
        total_chars = self.print_page_socket(mysock, url, limit, skipheaders)
        print("\n")
        print("Total characters found:", total_chars)
        return total_chars

    def print_page_socket(self, mysock, url, limit, skipheaders=False):
        """
        Print a document from a URL and socket and limit the 
        number of characters printed.
        """
        count = 0
        # skipheaders_local = skipheaders

        cmd = self.encode_get(url)
        try:
            mysock.sendall(cmd)
        except:
            print('SEND failed for ', url)
            return None

        first_time_flag = True
        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break

            page_data = data.decode()

            if first_time_flag:
                first_time_flag = False
                page_data_list = page_data.split()
                if page_data_list[1] != "200":
                    print("Opening socket failed with code:",
                          page_data_list[1])
                    break

            if skipheaders:
                idx = page_data.find("\r\n\r\n")
                page_data = page_data[idx + 4:]
                skipheaders = False

            count = self.print_page_data(page_data, count, limit)

        return count

    def print_page_urllib(self, url, limit):
        """
        Print a document from a URL file handle using urllib and limit the number of characters printed.
        """
        count = 0

        fh = self.open_url(url, None)

        page_data = self.get_url_page(fh)

        for line in page_data:
            count = self.print_page_data(line, count, limit)

        return count

    def print_page_data(self, page_data, count, limit):
        for char in page_data:
            count = count + 1
            if count < limit:
                print(char, end="")
            elif count == limit:
                print(char, end="")
                print("\n---- Done printing " + str(count) + " characters ----")
        return count

    def encode_get(self, url):
        cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
        cmd = cmd.encode()
        return cmd

    def get_jpeg(self, mysock, url):
        """
        get a jpeg document from a socket
        """
        count = 0
        picture = b""

        cmd = self.encode_get(url)
        try:
            mysock.send(cmd)
        except:
            print('SEND failed for ', url)
            return picture

        while True:
            data = mysock.recv(5120)
            if len(data) < 1:
                break

            time.sleep(0.25)  # wait to give recv a chance to get all bytes

            count = count + len(data)
            print(len(data), count)
            picture = picture + data

        return picture

    def stripheaders_img(self, img, file):
        """
        Strip headers from img and save to file
        """
        # Look for the end of the header (2 CRLF)
        pos = img.find(b"\r\n\r\n")
        print('Header length', pos)
        print(img[:pos].decode())

        # Skip past the header and save the img data
        img = img[pos+4:]
        return img

    def save_picture(self, picture, file):
        """
        Strip headers from picture and save to file
        """
        # Look for the end of the header (2 CRLF)
        pos = picture.find(b"\r\n\r\n")
        print('Header length', pos)
        print(picture[:pos].decode())

        # Skip past the header and save the picture data
        picture = picture[pos+4:]
        fhand = open(file, "wb")
        fhand.write(picture)
        fhand.close()
        return len(picture)

    class InternetTreeXML():
        def __init__(self, raw_tree):
            self.raw_tree = raw_tree

        def create_tree(self):
            self.tree = ET.fromstring(self.raw_tree)

        def replace_tree(self, tree):
            self.tree = tree

        def findall_users(self):
            '''
            Create list of users from the current tree
            '''
            return self.tree.findall('users/user')

        def print_element_tree(self, field_list):
            '''
            Search through xml tree for fields and/or attributes of xml 
            '''
            len_fields = len(field_list)
            print('Number of tuples found: ', len_fields)

            for tpl in field_list:
                if len(tpl) != 4:
                    print("Number of fields incorrect and will be ignored: ", len(tpl))
                    return len_fields

                title, field, field_type, attr_name = tpl

                if field_type == 'text' and self.tree.findtext(field) is not None:
                    print(title, self.tree.find(field).text)
                elif field_type == 'attr':
                    if len(attr_name) > 0:
                        if self.tree.findtext(field) is not None:
                            if self.tree.find(field).get(attr_name) is not None:
                                print(title, self.tree.find(field).get(attr_name))
                            else:
                                print("Attribute not found: '" + attr_name + "'")
                        elif self.tree.get(attr_name) is not None:
                            print(title, self.tree.get(attr_name))
                        else:
                            print("Attribute not found: '" + attr_name + "'")
                    else:
                        print("Attribute name is missing")
                else:
                    print("Field not found: ", field)

            return len_fields

    class InternetTreeJSON(InternetTreeXML):
        def create_tree_list(self):
            self.tree_list = json.loads(self.raw_tree)
            if len(self.tree_list) > 1:
                self.tree = self.tree_list[0]

        def tree_list_count(self):
            return len(self.tree_list)

        def get_tree_list(self):
            return self.tree_list

        def findtext(self, field):
            if field in self.tree:
                return self.tree[field]

            for tree in self.tree_list:
                if field in tree:
                    self.replace_tree(tree)
                    return tree[field]
            return None

        def print_element_tree(self, field_list):
            '''
            Search through xml tree for fields and/or attributes of xml 
            '''
            len_fields = len(field_list)
            print('Number of tuples found: ', len_fields)

            for tpl in field_list:
                if len(tpl) != 4:
                    print("Number of fields incorrect and will be ignored: ", len(tpl))
                    return len_fields
                title, field, field_type, attr_name = tpl

                text_value = self.findtext(field)
                if field_type == 'text' and self.findtext(field) is not None:
                    print(title, self.findtext(field))
                elif field_type == 'attr':
                    if len(attr_name) > 0:
                        if self.findtext(field) is not None:
                            if self.findtext(attr_name):
                                print(title, self.findtext(attr_name))
                            else:
                                print("Attribute not found: '" + attr_name + "'")
                        elif self.findtext(attr_name):
                            print(title, self.findtext(attr_name))
                        else:
                            print("Attribute not found: '" + attr_name + "'")
                    else:
                        print("Attribute name is missing")
                else:
                    print("Field not found: ", field)

            return len_fields
