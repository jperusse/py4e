from utils import ExerciseUtils
from bs4 import BeautifulSoup


class AccessWebData():
    """
    Methods contructed for Class 3
    """

    url_text_doc = "romeo.txt"
    url_jpg = "cover3.jpg"
    local_jpg = "stuff.jpg"

    def socket1(self):
        print("socket1 - World's simplest web browser")
        exu = ExerciseUtils()
        mysock, url = exu.init_socket(self.url_text_doc)

        page = exu.get_page(mysock, url)
        assert len(page) == 2

        mysock = exu.close_socket(mysock)  # normal socket
        assert mysock._closed

    def urljpeg(self):
        print("urljpeg - get a jpeg document")
        exu = ExerciseUtils()
        mysock, url = exu.init_socket(self.url_jpg)

        pic = exu.get_jpeg(mysock, url)
        assert len(pic) == 230608

        mysock = exu.close_socket(mysock)  # normal socket
        assert mysock._closed

        piclen = exu.save_picture(pic, self.local_jpg)
        assert piclen > 0

    def urllib1(self):
        print("urllib1 - use urllib to read a web page like a file")
        exu = ExerciseUtils()
        fh = exu.open_url(self.url_text_doc, None)
        assert fh != ""

        page = exu.get_url_page(fh)
        assert len(page) > 0

        print(page)

    def urlwords(self):
        print("urlwords - compute the frequency of each word in the file")
        exu = ExerciseUtils()
        fh = exu.open_url(self.url_text_doc, None)
        page = exu.get_url_page(fh)
        count = exu.getwords(page)
        assert len(count) == 26
        print(count)

    def curl1(self):
        print("curl1 - get and image and write it to a file")
        exu = ExerciseUtils()
        img = exu.open_url_small_img(self.url_jpg, None)
        imglen = len(img)
        assert imglen == 230210
        print("Length of " + self.url_jpg + " is:", imglen)

        rc = exu.write_file(self.url_jpg, "wb", img)
        assert rc == None

    def curl2(self):
        print("curl2 - get and image and write it to a file using a buffer to read any size file")
        exu = ExerciseUtils()
        img = exu.open_url(self.url_jpg, None)
        assert img != ""

        count = exu.get_url_large_img_and_save(img, self.url_jpg)
        assert count == 230210
        print(count, 'characters copied.')

    def urlregex(self, UserInput=False):
        print("urlregex - Search for link values within URL input")
        exu = ExerciseUtils()
        html = exu.get_html(UserInput)
        exu.regexlinks(html)



    def urllinks(self, UserInput=False):
        print("urllinks - Search for link values within URL page using BeatifulSoup to parse html")
        exu = ExerciseUtils()
        html = exu.get_html(UserInput)
        exu.bs4_tags(html)



class3 = AccessWebData()

class3.socket1()
class3.urljpeg()
class3.urllib1()
class3.urlwords()
class3.curl1()
class3.curl2()
class3.urlregex()
class3.urllinks()
