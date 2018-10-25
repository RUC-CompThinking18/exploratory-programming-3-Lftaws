#Importing the file A_padre_in_france
import re
file = open("A_padre_in_france.txt", "r")
infile = file.read()

#Beginning of the function that holds the type check and while loop
def guten(x):

#If statement to check if the file is a text file. If not, raises a TypeError
    if type(x) != str:
        raise TypeError

#If no TypeError is raised, continues with the program
# m equals all the words that end in AT in the findall function, it then prints
#out m, which then is put into the list called WordList
    else:
        #\w+at\b is used to find words that end in at
        m = re.findall(r"\w+at\b", x)
        WordList = [m]
        print (m)
#A while loop that determines that if m is greater than 3 letters presumably,
#then it will return the word in the list that has more than 3 letters.
    while [m] > 3 :
        return WordList
guten(infile)

#The file itself is hard to see work. However with the use of jupyter or pythons
#IDLE, it can be seen working .
