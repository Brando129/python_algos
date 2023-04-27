# Write A function that will return all the numbers from zero to the input given by a user

def all_integers(num):
    numbers = []
    
    for i in range(0,num+1):
        numbers.append(i)
    return numbers

print(all_integers(10))


