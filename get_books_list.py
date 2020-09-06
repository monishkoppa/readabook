# get books list in xml given goodreads id
import requests

def setup(goodreads_id):
    """get books list from shelves given Goodreads ID

    input: goodread user id
    output: xml file named 'books.xml'
    """

    total_books = int(input("How many books do you have in total? "))
    pages = total_books // 200 + 1

    print("Wait a minute...")

    for page in range(pages):
        url = f"https://www.goodreads.com/review/list/{goodreads_id}.xml?key=UIFk5Ow3yHib11pGUsb0Q&v=2&page={page+1}&per_page=200"

        r = requests.get(url)

        with open(f'books_list_{page+1}.xml', 'w') as f:
            f.write(r.text)

if __name__ == "__main__":
    goodreads_id = input("Goodreads ID: ")
    setup(goodreads_id)
    print("[INFO] books into saved successfully...")