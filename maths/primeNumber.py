import math
def check_prime(n):
    counter = 0

    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            counter += 1
            if int(n/i) != i and n/1:
                counter +=1
    return True if counter == 2 else False