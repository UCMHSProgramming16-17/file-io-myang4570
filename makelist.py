# open file in write mode 
file = open("listfile.txt", "w")

#TODO: create the list
file.write("Hello Mariya\n")

for n in range(10): 
    file.write(input("Please talk to me!") + "\n")
    
#close file
file.close()