words_list = input().lower().split(" ")
for i in range(1, len(words_list)):
    words_list[i] = words_list[i].capitalize()
print("".join(words_list))
