# print to console
print(1)


# create variables
my_var = 223
# or
a, b, c = 1, 2, 3


# format strings with f strings
string = f"hi {my_var}"
print(string)


# data types

# numeric
# float
22.654
# int
22
# complex
1j

# text
# string
"hello world" or "hello world"
# raw string
r"hi:\\bye"
# multiline spannable strings
"""hi
bye
good bye"""

# boolean
# bool
True
False

# sequence
# list
[1, 2, 3]
# tuple
(1,)
# range
range(3)

# mapping
# dict
{"name": "parth", "age": 20, "a": a}

# set
# set
{1, 2, 3}
# frozenset
frozenset({1, 2, 3})

# binary
# bytes
b"parth"
# bytearray
bytearray(7)
# memoryview
memoryview(bytes(7))


# naming convention

# normal variables
snake_case = "gg"
# constants
CAPITAL_SNAKE_CASE = 3.14
# private
__no_touchy__ = "private data"
# class


class UpperCamelCase:
    pass


# functions
def fun(x):
    print(x)


fun(1)


# strings

# accessing by position
a = "Hello, World!"
print(a[1])
# slicing
b = "Hello, World!"
print(b[2:5])
# length
print(len(b))
# methods
# It strips the spaces
a = " Hello, World! "
print(a.strip())

# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

# The split() method splits the string into substrings
# if it finds instances of the separator:
a = "Hello, World!"
print(a.split(","))

# check string
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)


# lists
thislist = ["apple", "banana", "cherry"]
print(thislist)
# negative index
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
# range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# range of negative indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
# change values
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
# looping
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
# use in keyword to check if item exists
# len for getting length of list
# append
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# remove
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
# copy
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
# join
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
# or you can use extend or append


# tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
# access
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
# you can not change ,remove or add tuple values because it is immutable
# use following syntax to create tuple with one item
thistuple = ("apple",)
print(type(thistuple))
# or
thistuple = ("apple",)
print(type(thistuple))


# set
thisset = {"apple", "banana", "cherry"}
print(thisset)
# loop
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)
# check
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
# add
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)
# remove
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

thisset = {"apple", "banana", "cherry"}

del thisset

# print(thisset) #error

# join
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# Theupdate()method inserts the items in set2 into set1:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
