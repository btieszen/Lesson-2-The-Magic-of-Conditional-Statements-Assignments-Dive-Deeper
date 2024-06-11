#Task 3: Equality Check
number1 = int(input("please enter a number "))
number2 = int(input("please enter a different number "))
number3 = int(input("Please enter the final number  "))
print("The smallest number is:")
if number1 < number2:
    print (number1)
elif number2 <  number3:
    print(number2)
elif number1 > number3:
    print(number3)
print("The biggest number is:")
if number1 > number2:
    print (number1)
elif number2 >  number3:
    print(number2)
elif number1 < number3:
    print(number3)
print (" the idintical numbers are: ")
if number1 == number2:
    print (number1)
elif number1 == number3:
    print (number1)
elif number2 ==number3:
    print (number3)
if number1 == number2 == number3:
    print ("all numbers are the same")
if number1 !=(number2)!=(number3):
    print ("there are no identical numbers")
    

    

    

