if True:
    print("true")
else:
    print("false")

list = [1,2,3,4,5,6,7,8,9]

for num in list:
    print(num)

for i in list:
    if i % 2 == 0:
        print("EVEN NUMNBER: {}".format(i))
    else:
        print(f"ODD NUMBER: {i}")

list_sum = 0
for i in list:
    list_sum = list_sum + i
print(list_sum)

for s in "string":
    print(s)

tup = (1,2,3)

for item in tup:
    print(tup)

list = [(1,2),(3,4),(5,6),(7,8)]

for (a,b) in list:
    print(f"{a},{b}")

dict = {'key':'value','key1':'value1','key2':'value2'}

for item in dict.items():
    print(type(item))
    print(f"{item}")


x = 0

while x <= 5:
    x = x + 1
    print(f"incremented value of {x}")

for i in tup:
    pass

string1 = 'abbca'

for i in string1:
    if i == 'a':
        continue
    else:
        print(i)


for i in string1:
    if i == "c":
        break
    print(i)

for i in range(10):
    print(i)

for num in range(0,10,2):
    print(num)

index_count = 0

for i in "myString":
    print("index {} has alphabet {}".format(index_count,i))
    index_count += 1

for i in enumerate("myString"):
    print(i)

for index,char in enumerate("mystring"):
    print("index {} has alphabet {}".format(index,char))

l1 = [1,2,3,4]
l2 = ['a','b','c','d']

for i in zip(l1,l2):
    print(i)

dict = {'a':1,'b':2}
print('a' in dict)
list = [1,2,3]
print(1 in list)
print(min(list),max(list))


from random import shuffle,randint
shuffle(list)
print(list)


print(randint(0,100))

i = int(input("Enter a number"))
print(i)