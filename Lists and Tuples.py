#List - Have brackets [] starts counting from 0 ITEMS between []
movies = ["Harry Potter", "The Wolf of Wall street", "The Hangover", "The Godfather"]
print(movies[0]) #this will return the first item in the list
print(movies[1])  #this will return the second item in the list
print(movies[0:1]) #will only return first item
print(movies[0:2]) ##will return first 2 items
print(movies[0:]) #will get all
print(movies[:1]) # stops at 1 item and grabs everything before one
print(movies[-1:]) #will grab last item
print(len(movies)) #show amount of items
movies.append("JAWS") #Append will add JAWS to end of the list
print(movies)
movies.pop()  #delete last item on list
print(movies)
movies.pop(0) #Delete first item on list
print(movies)


#Tuples  Do not change, () are like list but cannot be changed
grades = ("a", "b", "c", "d", "f")
print(grades[1])