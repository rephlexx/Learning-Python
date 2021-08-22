#Advanced Strings

my_name = "Michaël"
print(my_name[0])  #Print first letter in my name
print(my_name[-1]) #Print last letter from my name

sentence = "this is a sentence"
print(len(sentence)) #lengt of sentence
print(sentence[:4])  #prints first 4

print(sentence.split())  #splits based on a delimiter in this case its a space

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)  #join a sentence and add own delimiter
print(sentence_join)

quote = "He said, 'give me all your money'"  #adds quotes to a sentence with the ' '
print(quote)

quote = "He said, \"give me all your money\""  # \ to keep this string a string it will ignore the characters between the \
print(quote)

too_much_space = "                            HELLO                     "  # Will strip the spaces
print(too_much_space.strip())

print("A" in "Apple")   #Looks for A in Apple Case sensitive  TRUE
print("a" in "Apple")   #Looks for a in Apple Case sensitive  FALSE

letter = "A"
word = "Apple"
print(letter.lower() in word.lower())  #Improved

movie = "The hangover"
print("My favorite movie is {}.".format(movie))  #Placeholders {}
