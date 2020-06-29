import re


def check(inputText):
    """Check if parameter is a valid email and returns true or false"""
    isValidPrefix = False
    isValidSuffix = False
    split = re.split("@", inputText)
    if(len(split) != 2 or len(suffix) > 253):
        return False
    prefix = split[0]
    suffix = re.split(".",split[1])
    #Check prefix of address.
    if():
        return False
    #Now check Suffix
    for(domain in suffix):
        if(domain > 63 or ):
            return False
    #if All checks passed then simply return true
    return True
    


print(check("bleh"))
print(check("John@myspace.com"))
