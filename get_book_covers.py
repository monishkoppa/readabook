# utility file to get book covers
# use Open Library Covers API

import json
import time
import random
import urllib.request
import os, os.path

with open("books_test.json", "r") as read_file:
    data = json.load(read_file)

titles = []
for book in data:
    try:
        cwd = os.getcwd()
        fullfilename = os.path.join(f"{cwd}/static/images/", f"{book['isbn']}.jpg")

        urllib.request.urlretrieve(f"http://covers.openlibrary.org/b/isbn/{book['isbn']}-L.jpg", fullfilename)
        time.sleep(random()*5)
    except:
        print("Cover not found for " + str(book['title']))

        titles.append(book['title'])

read_file.close()

os.system("find . -name '*.jpg' -type 'f' -size -1k -delete")

books = [{"title": t} for t in zip(titles)]

with open('books_without_covers.json', 'w') as file:
    json.dump(books, file)

file.close()

print('Done...')