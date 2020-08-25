import re

#Legitimate Character Sets "[a-z][0-9][!#\$%&'\*\+/=?\^_`\{\|\}~-]"

def check(inputText):
    """Check if parameter is a valid email and returns true or false"""
    #First sanitise input by lowercasing the input
    inputText = inputText.lower()
    isValidPrefix = False
    isValidSuffix = False
    split = re.split("@", inputText)
    if len(split) != 2:
        return False
    
    prefix = split[0]
    suffix = re.split("\.",split[1])
    if len(split[1]) > 253 or len(prefix) > 64 or prefix[0:1] ==".":
        return False
    
    #Check prefix of address.
    legitChars = "(([a-z]*[0-9]*[!#$%&'*+/=?^_`{|}~. -]*)*)"
    legitCharsPlus = "(([a-z]+|[0-9]+|[!#$%&'*+/=?^_`{|}~-]+)+)"
    testpre = re.sub("(\." + legitCharsPlus + ")+|" + legitCharsPlus + "|(\""+ legitChars +"\")","",prefix)
    if(testpre != ""):
        return False
    #Now check Suffix
    legitChars = "(([a-z]*[0-9]*)*)"
    legitCharsPlus = "(([a-z]+|[0-9]+)+)"
    for domain in suffix:
        if(len(domain) > 63 or domain == "" or domain[0:1] == "-"):
            return False
        testsuf = re.sub("(\-" + legitCharsPlus + ")+|" + legitChars,"",domain)
        if(testsuf != ""):
            return False
    #if All checks passed then simply return true
    return True

#Test no @
print("@ test")
print("Should Fail:" + str(check("bleh")))

#Test Prefix
print("Prefix tests")
print("Should succeed:" + str(check("Jo.hn@myspace.com")))
print("Should succeed:" + str(check("J.o.hn@myspace.com")))
print("Should Fail:" + str(check(".John@myspace.com")))
print("Should Fail:" + str(check("John.@myspace.com")))
print("Should succeed:" + str(check("\"Jo..hn\"@myspace.com")))
print("Should Fail:" + str(check("Jo..hn@myspace.com")))
print("Should succeed:" + str(check("!#$%&'*+-/=?^_`{|}~@bleh.com")))

#Test Suffix
print("Suffix tests")
print("Should succeed:" + str(check("John@myspace.com")))
print("Should succeed:" + str(check("John@myspace.co-m")))
print("Should fail:" + str(check("John@myspace-.com")))
print("Should fail:" + str(check("John@-myspace.com")))
print("Should fail:" + str(check("John@myspace.-com")))
print("Should fail:" + str(check("John@myspace.com-")))

input("Press Enter to end")
