import random
import sys

def Game():
    sl = int(input("Set difficult 1 - (1-6), 2 - (1-9)"))
    var1 = 0
    ans = [0, 0, 0, 0]
    all2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    all1 = [1, 2, 3, 4, 5, 6]
    if sl == 1:
        all = all1
    elif sl == 2:
        all = all2
    for i in range(len(ans)):
        ans[i] = random.choice(all)
        all.remove(ans[i])
    list_of_str = [str(n) for n in ans]
    ans.clear
    ans = list_of_str
    sos = list()
    for i in range(0, 10):
        place = 0
        all = 0
        if i == 0:
            var1 = str(input("Start the game: "))
            sos = var1.split(' ')
            print(sos)
        else: 
            var1 = str(input("Try again: ((For exit print (exit)"))
            if var1 == "exit":
                sys.exit()
            sos = var1.split(' ')
        for a in range(len(ans)):
            if ans[a] == sos[a]:
                place = place + 1
            if any(element in sos[a] for element in ans):
                all = all + 1
        if place == 4:
            print("!!!YOU WIN!!! CONGRATULATIONS!!!", "TRIES: ", i, "!!!")
            sys.exit()
        print("|all: ", all, "|On place: ", place, "|TRIES: ", 10 - 1 - i, "|")
    print(ans)
Game()
