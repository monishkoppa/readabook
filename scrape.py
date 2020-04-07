# get books data from goodreads and write to database

from lxml import etree
import requests
import shutil
import wget

root = etree.parse('books.xml').getroot()
reviews = root.find('reviews')

review_ = reviews.findall('review')
print(review_)

for review in review_:
    book = review.find('book')
    isbn13 = book.find('isbn13')
    isbn13 = isbn13.text

    # This is the image url.
    image_url = f"http://covers.openlibrary.org/b/isbn/{isbn13}-M.jpg"
    # Open the url image, set stream to True, this will return the stream content.
    image_filename = wget.download(image_url)

    title = book.find('title')
    pages = book.find('num_pages')
    if book.find('description') != None:
        description = (book.find('description')).text
        print(description)
    authors = book.find('authors')
    author = authors.find('author')
    author = (author.find('name')).text.strip()
    print(isbn13, title.text)
    print(author)
    print(pages.text)

# for grandchild in books:
#     isbn13, title = grandchild.find('isbn13'), grandchild.find('title')
#     print (isbn13.text), (title.text)
