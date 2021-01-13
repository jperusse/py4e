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