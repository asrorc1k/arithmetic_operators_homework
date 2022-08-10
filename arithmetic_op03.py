#Create a variable called 'number' and assign it the two-digit number
number = 12
#Find the reverse of the number and assign it to a variable called 'answer'.
a = number % 10
a = str(a)
number //= 10
number = str(number)
answer = a + number
#Print the answer variable
print(answer)