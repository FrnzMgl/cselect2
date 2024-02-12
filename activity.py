

def calculator(operator, num1, num2): #created a function

    def add(num1, num2): #created a function
       return num1 + num2 #return result of the two numbers
    def subtract(num1, num2): #created a function
        return num1 - num2 #return result of the two numbers
    def divide(num1, num2):#created a function
        return num1 / num2#return result of the two numbers
    def multiply(num1, num2):
        return num1 * num2
    
    if operator == '+':
        return add(num1, num2) #return the result of the two numbers
    if operator == '-':
        return subtract(num1, num2) #return the result of the two numbers
    if operator == '/':
        return divide(num1, num2) #return the result of the two numbers
    if operator == '*':
        return multiply(num1, num2) #return the result of the two numbers
    
print(calculator('+',2,2))
print(calculator('-',2,2))
print(calculator('*',2,2))
print(calculator('/',2,2))

