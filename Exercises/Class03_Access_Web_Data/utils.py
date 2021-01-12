import re
import socket


class ExerciseUtils():
    """
    Test methods common to PY4E exercises
    """

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
        get data from a socket
        """
        page = list()

        cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
        cmd = cmd.encode()
        try:
            mysock.send(cmd)
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


print("re01 - Search for lines that contain 'From'")
exu = ExerciseUtils()
count = exu.run_search1('mbox-short.txt', 'From:', False)
assert count == 27

print("re02 - Search for lines that start with 'From'")
exu = ExerciseUtils()
count = exu.run_search1('mbox-short.txt', '^From:', False)
assert count == 27

print("re03 - Search for lines that start with 'F', followed by 2 characters, followed by 'm:'")
exu = ExerciseUtils()
count = exu.run_search1('mbox-short.txt', '^F..m:', False)
assert count == 27

print("re04 - Search for lines that start with From and have an '@' sign")
exu = ExerciseUtils()
count = exu.run_search1('mbox-short.txt', '^From:.+@', False)
assert count == 27

print("re05 - Search for an address")
exu = ExerciseUtils()
count = exu.run_findall('mbox-short5.txt', '\\S+@\\S+', False)
assert count == 5

print("re06 - Search for lines that have an at sign between characters")
exu = ExerciseUtils()
count = exu.run_findall('mbox-short.txt', '\\S+@\\S+', False)
assert count == 336

print("re07 - Search for lines that have an at sign between characters")
exu = ExerciseUtils()
count = exu.run_findall('mbox.txt', '[a-zA-Z0-9][a-zA-Z0-9.]*@[a-zA-Z][a-zA-Z.]*', False)
assert count == 22009

print("re10 - Search for lines that start with 'X' followed by any non whitespace characters and ':' followed by a space and any number. The number can include a decimal.")
exu = ExerciseUtils()
count = exu.run_search1('mbox-short.txt', 'X\\S*: [0-9.]+', False)
assert count == 54

print("re11 - Search for lines that start with 'X' followed by any non whitespace characters and ':' followed by a space and any number. The number can include a decimal.")
exu = ExerciseUtils()
count = exu.run_findall('mbox-short.txt', 'X\\S*: ([0-9.]+)', False)
assert count == 54

print("re13 - Search for lines that start with From and a character followed by a two digit number between 00 and 99 followed by ':'. Then print the number if it is greater than zero.")
exu = ExerciseUtils()
count = exu.run_findall('mbox-short.txt', '^From .* ([0-9][0-9]):', False)
assert count == 27

print("socket1 - World's simplest web browswer")
exu = ExerciseUtils()
url_prefix = "http://"
url_base = "data.pr4e.org"
url_page = "romeo.txt"
url = url_prefix + url_base + "/" + url_page
mysock = exu.open_socket("data.pr4e.org", 80) # normal socket
assert not mysock._closed

page = exu.get_page(mysock, url)
assert len(page) == 2

mysock = exu.close_socket(mysock) # normal socket
assert mysock._closed
