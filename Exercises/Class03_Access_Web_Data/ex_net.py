from utils import ExerciseUtils
import xml.etree.ElementTree as ET


class AccessWebData():
    """
    Methods contructed for Class 3
    """

    url_jpg = "cover3.jpg"
    local_jpg = "stuff.jpg"

    def socket1(self):
        print("socket1 - World's simplest web browser")
        exu = ExerciseUtils()
        mysock, url = exu.init_socket_and_url(exu.url_prefix, exu.url_base,
                                              exu.url_text_doc)
        assert mysock is not None
        page = exu.get_page(mysock, url)
        assert len(page) == 2

        mysock = exu.close_socket(mysock)  # normal socket

    def urljpeg(self):
        print("urljpeg - get a jpeg document")
        exu = ExerciseUtils()
        mysock, url = exu.init_socket_and_url(exu.url_prefix, exu.url_base,
                                              self.url_jpg)
        assert mysock is not None
        pic = exu.get_jpeg(mysock, url)
        assert len(pic) == 230608

        mysock = exu.close_socket(mysock)  # normal socket

        piclen = exu.save_picture(pic, self.local_jpg)
        assert piclen > 0

    def urllib1(self):
        print("urllib1 - use urllib to read a web page like a file")
        exu = ExerciseUtils()
        fh = exu.open_url(exu.url_text_doc, None)
        assert fh != ""

        page = exu.get_url_page(fh)
        assert len(page) > 0

        print(page)

    def urlwords(self):
        print("urlwords - compute the frequency of each word in the file")
        exu = ExerciseUtils()
        fh = exu.open_url(exu.url_text_doc, None)
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
        assert rc is None

    def curl2(self):
        print("curl2 - get and image and write it to a file using a buffer to\
              read any size file")
        exu = ExerciseUtils()
        img = exu.open_url(self.url_jpg, None)
        assert img != ""

        count = exu.get_url_large_img_and_save(img, self.url_jpg)
        assert count == 230210
        print(count, 'characters copied.')

    def urlregex(self):
        print("urlregex - Search for link values within URL input")
        exu = ExerciseUtils()
        html = exu.get_html(exu.url_default1)
        exu.regexlinks(html)

    def urllinks(self):
        print("urllinks - Search for link values within URL page using\
              BeatifulSoup to parse html")
        exu = ExerciseUtils()
        html = exu.get_html(exu.url_default1)
        exu.bs4_tags(html, 'a', pflags=[False, True, False, False])

    def urllinks2(self):
        print("urllinks2 - Look at the parts of a tag")
        exu = ExerciseUtils()
        html = exu.get_html(exu.url_default2)
        exu.bs4_tags(html, 'a')

    def xml1(self):
        data = '''
        <person>
        <name>James</name>
        <phone type="intl">
            +1 503 851 8418
        </phone>
        <email hide="yes" />
        </person>'''

        exu = ExerciseUtils()
        exu.print_element_tree([("Name:", "name", "text", "")], data)
        exu.print_element_tree([("Attr:", "email", "attr", "hide")], data)

    def xml2(self):
        input = '''
        <stuff>
            <users>
                <user x="2">
                    <id>001</id>
                    <name>Chuck</name>
                </user>
                <user x="7">
                    <id>009</id>
                    <name>Brent</name>
                </user>
            </users>
        </stuff>'''

        exu = ExerciseUtils()
        tree = ET.fromstring(input)

        field_list = [("Name:", "user", "text", ""), ("Attr:", "email", "attr", "hide")]
        exu.print_element_tree(field_list, tree)


class3 = AccessWebData()

# class3.socket1()
# class3.urljpeg()
# class3.urllib1()
# class3.urlwords()
# class3.curl1()
# class3.curl2()
# class3.urlregex()
# class3.urllinks()
# class3.urllinks2()
# class3.xml1()
class3.xml2()
