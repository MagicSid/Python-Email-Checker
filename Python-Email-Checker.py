import re


def check(inputText):
    """Check if parameter is a valid email and returns true or false"""
    isValidPrefix = False
    isValidSuffix = False
    split = re.split("@", inputText)
    if(len(split) != 2):
        return False
    prefix = split[0]
    suffix = split[1]
    #Check prefix of address.
    if():
        return False
    #Now check Suffix
    if():
        return False
    #if All checks passed then simply return true
    return True
    


print(check("bleh"))
print(check("John@myspace.com"))
