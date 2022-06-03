#returning a dictionary from a function


def create_fullname(first_name,second_name):

    person = {'first':first_name,'second ':second_name}

    return person

student=create_fullname('naomi','njeri')
print(student)

#parsing a list in a function
def greet_friends(names):
    for name in names:
        msg=(" hello "+ name.title()+"!")
        print(msg)
friends=['john','letty','mary']
greet_friends(friends)


