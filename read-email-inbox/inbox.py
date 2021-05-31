import imaplib  # IMAP4 protocol client
# This module defines three classes, IMAP4, IMAP4_SSL and IMAP4_stream
import email
# WE NEED TO LOGIN TO GMAIL
from keys import login_info

host = "imap.gmail.com"
username = login_info['gmail']
password = login_info["password"]






def get_inbox():

    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)

    mail.select("inbox")
    _, search_data = mail.search(None, "UNSEEN")  # UNPACK THE VALUE OF TUPLE - JUST INVERT IT

    # print(search_data)
    # print(search_data[0])
    # print(search_data[0].split())  # IT WILL TURN ALL OF THEM AS LIST ITEM

    my_message = []

    # INTRATE THE LIST
    for num in search_data[0].split():
        email_data = {}
        # print(num)
        _, data = mail.fetch(num, "(RFC822)")  # GRAB THE CURRECT MESSAGE
        # print(data) # VERY LONG OUTPUT
        # print(data[0]) # SHOWING TUPLE

        # SEPERATE THE VALUE
        _, b = data[0]
        # print(_,b)
        # msg_str = str(b)  # CONVERTING BYTES INTO STRING
        # print('msg_str: ', msg_str)

        email_message = email.message_from_bytes(b)  # READABLE FORMAT
        # email_message = email.message_from_string(b)  # READABLE FORMAT

        # print(email_message)

        for header in ['subject', "to", 'from', 'date']:
            print("{}:  {}".format(header, email_message[header]))
            email_data[header] = email_message[header]

        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                # print(body.decode())
                email_data['body'] = body.decode()

            elif part.get_content_type() == "text/html":
                html_body = part.get_payload(decode=True)
                # print(html_body.decode())
                email_data['html_body'] = html_body.decode()

        my_message.append(email_data)
    return my_message



if __name__ == "__main__":
    my_inbox = get_inbox()
    print(my_inbox)


print("message")
