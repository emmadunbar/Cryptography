"""
cryptography.py
Author: Emma Dunbar
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

while True:
    what=input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if what=="q":
        print("Goodbye!")
        break
    if what=="e":
        m1=list(input("Message: "))
        k1=list(input("Key: "))
    if what=="d":
        m2=input("Message: ")
        k2=input("Key: ")
    if (what!="q") and (what!="e") and (what!="d"):
        print("Did not understand command, try again.")
        continue
l1=[]
for char in m1:
    num=associations.find(char)
    print(num)
    l1=l1+[num]
print(l1)
for char2 in k1:
    got=associations.find(char2)
    print(got)
    l2=l2+[got]