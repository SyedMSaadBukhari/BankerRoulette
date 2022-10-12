import random
Name_Of_Friends = input("Give all names separated by comma: \n")
name = Name_Of_Friends.split(",")
length = len(name)

random_name = random.randint(0, length -1 )
payer = name[random_name]
print(f"{payer} ia going to buy the meal today!")
