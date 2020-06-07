# utility file to get book covers
# use Open Library Covers API

import json
import time
import random
import urllib.request

with open("books.json", "r") as read_file:
    data = json.load(read_file)

for book in data:
    try:
        urllib.request.urlretrieve(f"http://covers.openlibrary.org/b/isbn/{book['isbn']}-L.jpg", f"{book['isbn']}.jpg")
        time.sleep(random()*5)
    except:
        print(book['title'])



read_file.close()