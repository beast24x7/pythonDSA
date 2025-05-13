"""
(n-1)2 = n2 + 1 - 2n
(n-1)2 + 2n -1 = n2

"""
def square(num) -> int:
    if num == 0:
        return 0
    else:
        return square(num-1) + (2 * num) -1
    
print(square(10))