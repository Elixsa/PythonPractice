#3.2.1.15 LAB: Collatz's hypothesis
import time
while True:
    c0 = int(input("Enter in a non-zero number\n"))
    if c0>0:
        break
    print("Scallywag, try again")
    time.sleep(1)
steps = 0
#print("how are we doing?")
while c0 > 1:
    if c0 % 2 == 0:
        c0 //= 2
    else:
        c0 = c0*3 + 1
    steps += 1
    print(c0)
print("Steps:",steps)
