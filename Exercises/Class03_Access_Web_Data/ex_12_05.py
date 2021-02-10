import re

from utils import ExerciseUtils

def_url = "http://data.pr4e.org/romeo.txt"

print("socket1 - World's simplest web browser for any url")
print("  Format of url must be http(s)://urlbase/page")
print("  Example: " + def_url)

url = input("Enter url to open(" + def_url + "): ")
if url == "":
    url = def_url


exu = ExerciseUtils()
url_prefix, url_base, url_page = exu.split_url(url)
if url_base == "" or url_base == None:
    print("Bad URL")
else:
    print("opening socket to:", url)
    mysock, url = exu.init_socket_and_url(url_prefix, url_base, url_page)
    if mysock != None:

        page = exu.get_page(mysock, url)

        mysock = exu.close_socket(mysock)  # normal socket
        assert mysock._closed
