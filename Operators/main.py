# Write a function for arithmetic operators(+,-,*,/)

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Add two numbers
sum = float(num1) + float(num2)

# Substract two numbers
sub = float(num1) - float(num2)

# multiply two numbers
mul = float(num1) * float(num2)

# divide two numbers
div = float(num1) / float(num2)

# display the results

print("The sum of {0} and {1} is {2}".format(num1, num2, sum))
print("The substraction of {0} and {1} is {2}".format(num1, num2, sub))
print("The multiplication of {0} and {1} is {2}".format(num1, num2, mul))
print("The division of {0} and {1} is {2}".format(num1, num2, div))

# Write a method for increment and decrement operators(++, --)

a = 0
a =+ 1
a = a + 1
print("the value of a is: ", a)

#  Write a method for increment and decrement operators(++, --)

print("INCREMENT FOR LOOP")
for i in range(0, 5):
    print(i)

print("\nDECREMENTED FOR LOOP")
for i in range(4, -1, -1):
   print(i)

# Write a program to find the two numbers equal or not.

a = input("enter first number: ")
b = input("enter second number: ")
if a==b:
    print("the input value is equal")
else:
    print("the input value is not equal")

# Print the smaller and larger number.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
#To print larger number
if a > b:
    print(a, "is greter")
else:
    print(b, "is greter")
    
#To print samller number
if a < b:
    print(a, "is smaller")
else:
    print(b, "is smaller")
