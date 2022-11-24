# put your python code here
sequence_numbers = input().split(" ")
x = input()

res = ""
for i in range(len(sequence_numbers)):
    if x == sequence_numbers[i]:
        if res != "":
            res = res + " " + str(i)
        else:
            res = res + str(i)

if res == "":
    res = "not found"
print(res)
