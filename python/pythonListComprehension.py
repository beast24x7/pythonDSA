myList = []
mystring = 'mystring'

for i in mystring:
    myList.append(i)
print(myList)

list = [letter for letter in mystring]
print(list)


print([num**2 for num in range(0,10)])

print([num for num in range(0,10) if num % 2 == 0])

celsius = [10,20,30,40]
fahrenhiet = [(9/5)* temp + 32 for temp in celsius]
print(fahrenhiet)
print(celsius)


result = [x if x % 2 == 0 else f'ODD number {x}' for x in range(0,15)]
print(result)

##problems 
st = 'Print only the words that start with s in this sentence'
print([s for s in st.split() if s[0] == 's'])

## Use range() to print all the even numbers from 0 to 10.
print([n for n in range(0,11) if n % 2 == 0])

##Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.**
print([n for n in range(1,51) if n % 3 == 0])

##Go through the string below and if the length of a word is even print "even!"**
st = 'Print every word in this sentence that has an even number of letters'

print([string for string in st.split() if len(string) % 2 == 0])

