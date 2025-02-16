string1 = "hello"
print(string1[-1]) # last index of the string [start:stop:step]

print("hello \n world")

print(len("hello world"))

print(string1[2:])
print(string1[:2])
print(string1[1:5])

print(string1[::]) #pick entire string 

print(string1[::2])

print(string1[1:4:2])

print(string1[::-1]) #reverse string 


# strings are immutable 

name = "Hello"
#name[0] = "B"
#print(name)  string is immutable 

newName = "B"+ name[1:]
print(newName)
print("B"+name[1:])

alphabet = "a"

print(alphabet * 10)

print(2+4)
print('2'+'4') #"24"


s = "hello world" 
print(s.upper())

print(s.split(" "))
print(s.split("o"))

print("hello my name is {1} {0}".format("Ravi","Gupta"))

decimalValue = 100/7

print("decimal value: {d:1.5f}".format(d=decimalValue))

## formatted printing 

print(f"hey Good morining{s}")