#positive or negitive number
num1 = int(input("enter your number"))
if num1 >0:
    print("The number that you have given is: positive")
else:
    print("The number that you have given is: negitive")

print("next line of execution")

# profit and loss
cp = int(input("enter your cost price of your item"))
sp = int(input("enter your selling price of your item"))
if sp>cp:
    p = sp-cp
    print(f"you have a profit of {p}") 
else:
    loss = cp-sp 
    print(f"you have a loss of {loss}") 

# even or odd
num2 = int(input("enter your number"))
if (num2 %2==0):
    print("your entered number is even")    
else:
    print("your entered number is odd")    

 # checking number is greator or smaller
if num1 > num2:
    print(f"{num1} is greator that {num2}")
else:
    print(f"{num2} is greator that {num1}")    

