#!/usr/bin/python
#####################
#       Name : Naomi Njeri
#       Date : 6/06/2022
#       file : main.py

import operation
from student import student
from teachers import teachers

operation.add_numbers(4,5)
operation.subtract_number(10,9)
operation.divide_number(2,10)
operation.multiply_number(4,3)

print(operation.add_numbers (4,5))
print(operation.subtract_number (10,9))
print(operation.multiply_number (4,3))
print(operation.divide_number (2,10))

new_student = student("joan","riding",2000)

new_student.greet_student()





