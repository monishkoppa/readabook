# get books data from goodreads and write to database

from lxml import etree
import requests
import shutil
import wget
import json
import csv
import random
import time
import html2text
import wikipedia

root = etree.parse('books.xml').getroot()
reviews = root.find('reviews')

review_ = reviews.findall('review')
# print(review_)

titles, authorName, cat, isbn, numPages, desc = [], [], [], [], [], []

i = 1
numBooks = len(review_)
for review in review_:
    book = review.find('book')
    isbn13 = book.find('isbn13')
    isbn13 = isbn13.text

    # This is the image url.
    # image_url = f"http://covers.openlibrary.org/b/isbn/{isbn13}-M.jpg"
    # Open the url image, set stream to True, this will return the stream content.
    # image_filename = wget.download(image_url)

    title = book.find('title')
    pages = book.find('num_pages')

    if book.find('description').text != None:
        description = (book.find('description')).text
        description = html2text.html2text(description)
    else:
        description = None
        # print(description)
    authors = book.find('authors')
    author = authors.find('author')
    author = (author.find('name')).text.strip()
    # print(title.text)
    title = title.text
    titles.append(title)
    # print(author)
    authorName.append(author)

    # try to get book category
    # book_url = "https://book-genre-classification.herokuapp.com/predict"
    # data = {"book": f"{title}"}
    #
    # response = requests.post(book_url, data)
    # genre = response.text.split('"')[3]
    # # print(genre)
    #
    # print('Sleeping for %i seconds' % (3.0, ))
    # time.sleep(3.0 + random.uniform(0, 3))
    #
    # cat.append(genre)
    isbn.append(isbn13)
    # print(pages.text)
    numPages.append(pages.text)
    # desc.append(description)
    # if i == 31:
    #     break
    #
    # print(f"Processed {i}/{numBooks} books")
    # i += 1

print(authorName)

author_bio = []
for author in authorName:
    try:
        bio = wikipedia.summary(author, sentences=3)
        author_bio.append(bio)
        # print(bio)
    except:
        bio = None
        author_bio.append(bio)
        continue
    if i == 30:
        break
    i += 1
    print('Sleeping for %i seconds' % (3.0, ))
    time.sleep(3.0 + random.uniform(0, 3))

authors = [{"name": n, "bio": b} for n, b in zip(authorName, author_bio)]
# print(json.dumps(authors))
with open('authors.json', 'w') as file:
    json.dump(authors, file)
# for grandchild in books:
#     isbn13, title = grandchild.find('isbn13'), grandchild.find('title')
#     print (isbn13.text), (title.text)

# books = [{"title": t, "author": a, "genre": c, "isbn": i, "numPages": pages, "description": d} for t, a, c, i, pages, d in zip(titles, authorName, cat, isbn, numPages, desc)]

# print(json.dumps(books))

# with open('books.json', 'w') as file:
#     json.dump(books, file)


# with open('book32-listing.csv', 'r', encoding='mac_roman') as file:
#     reader = csv.reader(file)
#     i = 0
#     for row in reader:
#         if len("Zero to One: Notes on Start Ups, or How to Build the Future") / len("Zero to One: Notes on Startups, or How to Build the Future") >= 0.5:
#         # if "Peter Thiel" == row[4]:
#             print(row[3])
#         # i += 1
#         # if i == 10:
#         #     break
