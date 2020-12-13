if True:
    print("this is true")

if False:
    print("This is false")

if not False:
    print("this is not false")

if 10 == 10:
    print("ten is ten")

if not 10 > 12:
    print("ten is not grater than twelve")

if 10 < 12:
    print("12 is grater than 10")

if 100 >= 100:
    print("100 is grater than or equal to 100")

if 100 > 100 or 100:
    print("100 is grater than or equal to 100")


if str(True).lower() == 'true':
    print("this is true")

if str('true').title() == 'True':
    print("this is true in upparcase")

if bool(str('true').title() == 'True'):
    print("this is true in upparcase and  bool")



abc = [1,2,3,4,5]
abc_sq = []
for num in abc:
    new_num = num ** 2
    abc_sq.append(new_num)

print("Suqre all element in list: ",abc_sq)

is_odd = []
is_even = []
for num in abc_sq:
    if num % 2 == 0:
        print("this is even")
        is_even.append(num)
    else:
        is_odd.append(num)

print("THis is even: ", is_even)
print("This is odd: ", is_odd)


is_factor_of_3 = []
for num in abc_sq:
    if num % 3 ==0:
        is_factor_of_3.append(num)
    elif num % 2 == 0:
        is_even.append(num)
    else:
        is_odd.append(num)
print("Factor three: ",is_factor_of_3)


x = 10
i = 0
z = 12

while i < x:
    print("While loop: ",i)
    i = i+1

y = 0
while y < x:
    z = z * 2
    if z > 342900:
        break
    print("z and y ")
    print(z, y)
    y = y+ .000000001

t = 0
while t<x:
    if i % 2 == 2:
        print("even") # this condition is false
    else:
        continue
    t += 1