import re
import socket
import ssl
import time
import urllib.request

import requests  # requests is more advanced than urllib and does automatic decoding
from bs4 import BeautifulSoup


class ExerciseUtils():
    """
    Test methods common to PY4E exercises
    """
    url_prefix = "http://"
    url_base = "data.pr4e.org"
    url_default1 = "https://docs.python.org"
    url_default2 = "http://www.dr-chuck.com/page1.htm"
    url_text_doc = "romeo.txt"

    mbox_trace = "mbox_trace.txt"

    #
    # Base utility methods
    #
    def write_file(self, file, mode, list):
        fhand = self.openfile(file, mode)
        fhand.write(list)
        rc = fhand.close()
        return rc

    def openfile(self, fname, mode):
        """
        open a file and do error handling
        """
        try:
            fh = open(fname, mode)
        except:
            # Couldn't open the file
            fh = ""
        return fh

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
        hand = self.openfile(fname, 'r')
        if search_str == "" or hand == "":
            return count

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
        hand = self.openfile(fname, 'r')
        if search_str == "" or hand == "":
            return count

        if debug:
            wh = self.openfile(self.mbox_trace, "w")

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
        hand = self.openfile(fname, 'r')
        if search_str == "" or hand == "":
            return [0, 0]

        if debug:
            wh = self.openfile(self.mbox_trace, "w")

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
        if url == None:
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

    def bs4_tags(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        # Retrieve all of the anchor tags
        tags = soup('a')
        for tag in tags:
            print(tag.get('href', None))
        return tags

    def bs4_tags2(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        # Retrieve all of the anchor tags
        tags = soup('a')
        for tag in tags:
            # Look at the parts of a tag
            print('TAG:', tag)
            print('URL:', tag.get('href', None))
            print('Contents:', tag.contents[0])
            print('Attrs:', tag.attrs)
        return tags

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

        if ctx == None:
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
        url = url_prefix + url_base + "/" + url_page
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
            print("Bad Socket Received mysock='" + mysock + "'")
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
