import sys
import requests
from datetime import datetime

from formatting import format_msg
from send_mail import send_mail


def send(name, website=None, to_email=None, verbose=False):
    assert to_email != None
    format_msg(my_name="Justin", my_website="cfe.sh")
    if website != None:
        print("I have website")
        msg = format_msg(my_name=name, my_website=website)
    else:
        msg = format_msg(my_name=name)
        print("web site is none")

    if verbose:
        print("Varbase is false: ", name, website, to_email)

    """
    print("=========================")
    print("MSG: ",msg)
    print("to_email: ", to_email)
    print("html: ")
    print("=========================")
    """

    # send the message
    sent = None
    try:
        # send_mail(text, subject, from_email, to_emails, html)
        send_mail(text=msg, to_emails=[to_email], html=None)
        sent = True
    except:
        sent = False
        pass
    print("Sent: ",sent)
    return sent


send(name="Shayon", to_email="mdshayon0@gmail.com")

print("All info: ", sys.argv)
"""
if __name__ == "__main__":
    # print("Sys.argv: ",sys.argv)
    name = "Unknown"
    print("Default call of a function ")
    print("Length or argv: ",len(sys.argv))
    if len(sys.argv) > 1:
        name = sys.argv[1]
        print("name: ", name)
    email = None
    if len(sys.argv) > 2:
        email = sys.argv[2]
        print("Email: ", email)
    response = send(name, to_email=email, verbose=True)
    # print("Response ",response)
"""
