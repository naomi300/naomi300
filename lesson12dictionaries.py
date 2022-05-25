#!/usr/bin/python

#dictionaries is a collection of key value pairs
#syntax: dictionary = ["key":"value"]


from turtle import color


name ="naomi njeri"
colors={"color":"red"}
vehicle = {"type":"vanguard","plate_number":"KER234R"}
print(type(colors))
print(type(name))
#accessing values in a dictionary - using the key
print(vehicle["type" ],vehicle['plate_number'])

# dictionary person
person={"name":"naomi","gender":"female","id_number":"234567","location":"nairobi","phone_number":"012386435"}
person["age"]="20"#adding
person["favorite color"]="blue"
print(type(person))
print(person)

print(person["name"],person["favorite color"],person["age"])
del person["id_number"]
print(person)

#loop over dictionaries- using loops
for key, value in person.items():
    print (f"{key}:{value}")
    

colors=["blue","red","pink","yellow"]



f(color[1])==blue):
print(color[1].uppercase{})
  





















