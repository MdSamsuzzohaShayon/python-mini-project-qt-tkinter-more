# LIST IS AN ARRAY
# https://docs.python.org/3/tutorial/datastructures.html
# The list data type has some more methods.

fruits = ["orange", "apple", "banana", "pear"]
print(fruits)

print("Count of apple: ", fruits.count("apple"))
print("Count of apple: ", fruits.index("pear"))

fruits.reverse()
print("Reversing the list: ", fruits)

fruits.sort( key=None, reverse=False)
print("Sorting list: ",fruits)

newList = fruits.copy()
print("New List: ",newList)

newFruit = ['a', 'b', 'c']

fruits.append(newFruit)
print("Appending an list: ", fruits)


print(len(fruits))















print('\n\n-----------------------')
# Using Lists as Queues
# To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")
queue.popleft()



print(queue)




for i in queue:
    print("Looping: ",i)


print('\n\n-----------------------')
squares = []
for x in range(10):
    squares.append(x**2)
print("List created by loop: ",squares)
print('Adding integer: ',sum(squares))
