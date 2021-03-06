import random, os, time
from matplotlib import pyplot as pp

def create_num():
    """ This method generates a 4 digit random number - codeID """
    num = random.randint(1000, 10000)
    n = list(str(num))
    return n

def play_game():
    """ This method is the main logic of the whole game. Here the 4 digit user guess is taken and is evaluated for its correctness """
    bulls = cows = chances = 0
    n = create_num()
    while(bulls != 4):
        chances += 1
        bulls = cows = 0
        guess = (input("Enter your 4-digit guess = "))
        g = list(guess)
        if (len(g) == 4):
            for a in range(4):
                if g[a] in n:
                    print("------------")
                    if (g[a] == n[a]):
                        print("---- BULLS ----!!")
                        print(g[a], "is at correct position")
                        bulls += 1
                    else:
                        print("---- COWS ----!!")
                        print(g[a], "is in the number but at some other position")
                        cows += 1
            print("============================")
            print("Total bulls = ", bulls)
            print("total cows = ", cows)
            print("============================")
            
        else:
            print("-----------")
            print("Invalid guess with wrong length!!")
            print("-----------")
    else:
        print("***Congratulations!!***")
        print("You cracked the code right!!")
        print("You took ", chances, "chances")
        return chances

def check_record(name):
    """ This method will check whether a particular name matches or not in the record """
    present = False
    try:
        with open("PlayerRecord.txt", "r") as fobj:
            fname = fobj.readline()
            while(fname):
                flist = fname.split('\t')
                fname = fobj.readline()
                if (flist[0] == name):        
                    present = True
                    break;
    except FileNotFoundError:
        print("File not found!!")
    return present

def record(name, chances, tot_time):
    """ This method will create a new entry or update an existing entry in the players' records"""
    try:
        fobj = open("PlayerRecord.txt", 'a')
        statinfo = os.stat("PlayerRecord.txt")
        flen = statinfo.st_size
        rec = '\t'.join([name,str(chances), str(tot_time)])
        if flen == 0:
            fobj.write(rec)
            fobj.write('\n')
        else:
            present = check_record(name)
            if (not present):
                fobj.write(rec)        
                fobj.write('\n')
            else:
                update_record(name, chances, tot_time)
        fobj.close()
    except FileNotFoundError:
        print("File not found!!")

def update_record(name, chances, tot_time):
    """ This method updates the existing records but no new record is added """
    try:
        with open("PlayerRecord.txt", "r") as fobj:
            tobj = open("temp.txt", "a")
            fdata = fobj.readline()
            while(fdata):
                flist = fdata.split('\t')
                if (flist[0] == name):
                    fdata = '\t'.join([name, str(chances), str(tot_time)])
                    tobj.write(fdata)
                    tobj.write('\n')
                else:
                    fdata = '\t'.join(flist)
                    tobj.write(fdata)
                fdata = fobj.readline()
            tobj.close()
    except FileNotFoundError:
        print("File Not Found!!")

def read_record():
    """ This method reads and prints the records """
    try:
        with open("PlayerRecord.txt", "r") as fobj:
            rec = fobj.readlines()
            for fdata in rec:
                print(fdata)
            """while(fdata):
                print(fdata)
                fdata = fobj.readline()"""
    except FileNotFoundError:
        print("Records are empty!!")

def view_record():
    pp.title("Players' rank graph based on time taken")
    pp.xlabel("Player Name")
    pp.ylabel("Time taken")
    namelist= []
    timelist = []
    try:
        with open("PlayerRecord.txt", "r") as fobj:
            fdata = fobj.readline()
            while(fdata):
                flist = fdata.split('\t')
                namelist.append(flist[0])
                timelist.append(flist[2].rstrip('\n'))
                fdata = fobj.readline()
    except FileNotFoundError:
        print("Records not found!!")
    namelist.reverse()
    timelist.reverse()
    pp.bar(namelist, timelist)
    pp.show()

def rules():
    print("Hello cracker!! I am Major IntellX - chief-in-officer(IB), your mission head\n\
---------------------------------------------------------------------------------\n\
Your mission is to crack the 4-digit numeric codeID generated by the system\n\
You have to continously enter your guesses till you crack the codeID\n\
You have to accomplish the mission in minimum number of chances\n\
Each guess is checked for \"bulls\" or \"cows\"\n\
BULLS - A particular digit of the guess is present in the codeID and is at right position\n\
COWS - A particular digit of the guess is present in the codeID but at some other position\n\
No. of chances taken and time taken will decide your rank in the Dept.\n\
----------------------------------------------------------------------------------\n\
So use your wit and a pinch of luck and go on for some cracking!!")
# ------main-------
def main():
    print("Hey cracker!!! Let's play COWS & BULLS\n\
The dark world needs you this time to crack some codes\n\
So let's begin!!!!!")
    ch = "n"
    while (ch != "y" and ch != "Y"):
        print("=================================================\n\
Press 'y' to begin\n\
=================================================")
        ch = input()
        
    ch = 0
    while (ch != 4):
        print("Select your choice \n\
1- Mission details\n\
2- Crack a new codeID\n\
3- View records\n\
4- Quit")
        ch = int(input())
        if (ch == 2):
            print()
            name = input("Enter your name = ")
            print("Welcome cracker", name, "you seems to be confident enough that you are here to crack my code!!")
            print("All the best!!")
            t1 = time.time()
            chances = play_game()
            t2 = time.time()
            tot_time = t2 - t1
            print("You took", tot_time, "seconds")
            record(name, chances, tot_time)
            if (os.path.isfile("temp.txt")):
                os.remove("PlayerRecord.txt")
                os.rename("temp.txt", "PlayerRecord.txt")
        elif ch == 1:
            print()
            rules()
        elif ch == 3:
            print("NAME\t\tCHANCES\t\tTIME_TAKEN")
            read_record()
            view_record()
        else:
            print()
            print("Bad choice!!")
    else:
        print()
        print("Thanks for your time!!\n\
Hope you had a great time cracker")

main()
