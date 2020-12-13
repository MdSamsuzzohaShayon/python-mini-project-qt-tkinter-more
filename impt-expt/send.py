# IMPORTING INTERNAL FUNCTION
from formatting import format_msg
from fetchAPI import json_api

# BUILT IN MODULE IMPORT
# https://docs.python.org/3/py-modindex.html
from datetime import datetime
import requests
import sys


# https://docs.python.org/3/library/functions.html


def send(name, club=None):
    if club != None:
        msg = format_msg(name=name, club=club)

    else:
        msg = format_msg(name=name)
    return msg

print(send("Lewandoski", "Bayern"))

message_to_lewa = send("Lewandoski", "Bayern")
print("Using variable \n", message_to_lewa)

print("--------------")




def send_api_get():
    json_api_get = json_api("http://httpbin.org/json")
    print("Fetching API using get request", json_api_get)



# CALLING A FUNCTION  BY DEFAULT
if __name__ == "__main__":
    print("All info: ",sys.argv)
    name = "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    send_api_get()








