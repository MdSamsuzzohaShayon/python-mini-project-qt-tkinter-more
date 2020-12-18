import imaplib  # IMAP4 protocol client
# This module defines three classes, IMAP4, IMAP4_SSL and IMAP4_stream
import email
# WE NEED TO LOGIN TO GMAIL
from keys import login_info

host = "imap.gmail.com"
username = login_info['gmail']
password = login_info["password"]

mail = imaplib.IMAP4_SSL(host)
mail.login(username, password)

mail.select("inbox")
_, search_data = mail.search(None, "UNSEEN")  # UNPACK THE VALUE OF TUPLE - JUST INVERT IT

# print(search_data)
# print(search_data[0])
# print(search_data[0].split())  # IT WILL TURN ALL OF THEM AS LIST ITEM


# INTRATE THE LIST
for num in search_data[0].split():
    # print(num)
    _, data = mail.fetch(num, "(RFC822)")  # GRAB THE CURRECT MESSAGE
    # print(data) # VERY LONG OUTPUT
    # print(data[0]) # SHOWING TUPLE

    # SEPERATE THE VALUE
    _, b = data[0]
    # print(_,b)
    # msg_str = str(b)  # CONVERTING BYTES INTO STRING
    # print('msg_str: ', msg_str)

    email_message = email.message_from_bytes(b)
    print(email_message)

print("message")
