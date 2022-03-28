from os import system
from random import randrange
system(f"cls")
def Afeladat(e1,e2,e3):
    print("A feladat")
    return max(e1,e2,e3)
        
def Elefant():
    elefant1=randrange(202,241)
    elefant2=randrange(202,241)
    elefant3=randrange(202,241)
    print(f"Elefántok napi fogyasztása: {elefant1}, {elefant2}, {elefant3}.")
    print(Afeladat(elefant1, elefant2, elefant3))
def Main():
 Elefant()
if __name__=='__main__':
    Main()