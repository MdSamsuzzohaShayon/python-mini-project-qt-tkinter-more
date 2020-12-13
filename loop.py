# LOOPING
for i in 'abc':
    print('----')
    print("abc string looping: ",i)
    print("Printing from index value: " + "abc"[1])


# NESTED LOOP
print("Nested for loop")
for x in range(1,20):
    for y in range(1,20):
        print("%d * %d = %d" % (x, y, x*y))


# FOR ELSE LOOP AND STATEMENT
for x in range(3):
    print(x)
else:
    print("X is out of range 3 now x is ", x)

# Lists as an iterable
clubs = ['Barcelona', 'PSG', 'Bayern Munich']
for x in clubs:
    print("All clubs we have: "  + x)


# https://www.youtube.com/watch?v=iTa1ZnWdIS0&list=PLEsfXFp6DpzQjDBvhNy5YbaBx9j-ZsUe6&index=4
# TOUPLE CAN BE COMMA SEPARATED - NO DUPLICATES
clubByCountry = (
    ("Barcelona", "Real Madrid", "Atletico De Madrid"),
    ("Bayern Munich", "Leipzig", "Dortmund"),
    ("Liverpool", "Man Utd", "Man City")
)

for touple_of_touple in clubByCountry:
    for t in touple_of_touple:
        print("Print all from nested element: ",t)


# MAKING TWO TOUPLE FROM NESTED TOUPLE
# club by country list
crty_a = clubByCountry[0]
crty_b = clubByCountry[1]

clubList = [crty_a, crty_b ]
for f_club in clubList:
    print("FC from created touple: ",f_club)

for f_c in clubList:
    print("Getting single value from each loop: ",f_c[0])



# MAKING A DISTIONARIES
mbappe = {"name": "Mbappe", "totalGoal": 120, "marketValue": 150}
neymar = {"name": "Neymar", "totalGoal": 180, "marketValue": 130, "nationalSide": "Brazil"}

psg = [mbappe, neymar]


for p in psg:
    print("This is psg for you: ", psg)
    print("This is psg player for you: ", p['name'])
    if 'nationalSide' in p:
        print("national side: ", p['nationalSide'])



