money_user = int(input())
sheep = 6769
cow = 3848
pig = 1296
goat = 678
chicken = 23
if money_user // sheep > 0:
    if money_user // sheep == 1:
        print(str(money_user // sheep) + " sheep")
    else:
        print(str(money_user // sheep) + " sheep")
elif money_user // cow > 0:
    if money_user // cow == 1:
        print(str(money_user // cow) + " cow")
    else:
        print(str(money_user // cow) + " cows")
elif money_user // pig > 0:
    if money_user // pig == 1:
        print(str(money_user // pig) + " pig")
    else:
        print(str(money_user // pig) + " pigs")
elif money_user // goat > 0:
    if money_user // goat == 1:
        print(str(money_user // goat) + " goat")
    else:
        print(str(money_user // goat) + " goats")
elif money_user // chicken > 0:
    if money_user // chicken == 1:
        print(str(money_user // chicken) + " chicken")
    else:
        print(str(money_user // chicken) + " chickens")
else:
    print("None")

