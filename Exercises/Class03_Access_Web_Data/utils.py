import re
import socket
import time
import urllib.request


class ExerciseUtils():
    """
    Test methods common to PY4E exercises
    """

    def open_url(self, url_page):
        url_prefix = "http://"
        url_base = "data.pr4e.org"
        url = url_prefix + url_base + "/" + url_page
        fh = urllib.request.urlopen(url)
        assert not fh == ""
        return fh

    def init_socket(self, url_page):
        url_prefix = "http://"
        url_base = "data.pr4e.org"
        url = url_prefix + url_base + "/" + url_page
        mysock = self.open_socket("data.pr4e.org", 80)  # normal socket
        assert not mysock._closed
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

        cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
        cmd = cmd.encode()
        try:
            mysock.sendall(cmd)
        except:
            print('SEND failed for ', url)
            return page
        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break

            page_data = data.decode()
            page.append(page_data)
            print(page_data, end='')

        return page

    def get_jpeg(self, mysock, url):
        """
        get a jpeg document from a socket
        """
        count = 0
        picture = b""

        cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
        cmd = cmd.encode()
        try:
            mysock.send(cmd)
        except:
            print('SEND failed for ', url)
            return picture

        while True:
            data = mysock.recv(5120)
            if len(data) < 1:
                break

            time.sleep(0.25) # wait to give recv a chance to get all bytes

            count = count + len(data)
            print(len(data), count)
            picture = picture + data

        return picture

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
            wh = self.openfile("mbox_trace.txt", "w")

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
            wh = self.openfile("mbox_trace.txt", "w")

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
        