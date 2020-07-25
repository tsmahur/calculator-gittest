##This is the basic code to calculate the basic operation and it is
##used as a resourse to test the git and github
##Waiting for the pull request...
##
## Function to add two numbers 
def add(num1, num2): 
	return num1 + num2 ;

## Function to subtract two numbers 
def subtract(num1, num2): 
	return num1 - num2 ;

## Function to multiply two numbers 
def multiply(num1, num2): 
	return num1 * num2 ;

## Function to divide two numbers 
def divide(num1, num2): 
	return num1 / num2 ;

## Take input from the user
##pep5 syntax follow refer coursera
##merge print and input statement
print('Enter the value1');
a=int(input());
print('Enter the value2');
b=int(input());
print("Please select operation -\n" 
		"1. Aaddition\n"
		"2. Subtract\n"  
		"3. Multiply\n" 
		"4. Divide\n");
c=int(input("Select operations form 1, 2, 3, 4 :"))


if c == 1: 
	print(a, "+", b, "=", add(a, b)); 

elif c == 2: 
	print(a, "-", b, "=", subtract(a, b)); 

elif c == 3: 
	print(a, "*", b ,"=", multiply(a, b)); 

elif c == 4: 
	print(a, "/", b, "=", divide(a, b)); 
else: 
	print("Invalid input"); 
