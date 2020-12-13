def my_print(txt):
    print(txt)

my_print("Hello World")



template = """Hello there,
    {name} this is an amazing way to do
    subbming my cool team {club}. 
"""


def format_msg(name= "Pablo Sarabia", club= "PSG"):
    msg = template.format(name= name, club=club)
    # print("msg from function: \n",msg)
    return msg

format_msg()
print("-----------------------------------")
returning_func = format_msg()
print("printing function: \n", returning_func)

print("-----------------------------------")


names = 'a', 'b', 'c'
for n in names:
    this_person_club = format_msg(name = n)
    print("This person message: \n", this_person_club)


def baseFunction(*args, **kwargs):
    print("Args and kwargs: ",args, kwargs)

baseFunction()


