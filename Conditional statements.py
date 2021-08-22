#Conditional statements
def drink(money):  #money = parameter
        if money >= 2:
                return "you've got yourself a drink!"
        else:
                return "NO drink for you!"
print(drink(3))  #3 = parameter
print(drink(1)) #1 = paramter

def alchohol(age,money):
                if (age >=21) and (money >= 5):
                                return "we're getting a drink!"
                elif (age >= 21) and (money < 5):
                                return "Come back with more money"
                elif (age < 21) and (money >= 5):
                                return "Nice try kid"
                else:
                        return "you're too poor and too young"



print(alchohol(21,5))
print(alchohol(21,4))
print(alchohol(20,4))