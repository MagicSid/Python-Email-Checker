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
    if(
    
    #Now check Suffix
    
    #Final checks for validity
    if(isValidPrefix and isValidSuffix):
        return True
    else:
        return False
    


print(check("bleh"))
print(check("John@myspace.com"))
