input_text = input()

print(input_text.strip("__").strip("~~").strip("**").strip("*").strip("`").strip("_"))
