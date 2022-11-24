dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

input_words = input().split()
word_in_dictionary = 1
for x in input_words:
    if dictionary.count(x) == 0:
        print(x)
        word_in_dictionary = 0

if word_in_dictionary == 1:
    print("OK")

