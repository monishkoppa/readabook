# readabook.in
:books: Encourage people to read paperbacks, old style.

* Run `get_books_list.py`
* Run `authors.py`
* Run `books.py`


### Code layout
There are three large parts of the code:

**Indexing code.** Uses Goodreads API to get a list of books in a user's shelves in xml format. `scrape.py` then scrapes the details of the books listed in `books.xml` -- title, author, isbn, page count etc.

**User interface.** The web server uses `Flask` to serve the app. Users can Register, Log in and Request to borrow books available in the catalog.

**Admin interface.** A set of pre-approved admins can issue books, add books to the catalog, and edit stuff on the site.

### Dependencies
Requires `python >= 3.6`. I recommend installing [Anaconda](https://www.anaconda.com/) for easy installing of packages and managing virtual envs.

In short, many dependencies. :cry: You will need `cs50` for easy execution of SQL commands, `Flask` for viewing the application, `requests` for making `https` requests and scraping content off the web. In addition, you'll also require `Flask-Session` for allowing log in and log out. Most, of these are easy to get through `pip`. e.g.:
```
$ conda create -n readabook python=3.7      # create a virtual env, so that dependencies don't clash
$ conda activate readabook                  # activate virtual env
$ pip install -r requirements.txt           # this will install most of the dependencies
```
### Email Notification system (Using Gmail)
To use this feature please follow the instructions below:
* run `export MAIL_USERNAME="your-full-gmail-address"`
* run `export MAIL_PASSWORD="your-gmail-password"`
* run `export MAIL_RECIPIENT="full-email-address-to-receive-test-email"`

**Note.** Be sure to allow access to less secure apps. Follow the instructions [here](https://support.google.com/accounts/answer/6010255?hl=en%3E). You should also turn off two factor authentication for Gmail, if you have that turned on.

### Running locally
To run the app locally on your machine, assuming you have all the dependencies installed, you can:
```
$ export FLASK_APP=application.py
$ flask run
# you'll get something like this. Follow the output URL to launch the web server
* Serving Flask app "application.py"
* Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
* Debug mode: off
INFO:werkzeug: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```


