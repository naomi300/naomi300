#ask user to select which input to check number or letter
#palindrome number is a number that when reversed it remains the same



msg = input("enter a number to check if it is a palindrome   ")
if msg==msg[::-1]:
    print("this number is a palindrome")

else:
    print("this number is not a palindrome")

msg = input("enter a letter to check palindrome  ")
if msg==msg[::-1]:
    print("this letter is a palindrome")

else:
    print("this letter is not a palindrome")


    