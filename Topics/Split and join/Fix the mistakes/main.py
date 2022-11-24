text = input()
words = text.split()
for word in words:
    # finish the code here
    if word.lower().find("https://") == 0 or word.lower().find("http://") == 0\
            or word.lower().find("www.") == 0:
        print(word)
