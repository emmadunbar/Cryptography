"""
cryptography.py
Author: Emma Dunbar
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
print(associ
while True:
    what=input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if what=="q":
        print("Goodbye!")
        break
    if what=="e":
        m1=input("Message: ")
        k1=input("Key: ")
    if what=="d":
        m2=input("Message: ")
        k2=input("Key: ")
    if (what!="q") and (what!="e") and (what!="d"):
        print("Did not understand command, try again.")
        continue
    