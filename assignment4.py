
#write a program to withdraw ksh 25000 if account balance is between ksh 10000 to 200000 30%if account bal is btwn 500000 and 1million
#above 100000 deduct 150000
acc_bal= input("enter accont bal")
if (int(acc_bal))>1000000 and (int(acc_bal)<200000): 
  acc_bal=acc_bal-25000
  print("we have deducted ksh 25000")
elif(int (acc_bal))>500000 and(int(acc_bal)<1000000):
    acc_bal=acc_bal-(acc_bal*0.3)
    print("we have deducted 30% from your account")
elif(int(acc_bal)>1000000):
    acc_bal=acc_bal-15000
    print("we have deducted 15000")
else:
    print("no deducting")













