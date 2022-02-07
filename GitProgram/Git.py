from os import system
import sys
def Main():
    print("This program will automaticcaly add every file to the repository you enter.")
    print("You going to need to log in to GitHub")
    hdd=str(input("Please enter the Storage Drive's letter"))
    folder=str(input("Please enter the folder path"))
    gitLink=str(input("Please enter just the link to your GitHub repository"))
    userName=str(input("Please enter your GitHub username"))
    userEmail=str(input("Please enter your GitHub email"))
    system(f"{hdd}:")
    system(f"cd {folder}")
    system(f"git init")
    system(f"git status")
    system(f"git add *.*")
    system(f"git status")
    system(f"git config --global user.name \"{userName}\"")
    system(f"git config --global user.email {userEmail}")
    system(f"git remote add main {gitLink}.git")




if __name__=='__main__':
    Main()