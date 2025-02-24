def my_name(name='TESTER'):
    return (f"my name is {name}")


print(my_name("Ravi"))
print(my_name())

def add(num1, num): 
    return(num + num1)

print(add(2,4))

def check_even(number):
    return number % 2 == 0
print(check_even(6))


def check_in_list(number,list):
    return number in list

print(check_in_list(7,[1,2,3,4,5]))

def check_even_in_list(list):
    for num in list:
        if num % 2 == 0:
            return True
        else:
            pass

print(check_even_in_list([1,2,3,4,5]))


def retun_even_elems(list):
    evenList = []
    for i in list:
        if i % 2 == 0:
            evenList.append(i)
        else:
            pass
    return evenList

print(retun_even_elems([1,7]))


stock_prices = [('GOOGLE',100),('META',200),('APPLE',300)]
for stock,price in stock_prices:
    print(f"Stock: {stock} Price: {price}")



def highest_stock(stocks):
    p = 0
    s = ''
    for stock,price in stocks:
        if price > p:
            p = price
            s = stock
        else:
            pass
    return(p,s)

print(highest_stock(stock_prices))


## args & kwargs

# function only takes 5 arguments 
def sixsums(*args):
    return sum(*args) * 0.5

print(sixsums([1,2,4,5,6]))

#args return tuple

def printargs(*args):
    print(args)
    for item in args:
        print(item)

printargs(1,2,3,4,5)


def printkwargs(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print("fruit of choice {}".format(kwargs['fruit']))
    else:
        pass

printkwargs(fruit = 5)


def combined(*args,**kwargs):
    print(args)
    print(kwargs)
    print("I like to have {} {}".format(args[2],kwargs['fruit']))

combined(1,2,3,5,fruit='apple',food='rice',animal='dog')


def lesser_of_two_evens(a,b):
    result = 0
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            result =  a
        else:
            result = b
    else:
        if a < b:
            result = b
        else:
            result = a
    return result

        
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))



def animal_crackers(text):
    first,second =text.split()
    if first[0] == second[0]:
        return True
    else:
        return False
    
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

#### SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(list):
    popList = [0,0,7,'x']
    for item in list:
        if item == popList[0]:
            popList.pop(0)
    if len(popList) == 1:
        return True
    else:
        return False


print(spy_game([1,2,4,0,0,7,5])) #-> True
print(spy_game([1,0,2,4,0,5,7])) #-> True
print(spy_game([1,7,2,0,4,5,0])) #-> False



def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(9))


def listPrime(limit):
    primes = []
    for i in range(2,limit+1):
        if is_prime(i):
            primes.append(i)
        else:
            pass
    return primes

print(listPrime(10))
limit = 10
print([i for i in range(2,limit+1) if is_prime(i)])
