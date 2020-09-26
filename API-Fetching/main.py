# Tutorial     -      https://www.youtube.com/watch?v=tb8gHvYlCFs
# https://requests.readthedocs.io/en/master/

# pip install requests
# https://xkcd.com/

import requests

# GET REQUEST
# https://requests.readthedocs.io/en/master/user/quickstart/#make-a-request
# r = requests.get('https://xkcd.com/');
# print(dir(r))
# print(help(r))



# get source of a website
# text
# Content of the response, in unicode.
# print(r.text)




# get image
#  content
# Content of the response, in bytes.
# get_image = requests.get('https://imgs.xkcd.com/comics/parity_conservation.png')
# print(get_image.content)
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# with open("comic.png", "wb") as f:
#     f.write(get_image.content)


# GETTING STATUS CODE
# print(get_image.status_code)


# Return true if status code is lass than 400
# print(get_image.ok)



# GETTING HEADERS
# https://requests.readthedocs.io/en/master/user/quickstart/#response-headers
# print(get_image.headers)



# https://httpbin.org/
# WE CAN USE THIS SITE TO TEST DIFFERENT KINDS OF HTTP REQUEST FOR AUTH, CODES, DYNAMIC DATA, COOKIE ETC
# testing_request = requests.get('https://httpbin.org/get?page=2&count=25')

# payload = {'page': 2, 'count':25}
# testing_request = requests.get('https://httpbin.org/get', params=payload)
# print(testing_request.text)
# print(testing_request.url)















# # POST REQUEST
# payload = {'username': "shayon", 'password':'1234'}
# testing_post_request = requests.post('https://httpbin.org/post', data=payload)
# # print(testing_post_request.text)
#
#
#
# # GET JSON RESPONSE
# r_dict = testing_post_request.json()
# print(r_dict['form'])










# AUTH ROUTE
# https://httpbin.org/#/Auth
# PASTE URL IN BROWSER IT WILL ASK FOR AUTHENTICATION
# https://httpbin.org/shayon/1234
# auth_url = "https://httpbin.org/basic-auth/shayon/1234"
# auth_res = requests.get(auth_url, auth=('shayon','1234'))
# print(auth_res.text)
# print(auth_res)














# PREVENT RESPONSE CRUSHING
# https://httpbin.org/#/Dynamic_data/get_delay__delay_
# PASTE URL IN BROWSER IT WILL ASK FOR AUTHENTICATION
# https://httpbin.org/delay/3
delay_res = requests.get('https://httpbin.org/delay/2', timeout=3)
print(delay_res.text)
print(delay_res)