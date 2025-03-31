print('hello world')

eni = input('What is your age? ')

print(eni + ' This is eniolas variable')

#converting string to int

another = int(eni);
print(another)
#convert to float float(another), bool(), str()- to string

course = 'Python for Beginners'

#finding a part of  a string. e.g 'python' in course(//true) 

#10//3 minimalistic floor functoin

#The and operator in python: print(price > 10 and price < 30). The or operator is siilar, just replace and with or.
#inversion operator: print(not price > 10)

temp = 20;

if temp > 10:
    print('Drink plety of water')
elif temp < 10:
    print("I am actually lesss than 10")
else:
    print("If any of the above conditions doesn't get validated")
print("I don't really care of the condition")

#using while looos

#making large number more readable: 1000 can be rewritten as 1_000
i = 1;
while i <= 5:
    print(i)
    i = i + 1
    
#multiplying a number by a sgring( this will repaet the string by that number)

#lists in python
names = ["John", "Micheal", "Daniel"];
print(names) #names[-1]: last element in the list. while -2 represents the second element from the end of the list.
#you can just mutate the elment of a list by using the indexing mutation method.
print(names[0:3]) #print the elements starting from the first element but excluding the element with index 3. This doesn't mutate the original list.

names.append(4) #addding an elmeent to the end of a list, 
names.insert(0, -3) #adding to the beginning of the list or somewhere in between .(replace the first element with -3)
names.remove(4) #remove the number 4 from the list
names.clear() #to clear all the elements from a list.
#we can also use the in operator for lists as well to check if a particular item exists as an element of a list.
print(3 in names) #we should expect a boolean returnl
len(names) #to determine the size of list

#for loops
for item in names:
    print(item) #simple use of for loop in python
    
#using the range built function to declare the range between 2 numbers.

numbers = range(0,10)

for number in numbers:
    print(number) #This should now print each number in the numbers range.(This doesn't include the last number(digit, element))
    
#not that if a third parameter is passed to the range function, it is taken as the step of the ranging(series);

#Tuples are immutable
rand_nums = (1,3,4) #how to define a tuple
#rand_nums[0] = 1 (this is impossible here as the tuples are immutable)
rand_nums.count(3) #returns the number of occurrence of the element 3.
rand_nums.index(3) #this returns the index of the first occurrence of the given element.