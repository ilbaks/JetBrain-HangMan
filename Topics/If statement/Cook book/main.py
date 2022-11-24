pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

time_string = ' time!'
ingredient = input()

if ingredient in pasta:
    print('pasta' + time_string)
if ingredient in apple_pie:
    print('apple pie' + time_string)
if ingredient in ratatouille:
    print('ratatouille' + time_string)
if ingredient in chocolate_cake:
    print('chocolate cake' + time_string)
if ingredient in omelette:
    print('omelette' + time_string)
