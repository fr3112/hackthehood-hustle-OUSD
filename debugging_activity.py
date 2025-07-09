#Debugging Activity - Erika Ramos

#1
x = 10
#y = 0
y =  2
result = x / y #Zero Division Error, you can fixed it by chanching y by other number but not 0
print("Result:", result)

#2
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
   #print(numbers[i+1])
   print(numbers[i]) #Off by one Error, fixed by removing the number that is added to the index

#3
def calculate_area(radius): #Missing colon, Syntax Error,  put a colon after the parentesis of an funtion or loop or if statement
   area = 3.14 * radius ** 2
   return area
 
radius = 5
print(calculate_area(radius))

#4
def is_even(number):
   if number % 2 == 0 : #Syntax Error,Missing colon, put a colon after the statement
       return True
   else :   #Missing colon
       return False
 
print(is_even(4))
print(is_even(7))

#5
for i in range(5): #Syntax Error, Missing colon, put a colon after the loop statement
   print(i)

#6
def greet(name):
   #return "Hello, " name
   return "Hello, " + name  #Syntax Error, if you want to add the variable to the stringg put a +
 
print(greet("Alice"))

#7
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
   sum += number #IndentationError, indent the code inside a function or statement
   print("Sum of numbers:", sum)

#8
def factorial(n):
   if n == 0:
      return 1
   else:
      #return n * factorial(n+1)
      return n * factorial(n-1) #RecursionError, delete the +, put a -

print(factorial(5))

#9
name = input("Enter your name: ")
if name == "Alice" or name == "Bob":  #Incorrect Conditional Statements, you have to put another time name == "Bob", else if you put another name it will not give you "hello, stranger!"
   print("Hello, " + name)
else:
   print("Hello, stranger!")

#10
def divide_numbers(x, y):
   result = x / y
   return result
 
num1 = 10
#num2 = 0
num2 = 5 #ZeroDivisionError, change the value of variable num2 to a non-zero number
print(divide_numbers(num1, num2))
