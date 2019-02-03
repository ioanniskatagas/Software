#variables
int1 = int(input("First number"))
operation = input("Operation")
int2 = int(input("Second number"))

#calculations
if (operation == "+"):
    print (int1 + int2)
    
elif (operation == "-"):
    print (int1 - int2)
    
elif (operation == "/"):
    print (int1 / int2)
    
elif (operation == "x" or "*"):
    print (int1 * int2)
    
else:
    print("Invalid input")
