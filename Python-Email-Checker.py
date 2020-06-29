import re


def check(inputText):
    """Check if parameter is a valid email and returns true or false"""
    isValidPrefix = False
    isValidSuffix = False
    split = re.split("@", inputText)
    #Check suffix and prefix of address.

    if(len(split) == 2 and isValidPrefix and isValidSuffix):
        return True

    return False
    


print(check("bleh"))
print(check("John@myspace.com"))
