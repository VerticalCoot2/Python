import os

os.system("cls")
num = int(input("Adjon meg egy 7nél nagyobb számot: "))
while(num<=7):  
    szam=int(input("Buta vagy, de megpróbálhatod mégegyszer :)"))

input("")
os.system("cls")

again = "i"
while(again == "i"):
    a = int(input("1 szam:"))
    b = int(input("1 szam:"))
    osszeg = a+b
    print("A két szám összege: ", osszeg, "\n")
    again=input("akarsz még egyet számolni?(i/n)")
    os.system("cls")