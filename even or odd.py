n1 = int(input('enter your number:',))  
even = True

# Checking if the number is even or odd
if n1%2 == 0:
    print('It\'s an even number.')
else :
    print('It\'s an odd number.')
    even=False
    

# Adding another number if even
if even:
    print('New value',n1+5)
else:
    print('New value',n1-5)
