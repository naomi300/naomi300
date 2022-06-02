#write a program that writes numbers in reverse
number = 789
reversed_number_string = str(number)[::-1]
if type(number) == float:
    reversed_number = float(reversed_number_string)
elif type(number) == int:
    reversed_number = int(reversed_number_string)
    
print(reversed_number)



num = (input('Enter your number: '))
reverse = ''
for i in range(len(num), 0, -1):
   reverse += num[i-1]
print('The reverse number is =', reverse)


