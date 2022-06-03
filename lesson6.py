#learning about lists
plate_number=['KAZ456U','KPS900T','KUY235K']
motorcycle =['honda','suzuki','yamaha']
#accesing lists items using index
#print(motorcycle)
#print(motorcycle[0])
#print(motorcycle[1])
motorcycle[0]='Bugati' #changing element in a list 
#print(motorcycle)
motorcycle[1]='bugati'

#deleting an from a list...del
del motorcycle[0]#deleting an item from a list
print(motorcycle)
del motorcycle[0]
print(motorcycle)
#task print a statement.
#print("my name is(motorcycle owner) and on a [motorcycle[0]plate number(KAZ123W)")


#removing an item from a list
motorcycle.remove("honda")
print(motorcycle)