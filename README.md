# readabook.in
:books: Encourage people to read paperbacks, old style.

#### Features
* [x] Register
* [x] Log in
* [x] Log out
* User page:
    * Tabs: 
      * [ ] Your books (books borrowed by the user)
    * Homepage:
        * [x] Display all books, searchable
        * [ ] Request from this page
        * [ ] Click on book name, take to book page and then allow request to borrow book
* Book page:
    * Tabs: 
      * [ ] Your books
    * Homepage:
        * [ ] Display individual book details
            * [ ] title
            * [ ] author(s)
            * [ ] thumbnail image
            * [ ] pages
            * [ ] genre
            * [ ] description

* Admin page:
    * Tabs:
        * [ ] Books issued
        * [ ] Requested books
        * [ ] Books to acquire
        * [ ] Add books to catalog
    * Homepage:
        * [x] Display all books, searchable
        * [ ] Count of the available books
        
        
### Code layout
There are three large parts of the code:

**Indexing code.** Uses Goodreads API to get a list of books in a user's shelves in xml format. `scrape.py` then scrapes the details of the books listed in `books.xml` -- title, author, isbn, page count etc.

**User interface.** The web server uses `Flask` to serve the app. Users can Register, Log in and Request to borrow books available in the catalog.

**Admin interface.** 
