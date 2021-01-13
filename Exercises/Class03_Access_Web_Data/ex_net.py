from utils import ExerciseUtils

# print("socket1 - World's simplest web browser")
# exu = ExerciseUtils()
# mysock, url = exu.init_socket("romeo.txt")

# page = exu.get_page(mysock, url)
# assert len(page) == 2

# mysock = exu.close_socket(mysock)  # normal socket
# assert mysock._closed

# print("urljpeg - get a jpeg document")
# exu = ExerciseUtils()
# mysock, url = exu.init_socket("cover3.jpg")

# pic = exu.get_jpeg(mysock, url)
# assert len(pic) == 230608

# mysock = exu.close_socket(mysock)  # normal socket
# assert mysock._closed

# piclen = exu.save_picture(pic, "stuff.jpg")
# assert piclen > 0

# print("urllib1 - use urllib to treat a web page like a file")
# exu = ExerciseUtils()
# fh = exu.open_url("romeo.txt")
# assert fh != ""

# page = exu.get_url_page(fh)
# assert len(page) > 0

# print(page)

print("urlwords - ")
exu = ExerciseUtils()
fh = exu.open_url("romeo.txt")
page = exu.get_url_page(fh)
count = exu.getwords(page)
assert len(count) == 26
print(count)

