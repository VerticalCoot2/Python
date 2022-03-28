from os import system
def taskA(list_):
    print(", ".join([i for i in list_ if i[0]=='T' or i[0]=='t']))

def taskB(list_):
    count = 0

    for i in list_:
        count += str.count(i, "a")
    
    print(count)

def taskC(list_):
    newlist = list(map(len, list_))
    i = list.index(newlist, max(newlist))
    print(list_[i])

def main():
    szavak = ['ajtó','tojás','Otto','Tamás','njnjknknjknjknjk','tép','Tesla','alma','python']
    taskA(szavak)
    taskB(szavak)
    taskC(szavak)
if __name__=='__main__':
    main()