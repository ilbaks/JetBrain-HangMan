lower_camel_case = list(input())
snake_case = []
for x in lower_camel_case:
    if x.isupper():
        snake_case.append("_")
    snake_case.append(x)
print(''.join(snake_case).lower())
