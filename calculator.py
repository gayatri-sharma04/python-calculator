'''

a=int(input("Enter First Number"))

b=int(input("Enter Second Number"))

#a=20
#b=10
print("The sum of 2 number is",a+b)
print("The sub of 2 number is", a-b)
print("The div of two number is", a//b)
'''
class Calculator:
    def calculation(self,a,b,calc):
	
        match calc:
            case "+":
              print(f"The sum of {a} & {b} is: {a+b}")
            case "-":
              print(f"The difference of {a} & {b} is: {a-b}")
            case "*":
              print(f"The multiplication of {a} & {b} is: {a*b}")
            case "/":
              try:
                  print(f"The decimal division of {a} & {b} is: {a/b}")
              except ZeroDivisionError:
                 print("Cannot Divide by Zero")
                 
            case "//":
             try:
        
                 print(f"The integer division of {a} & {b} is: {a//b}")
             except ZeroDivisionError:
                 print("Cannot Divide by Zero")

            case _:
              print("Enter a valid operator")
		  
		  
print("Addition(+)")
print("Subtraction(-)")
print("Multiplication(*)")
print("Decimal Division(/)")
print("Division(//)")
Calculation=input("Enter Your Choice: +,-,*,/,// :- ").strip()
 

	  
x=int(input("Enter First Number:"))
y=int(input("Enter Second Number:"))
c=Calculator()
c.calculation(x,y,Calculation)
	   
	  
	  
	  
 
