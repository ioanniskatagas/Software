#variables
num1 = float(input("First number: "))
operation = input("Operation: ")
num2 = float(input("Second number: "))

#calculations
if (operation == "+"):
    print (num1 + num2)
    
elif (operation == "-"):
    print (num1 - num2)
    
elif (operation == "/"):
    print (num1 / num2)
    
elif (operation == "x" or "*"):
    print (num1 * num2)
    
else:
    print("Invalid input")
