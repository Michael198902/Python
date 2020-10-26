#countdown recursion example

def countdown(x):
    if(x==0):
        print("done!")
        return
    else:
        print(x,"...")
        countdown(x-1)

countdown(4)

#Power of and Factorial:

def power(num, pwr):

    if (pwr == 0):
        return 1
    else:
        return num*power(num, pwr-1)



#5! = 5x4x3x2x1 = 120
#0! = 1
def factorial(val):
    if (val==0):
        return 1
    else:
        return val*factorial(val-1)


print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
print("{} to the power of {} is {}".format(1, 5, power(1, 5)))
print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(0, factorial(0)))
