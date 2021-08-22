#Dictionaries - Key/Value pairs {}

drink = {"gin": 7, "duvel": 4, "Limoncello": 8} #drink is key, price is value ( key value pair )
print(drink)

employees = {"Finance": ["bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy JR", "Mort"]}
print(employees)

employees['legal'] = ["Mr. Frond"] #Add new key/Value pair
print(employees)

employees.update({"Sales": ["Andy", "Ollie"]}) #Multiple ways to add new key/value pairs
print(employees)

drink['gin'] = 8  #updates price
print(drink)

print(drink.get("gin"))