import os

def mainfunction():

   directory = input("Input directory file is to be saved to: ")
   filename = input("Input name of the file: ")
   name = input("Input your name (first and last): ")
   address = input("Input your home address: ")
   phone_number = input("Input your phone number: ")


   if os.path.isdir(directory):

       writeFile = open(os.path.join(directory,filename),'w')

       writeFile.write(name+','+address+','+phone_number)

       writeFile.close()

       print("File contents:")

       readFile = open(os.path.join(directory,filename),'r')

       for line in readFile:

           print(line)

       readFile.close()

   else:

       print("Directory does not exist")

mainfunction()