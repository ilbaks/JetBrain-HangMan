words_list = input().lower().split("_")
for i in range(len(words_list)):
    words_list[i] = words_list[i].capitalize()
print("".join(words_list))
