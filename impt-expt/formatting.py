template = """Hello there,
    {name} this is an amazing way to do
    subbming my cool team {club}. 
"""


def format_msg(name= "Pablo Sarabia", club= "PSG"):
    msg = template.format(name= name, club=club)
    return msg