from os import system
from time import sleep
def NewRepo(sT):
    sT=2
    print("This program will automaticcaly add every file to the repository you enter.")
    print("You going to need to log in to GitHub")
    whereAreWe=str()
    hdd=str(input("Please enter the Storage Drive's letter: "))
    folder=str(input("Please enter the folder path: "))
    gitLink=str(input("Please enter just the link to your GitHub repository: "))
    userName=str(input("Please enter your GitHub username: "))
    userEmail=str(input("Please enter your GitHub email: "))
    system(f"cd..")
    system(f"{hdd}:")
    system(f"cd {folder}")
    system(f"git init")
    sleep(sT)
    system(f"git status")
    system(f"git add *.*")
    sleep(sT)
    system(f"git config --global user.name \"{userName}\"")
    system(f"git config --global user.email {userEmail}")
    sleep(sT)
    system(f"git status")
    system(f"git remote add main {gitLink}.git")
    sleep(sT)
    CommentFor=str(input("Comment what did you do? "))
    system(f"git comit -m \"{CommentFor}\"")
def existingRepo(sT):
    sT=2
    print("This program will automaticcaly add every file to the repository you enter.")
    print("You going to need to log in to GitHub")
    whereAreWe=str()
    hdd=str(input("Please enter the Storage Drive's letter: "))
    folder=str(input("Please enter the folder path: "))
    gitLink=str(input("Please enter just the link to your GitHub repository: "))
    userName=str(input("Please enter your GitHub username: "))
    userEmail=str(input("Please enter your GitHub email: "))
    system(f"cd..")
    system(f"{hdd}:")
    system(f"cd {folder}")
    sleep(sT)
    system(f"git status")
    system(f"git add *.*")
    sleep(sT)
    system(f"git config --global user.name \"{userName}\"")
    system(f"git config --global user.email {userEmail}")
    sleep(sT)
    system(f"git status")
    system(f"git remote add main {gitLink}.git")
    sleep(sT)
    CommentFor=str(input("Comment what did you do? "))
    system(f"git comit -m \"{CommentFor}\"")

def Main():
    pass



if __name__=='__main__':
    Main()