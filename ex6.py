#Declare variable types_of_people
types_of_people = 10
#Format types_of_people into x
x = f"There are {types_of_people} types of people"
#Create variable with the strings binary, and don't
binary = "binary"
do_not = "don't"
#Add above strings into a thrid string
y = f"those who know {binary} and those who {do_not}."
#Print both the strings
print(x)
print(y)
#Print them again
print(f"I said {x}")
print(f"I also said {y}")
#assign hilarious as False
hilarious = False
#assign string into joke evaluation, and prepare it to be formatted
joke_evaluation = "Isn't that joke so funny?! {}"
#print joke_evaluation and format hilarious into it
print(joke_evaluation.format(hilarious))
#assign two stings into two variables
w = "this is the left side of..."
e = "a string with a right side"
#concatinate both variables and print them
print(w + e)
