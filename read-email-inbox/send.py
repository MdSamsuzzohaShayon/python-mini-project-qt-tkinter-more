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
    print("Sent: ", sent)
    return sent


# THIS IS DEFAULT CALL FOR OUR MODULE
# THIS IS MORE APPROPRIATE IN PYTHON THAN CALLING OUTSIDE
# IF WE CALL ANY FUNCTION BY USING THIS IT WON'T CALL THE WHOLE FUNCTION
if __name__ == "__main__":
    print("Default call of a function ")
    send(name="Shayon", to_email="mdshayon0@gmail.com")

    """
    # PASSING THE ARGUMENTS THOUGH TERMINAL AND USE THE VALUE IN OUR PROJECT 
    print("All info: ", sys.argv)
    name = "Unknown"
    
    print("Length or argv: ",len(sys.argv))
    
    # THIS WILL GRAB THE FIRST VALUE FROM TERMINAL COMMAND
    # python3 send.py value_one
    # FROM THE COMMAND AVOBE VALUE_ONE IS ACCESSABLE USING SYS.ARGV[1] 
    if len(sys.argv) > 1:
        name = sys.argv[1]
        print("name: ", name)
    email = None
    
    # THIS WILL GRAB THE FIRST VALUE FROM TERMINAL COMMAND
    # python3 send.py value_one value_two
    if len(sys.argv) > 2:
        email = sys.argv[2]
        print("Email: ", email)
    response = send(name, to_email=email, verbose=True)
    # print("Response ",response)
    """
