def count(array, key):
    if array == []:
        return 0
    if array[0] == key:
        return 1 + count(array[1:],key)
    else:
        return 0 + count(array[1:],key) 
    
print(count([1,2,3,4,1],1))