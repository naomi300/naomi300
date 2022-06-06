
#f =  open("lesson.txt")
f = open("lesson1.txt")

with open("lesson1.txt","w",encoding="UTF-8")as f :
    f.write("this is my new file\n")
    f.write ("consider a module to be the same as a code library.\n A file containing a set of functions")

#reading a file
print(f.read())
f.close()