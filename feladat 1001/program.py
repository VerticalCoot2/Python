import os
import random

os.system("cls")
"""
magassag1=197   #értékadásos modszer
magassag2=165
atlag=(magassag1+magassag2)/2
print("A magasság átlaga", (atlag))


tall1=int(input("Kérem az első magasságot: "))
tall2=int(input("Kérem a második magasságot: "))
atlag2=(tall1+tall2)/2
print("a megadott magasságok átlaga",(atlag2))


#véletlen értéket adjunk meg
tall3=random.randrange(int(input("Adja meg az első kritériumot: ")), int(input("Adja meg az második kritériumot: ")))
tall4=random.randrange(int(input("Adja meg az harmadik kritériumot: ")), int(input("Adja meg az negyedik kritériumot: ")))
print(tall3)
print(tall4)
atlag3=(tall3+tall4)/2
print("A magasságok átlaga:", (atlag3))
"""
randomHIGHT=random.random()*40+150
print("a random magasság", round(randomHIGHT))