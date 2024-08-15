import string
import random

s1 = string.ascii_lowercase
s2 =string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation
plen = (input("Enter password length \n"))

while True:
    try :
        length = int(plen)
        if length < 8 :
            print("Your number should atleast be 8 ")
            plen = (input("Enter password length \n"))
        else :
            break
    except :
        print ("Please enter numbers only")
        plen = (input("Enter password length \n"))
result = []
result.extend(list(s1))
result.extend(list(s2))
result.extend(list(s3))
result.extend(list(s4))
random.shuffle (result)
print("".join(result[0:length]))


