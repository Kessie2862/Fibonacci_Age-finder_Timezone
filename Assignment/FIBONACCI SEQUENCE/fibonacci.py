print('python program that sums even numbers in a Fibonacci sequence from 10 and not exceeding 200.')

x = [] # let's say 'x' is an empty array
a = 10 # where a is the first term in the sequence
b = 11 # where b is the second term in the sequence
c = a + b # c is the sum of the last two numbers in the sequence i.e (a + b)

# checking to make sure c is less than 200.
while c < 200:
    a = b
    b = c
    c = a + b

    # since we're only interested in even numbers, let's check to see and then insert to x
    if c % 2 == 0:
        x.insert(0, c)
    print(x)

# add sum of the list 
numSum = (sum(x))

# print sum
print(numSum)



