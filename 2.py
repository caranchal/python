import random
print("--------------------------")
print("камень ножницы бумага")
print("веберите вариант")

player_score = 0
player_select = 0
comp_score = 0
comp_select = 0
for i in range(3):
    print("\t-----------ROUND  " + str(i + 1)+"--")
    comp_select = random.choice("rps")
    player_select = ""
    while True:
        if (player_select == "r") or (player_select == "p") or (player_select == "s"):
            break
        else:
            player_select = input("введите r or p or s")
    if player_select == comp_select:
        print("ничья")
    elif player_select == "s" and comp_select == "p":
        print("игрок выйграл")
        player_score +=1
    elif player_select == "p" and comp_select == "r":
        print("игрок выйграл")
        player_score +=1
    elif player_select == "s" and comp_select == "r":
        print("компьютер победил")
        comp_score +=1
    elif player_select == "r" and comp_select == "p":
        print("компьютер победил")
        comp_score +=1
    elif player_select == "p" and comp_select == "s":
        print("игрок победил")
        player_score +=1
    elif player_select == "r" and comp_select == "s":
        print("игрок выйграл")
        player_score +=1
    elif player_select == "p" and comp_select == "s":
        print("компьютер победил")
        comp_score +=1
    elif player_select =="s" and comp_select == "r":
        print("компьютер победил")
        comp_score +=1
    if comp_score >=2:
        print("компьютер победил")
    if player_score >=2:
        print("игрок победил")









