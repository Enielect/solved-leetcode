import math
import random

print(list(range(10,1,-1))) #by default the range starts from 0

eniola = 'I think i am quite proficient in python'
print(eniola.center(50)) #center the string based on the width i pass.
print(eniola.ljust(50))
print(eniola.rjust(100))#now this should make the concept of center, ljust, and rjust pretty clear.
print(len(eniola))
print(eniola.count('i'))
print(eniola.split('quite'))

#while a list is mutable a Tuple isn't.
tuple = (1,True,4.96)


print(tuple*3)

my_set = {False, True,6,3,1.3,'cay'}
print(False in my_set)
print("cat" in my_set)#we can also use len() to determine the length of the set.
print(my_set)

##adding and removing items frmo a set
first = {1,2,3}
second = {3,4,5,6}
print(first | second)
print(first&second)
print(first.difference(second))

#dictionaries
cities = {'Lagos': 'Ikeja', 'Ondo': 'Akure', 'Oyo': 'Ibadan'}
print(cities)
print(cities['Lagos'])
#you can mutate the dictionary in the normal way.
for k in cities:
    print(cities[k],'is the capital of ',k)
    
print(list(cities.keys()))
print('Ikeja' in cities) #The in operator checks for keys that are in the dictionary
print(cities.values())
print(cities.items())
print(list(cities.items()))
del cities['Oyo']
print(cities)

#input and output
##note that the print() stores the user inputed value as as string, and you would have to convert them to the type you want to work with for further processing
#print ends with a newline by default
print('Eniola', 'codes',sep='****',end='##')
print('Eniola', 'codes',sep='****')

#write a program to convert a list of words into a concatenated list.
word_ilst = ['cat', 'dog', 'rabbit']

together = [ ]
for word in word_ilst:
    for letter in word:
        together.append(letter)
print(together)

sq_list = [x * x for x in range(1,11)]
sq_list_2 = [x * x for x in range(1,11) if x % 2 == 0]
print(sq_list)
print(sq_list_2)

#print uppercase that are not vowels
upper = [ch.upper() for ch in 'comprehension' if ch not in 'aeiou']
print(upper)

#handling exceptions
a_number = input('Input a number to derive the sq root ')
try:
    print(math.sqrt((int(a_number))))
except:
    print("Bad value", "Use absolute value instead")
    print(math.sqrt(abs(int(a_number))))
    
# creating(raising) a new RuntimeError exception.
if int(a_number) < 0:
    raise RuntimeError("Cannot get the square root of a negative value")
else:
    print(math.sqrt(int(a_number)), 'is the square root of the number you inputed')
    
#defining functions.
def square (x):
    return x * x
print(square(3), "This is the square")

def sq_root(n):
    root = n / 2
    for k in range(20):
        root = (1 / 2) * (root + (n / root))
    return root;

print(sq_root(4), "this is supposed to be the square root of 4")

#first self-check challenge

