input_text = input()

print_text = input_text
print_text = print_text.replace(",", "")
print_text = print_text.replace(".", "")
print_text = print_text.replace("!", "")
print_text = print_text.replace("?", "")

print(print_text.lower())
