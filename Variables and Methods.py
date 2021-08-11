#Variables and Methods
quote = "All is fair in love and war." #Variable
print (quote)
#Method
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case
print(len(quote)) #Lenght of quote

name = "Michael" #string
age = 30 #int int(30) define
gpa = 3.7 #float float has decimal points. To define float(3.7)

print(int(age))
print(int(30.1)) #will only show 30 because its integer

#print("My name is " + name + " and I am " + age + " years old.") #can only concatenate str (not "int") to str
print("My name is " + name + " and I am " + str(age) + " years old.") #correct way str format before age

age += 1
print(age)
print("My name is " + name + " and I am " + str(age) + " years old.") #correct way str format before age

birthday = 1
age += birthday
print(age)