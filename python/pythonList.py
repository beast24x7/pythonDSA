myList = [1,2,3]
print(len(myList))

myList = ['a',1,3]

print(myList[1:])

myList2 = ['b',4,5]

newList = myList + myList2
newList[0] = "HELLO"

print(newList)

newList.pop()
newList.pop(0) #index based popping

print(newList)

l1 = [7,2,0,10,5]
l1.sort()
print(l1)
l2 = l1.sort()
print(l2) #returns None