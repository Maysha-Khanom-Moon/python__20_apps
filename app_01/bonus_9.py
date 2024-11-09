'''
Strong password:
    1. minimun length 8 
    2. minimum one upper and lower case character
    3. minimum one digit
    4. minimum one special character
'''

#  way 1:
# -------
print("First way")
print("---- ----")

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

digits = '0123456789'
special = '~!@#$%^&*()_-[]{}<>,/?|'

password = input("Enter new password: ")

checkLen = True if len(password) >= 8 else False


# checkLower = False
# for i in password:
#     if i in lower:
#         checkLower = True

checkLower = any(i in lower for i in password)
checkUpper = any(i in upper for i in password)
checkDigit = any(i in digits for i in password)
checkSpecial = any(i in special for i in password)

if checkLen and checkLower  and checkUpper and checkDigit and checkSpecial:
    print("Strong password\n")
else:
    print("Weak password\n")


#  way 2:
# -------

print("Second way")
print("----------")
password = input("Enter new password: ")

# dictionary --> {(key, value)}
# value: data
# key: metadata
# dir(dict)
results = {}

if len(password) >= 8:
    results["length"] = True
else:
    results["length"] = False


lower = False
for i in password:
    if i.islower():
        lower = True

results["lower"] = lower


upper = False
for i in password:
    if i.isupper():
        upper = True

results["upper"] = upper


digit = False
for i in password:
    if i.isdigit():
        digit = True

results["digit"] = digit


print(results)

# results.values() --> returns a list of values
if all(results.values()):
    print("Strong password")
else:
    print("Weak password")