# A tuple consists of a number of values separated by commas
# https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

t = 123, 456, 'hello'
print("This is tuples: ",t)
print("First Tuples: ", t[0])

# TUPLES CAN BE NESTED
nestedTuples = 1,2,3, (4, 5, 6, ("One", "two", "three"))
print("Nested tuples: ", nestedTuples)

multiObj = ([1, 2, 3], [3, 2, 1])
print("Multiple object: ", multiObj)


# Tuples may be nested:
# Tuples are immutable:
# but they can contain mutable objects: