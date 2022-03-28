from os import system
from random import randrange


def Veletlen(mennyiseg,min,max):
    return [randrange(min,max+1) for i in range(mennyiseg)]

def Letezik(lista, keresett):
    return keresett in lista

def Oszthato(lista, oszto):
    return [i for i in lista if i % oszto == 0]

def Legnagyobb(lista,tavolsag):
    ujlista = [lista[i]  for i in range(tavolsag)]
    print(max(ujlista))

def Main():
    system("cls")
    lista = Veletlen(10,30,50)
    print(lista)
    print(Letezik(lista,37))
    print(Oszthato(lista,3))
    Legnagyobb(lista,5)
    




if __name__ == "__main__":
    Main()