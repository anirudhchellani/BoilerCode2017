# @Description : Recursive Functions - Factorial

def Factorial(num):
    if num == 1:
        return 1
    else :
        return num * Factorial(num-1)

def main():
    print "Factorial of 5 is ", Factorial(5)

main()
