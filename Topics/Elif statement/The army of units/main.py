number_units = int(input())
if number_units < 1:
    print("no army")
elif number_units >= 1 and number_units <= 9:
    print("few")
elif number_units >= 10 and number_units <= 49:
    print("pack")
elif number_units >= 50 and number_units <= 499:
    print("horde")
elif number_units >= 500 and number_units <= 999:
    print("swarm")
else:
    print("legion")
