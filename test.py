# import requests
# # book_url = "https://book-genre-classification.herokuapp.com/predict"
# # data = {"book": f"{title}"}
# #
# # response = requests.post(book_url, data)
# # print(response.text.split('"')[3])
#
# import html2text
#
# text = "Peter Guillam, staunch colleague and disciple of George Smiley of the British Secret Service, otherwise known as the Circus, has retired to his family farmstead on the south coast of Brittany when a letter from his old Service summons him to London. The reason? His Cold War past has come back to claim him. Intelligence operations that were once the toast of secret London are to be scrutinised by a generation with no memory of the Cold War. Somebody must be made to pay for innocent blood once spilt in the name of the greater good.<br /><br />Interweaving past with present so that each may tell its own story, John le Carré has given us a novel of superb and enduring quality."
#
# print(html2text.html2text(text))
import wikipedia

print(wikipedia.summary("Sophie Kinsella", sentences=3))

# print(text)
