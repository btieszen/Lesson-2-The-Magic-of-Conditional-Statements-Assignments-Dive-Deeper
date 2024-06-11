# Task 2: Identify the Smallest
# enter 3 different numbers identify the smallest
print("What number is smallest?")
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