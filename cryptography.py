"""
cryptography.py
Author: Emma Dunbar
Credit: Geoff Dunbar, Learn Python

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
        l1=[]
        l2=[]
        for char in m1:
            num=associations.find(char)
            l1=l1+[num]
        for char2 in k1:
            got=associations.find(char2)
            l2=l2+[got]
        s=len(l1)/len(l2)+1
        l2=int(s)*l2
        l3=[]
        h=('')
        for i in range(0,len(l1)):
                j=l1[i]+l2[i]
                l3=l3+[j]
        for f in l3:
            if f>=len(associations):
                f=f-len(associations)
            e=associations[f]
            h=h+e
        print(h)
    if what=="d":
        m2=input("Message: ")
        k2=input("Key: ")
        l1=[]
        l2=[]
        for char in m2:
            num=associations.find(char)
            l1=l1+[num]
        for char2 in k2:
            got=associations.find(char2)
            l2=l2+[got]
        s=len(l1)/len(l2)+1
        l2=int(s)*l2
        l3=[]
        h=('')
        for i in range(0,len(l1)):
                j=l1[i]-l2[i]
                l3=l3+[j]
        for f in l3:
            e=associations[f]
            h=h+e
        print(h)
    if (what!="q") and (what!="e") and (what!="d"):
        print("Did not understand command, try again.")
        continue