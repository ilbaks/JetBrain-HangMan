# put your python code here
x = int(input())
list_numbers_input = []
while x <= 100:
    if x < 10:
        x = int(input())
        continue
    list_numbers_input.append(x)
    x = int(input())

for _number in list_numbers_input:
    print(_number)
