# put your code here
input_number = int(input())
_sum = 0
count = 0
while input_number != 55:
    _sum += input_number
    count += 1
    input_number = int(input())

print(count)
print(_sum)
print(int(round(_sum / count, 0)))
