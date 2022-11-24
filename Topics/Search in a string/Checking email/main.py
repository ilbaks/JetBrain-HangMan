def check_email(string):
    if string.find(" ") > -1:
        return False
    elif string.find("@") == -1:
        return False
    elif string.find(".") == -1 or string.index(".", string.find("@")+1) and string.index(".", string.find("@")+1) == string.index("@")+1:
        return False
    return True
