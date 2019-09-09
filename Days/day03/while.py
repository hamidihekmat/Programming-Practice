import time
n = 10

# as long as n -> 10 is greater than 0, loop through this block of code
while n > 0:
    print(n)
    time.sleep(1)
    n -= 1
print('Blast off!')
