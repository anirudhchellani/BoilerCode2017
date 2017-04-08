def power(num1, num2):
    if (num2 == 1):
        return num1
    else:
        return num1*power(num1,num2-1)

print power(int(input("Number:")),int(input("Power:")))
