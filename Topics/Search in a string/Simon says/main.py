def what_to_do(instructions):
    if  instructions.startswith("Simon says") == True or instructions.endswith("Simon says") == True:
        str =  instructions.replace("Simon says", "")
        str = str.strip()
        return "I " + str
    return "I won't do it!"
