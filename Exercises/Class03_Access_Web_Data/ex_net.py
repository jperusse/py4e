from utils import ExerciseUtils

print("socket1 - World's simplest web browser")
exu = ExerciseUtils()
mysock, url = exu.init_socket("romeo.txt")

page = exu.get_page(mysock, url)
assert len(page) == 2

mysock = exu.close_socket(mysock)  # normal socket
assert mysock._closed

print("urljpeg - get a jpeg document")
exu = ExerciseUtils()
mysock, url = exu.init_socket("cover3.jpg")

pic = exu.get_jpeg(mysock, url)
assert len(pic) == 230608

mysock = exu.close_socket(mysock)  # normal socket
assert mysock._closed

piclen = exu.save_picture(pic, "stuff.jpg")
assert piclen > 0

print("urllib1 - use urllib to treat a web page like a file")
exu = ExerciseUtils()
fh = exu.open_url("romeo.txt")
assert fh != ""

page = exu.get_url_page(fh)
assert len(page) > 0

print(page)

print("urlwords - compute the frequency of each word in the file")
exu = ExerciseUtils()
fh = exu.open_url("romeo.txt")
page = exu.get_url_page(fh)
count = exu.getwords(page)
assert len(count) == 26
print(count)

print("curl1 - get and image and write it to a file")
exu = ExerciseUtils()
file = "cover3.jpg"
img = exu.open_url_small_img(file)
imglen = len(img)
assert imglen == 230210
print("Length of " + file + " is:", imglen)

rc = exu.write_file("cover3.jpg", "wb", img)
assert rc == None

print("curl2 - get and image and write it to a file using a buffer to read any size file")
exu = ExerciseUtils()
file = "cover3.jpg"
img = exu.open_url(file)
assert img != ""

count = exu.get_url_large_img_and_save(img, file)
assert count == 230210
print(count, 'characters copied.')

print("urlregex - Search for link values within URL input")
exu = ExerciseUtils()

