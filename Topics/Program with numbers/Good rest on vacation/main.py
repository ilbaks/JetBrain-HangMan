duration =  int(input())
day_food_cost = int(input())
one_way_fly_cost =  int(input())
cost_one_night = int(input())

print(one_way_fly_cost * 2 + duration * day_food_cost + cost_one_night * (duration - 1))
