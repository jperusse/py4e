import re

from utils import ExerciseUtils

def_url = "http://data.pr4e.org/romeo.txt"

print("socket1 - World's simplest web browser for any url")
print("  Format of url must be http(s)://urlbase/page")
print("  Example: " + def_url)

url = input("Enter url to open(" + def_url + "): ")
if url == "":
    url = def_url
url_list = re.findall("(.+//)(.*)/(.+)", url)
url_prefix, url_base, url_page = url_list[0] # first element is a tuple

exu = ExerciseUtils()
print("opening socket to:", url)
mysock, url = exu.init_socket_and_url(exu.url_prefix, exu.url_base, exu.url_text_doc)
assert mysock != None

page = exu.get_page(mysock, url)
assert len(page) == 2

mysock = exu.close_socket(mysock)  # normal socket
assert mysock._closed
