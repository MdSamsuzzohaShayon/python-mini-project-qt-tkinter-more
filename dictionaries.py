# indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys.
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# It is best to think of a dictionary as a set of key: value pairs

players = {
    'Griezman': 123,
    "harry Kane": 140,
    "Mbappe": 150
}

print("Getting whole dictionary with keys and values: ",players)
# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
print("Only keys: ", players.keys())
print("Only values: ", players.values())

players["Haaland"]= 145

print("Adding item to it: ",players)

print("Get value for specific key(Mbappe): ", players['Mbappe'])
print("Getting key as list: ",list(players))



for k,v in players.items():
    print("Print key and value: ", k,v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)




questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
