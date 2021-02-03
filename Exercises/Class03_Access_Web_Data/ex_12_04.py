from bs4 import BeautifulSoup

from utils import ExerciseUtils


print("urlpara - Search for paragrapsh (tags beginning with <p>) within URL page using BeatifulSoup to parse html")
exu = ExerciseUtils()
urls = [exu.url_default1, exu.url_default2, exu.url_default3, exu.url_default4]
for idx in range(4):
    for url in urls:
        html = exu.get_html(url)
        tags = exu.bs4_tags(html, "p", [False, False, False, False, ])
        print("Reading: ", url)
        print("Number of paragraphs: ", len(tags))
