from utils import ExerciseUtils

print("socket1 - World's simplest web browser")
exu = ExerciseUtils()
mysock, url = exu.init_socket(exu.url_text_doc)

page = exu.get_page(mysock, url)
assert len(page) == 2

mysock = exu.close_socket(mysock)  # normal socket
assert mysock._closed
