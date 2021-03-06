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
total_chars = exu.print_page_limit(url_prefix, url_base, url_page, 3000, skipheaders=True)  # normal socket
