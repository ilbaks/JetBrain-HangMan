input_sentence = input()
list_all_words = input_sentence.split()
words_with_s = []

for x in list_all_words:
    if x[len(x) - 1] == "s":
        words_with_s.append(x)

result = ""
for _ in range(len(words_with_s)):
    result = "_".join(words_with_s)

print(result)
