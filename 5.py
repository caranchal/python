import random
print("проверка на знание умножения")
human = random.choice(1234567890)
human_score = 0
human = int(input("2*2=?"))
if human == 4:
    print("правильно")
    human_score +=1
else:
    print("неправильно")
human = int(input("4*5=?"))
if human == 20:
    print("правильно")
    human_score +=1
else:
    print("неправильно")
human = int(input("5*5=?"))
if human == 25:
    print("правильно")
    human_score +=1
else:
    print("неправильно")
if human_score ==3:
    print("оценка 5")
elif human_score <3:
    print("оценка 4")



