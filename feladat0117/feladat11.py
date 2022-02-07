import os
def bevitel():
    a= int(input("a: "))
    b= int(input("b: "))
    return a,b
def muvelet():
    terulet= bevitel()
    print("Terület = ", terulet[0]*terulet[1])

os.system("cls")
muvelet()