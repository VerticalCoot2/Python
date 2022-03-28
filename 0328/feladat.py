from os import system as ww

def main():
    kulon()
def elsoSor():
    be=open("szuletes.txt","r", encoding="utf-8")
    line=be.readline()
    be.close()
    print(line)

def stringLIST():
    be=open("szuletes.txt", encoding="utf-8")
    lines=be.readlines()
    be.close()
    print(lines)
    for i in range(len(lines)):
        lines[i]=lines[i].strip()
    print(lines)

def kulon():
    szemelyek=[]
    be=open("szuletes.txt", encoding="utf-8")
    for sor in be:
        sor = sor.strip().split(" ")
        sor[2]=int(sor[2])
        szemelyek.append(sor)
    be.close()
    for i in range(len(szemelyek)):
        for j in range(3):
            print(szemelyek[i][j], end=" ")
        print("")
    ki=open("adatok.txt","w",encoding="utf-8")
    print(szemelyek[1][1],file=ki)
    ki=open("adatok.txt","a",encoding="utf-8")
    print(szemelyek[2][1],file=ki)
    ki.close()
    

def egesz():
    ww("cls")
    be=open("szuletes.txt", encoding="utf-8")
    text=be.read()
    be.close
    print(text)
    textlist=text.split("\n")
    print(textlist)


if __name__ =='__main__':
    main()