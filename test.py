import random

while True:
    igrock_1 = input("Выберите игрока, указав цифру: \n1) Василиса Огненкая \n2) Алиса Мгновенная \n3) Дмитрий Теневед \n")

    if igrock_1 == "1":
        pers_1 = "Василису Огненкая"
        print(pers_1)
        break
    elif igrock_1 == "2":
        pers_1 = "Алису Мгновенную"
        print(pers_1)
        break
    elif igrock_1 == "3":
        pers_1 = "Дмитрия Теневеда"
        print(pers_1)
        break
    else:
        print("Такого персонажа нет, выберите еще раз")

# Персонаж второго игрока
igrock_2 = random.randint(1, 3)

if igrock_2 == 1:
    pers_2 = "Василису Огненкая"
    print(pers_2)

elif igrock_2 == 2:
    pers_2 = "Алису Мгновенную"
    print(pers_2)

elif igrock_2 == 3:
    pers_2 = "Дмитрия Теневеда"
    print(pers_2)

else:
    print("Такого персонажа нет, выберите еще раз")

# Сохранение выборов персонажей
games = pers_1
games2 = pers_2
print(games, games2)
# жизни игроков
xp_players = 100
xp_players2 = 100

#способности
spos = 0
spos2 = 0

# бафы дебафы
gamebafdebuf ={"baf": "","debaf": ""}
gamebafdebuf2 ={"baf2": "","debaf2": ""}

time_stop = False
time_stop2 = False

print(f"Игроки выбрали своим персонажей битва начилась")
while True:
    print(f"Ход первого игрока")
    if not time_stop:
        action = input("Выберите ход написав цифру: \n1)Атака \n2)Способность \n")
        
        if action == "1":
            if "Доспех огня" in gamebafdebuf2.values():
                xp_players2 -= 5
                xp_players -= 5
                spos += 10
            elif "Плащ тьмы" in gamebafdebuf2.values():
                print("плащьт есть")
                chance = 0.4 # Шанс выпадения
                if random.random() < chance:    
                    print(f"Вы нанесли урон")
                    xp_players2 -= 15
                    spos += 15
                else:
                    print(f"Вы промахнулись")
                    spos += 10
            
            elif "Доспех огня" not in gamebafdebuf2.values():
                xp_players2 -= 10
                spos += 15
            

        elif action == "2":
            if spos >= 100:
                spos = 100
            if spos == 100:
                if games == "Василису Огненкая":
                    print(f"Вы наложили на себя огненый доспех")
                    gamebafdebuf["baf"] = "Доспех огня"
                    spos -= 100
                    continue
                elif games == "Алису Мгновенную":
                    print(f"Вы остановили время 2 игроку")
                    gamebafdebuf2["debaf2"] = "Остановка времени"
                    time_stop2 = True
                    spos -= 100
                    continue
                elif games == "Дмитрия Теневеда":
                    print(f"Вы слились с тьмой и вероятность по вам попасть 40%")
                    gamebafdebuf["baf"] = "Плащ тьмы"
                    spos -= 100
                    continue
            else:
                print(f"Ваша способность не готова {spos}")
        else:
            print(f"Такого хода нету")
            continue
        
        
    print(f"Ход первого игрока")
    if not time_stop:
        action = input("Выберите ход написав цифру: \n1)Атака \n2)Способность \n")
        
        if action == "1":
            if "Доспех огня" in gamebafdebuf2.values():
                xp_players -= 5
                xp_players2 -= 5
                spos += 10
            elif "Плащ тьмы" in gamebafdebuf2.values():
                print("плащьт есть")
                chance = 0.4 # Шанс выпадения
                if random.random() < chance:    
                    print(f"Вы нанесли урон")
                    xp_players -= 15
                    spos += 15
                else:
                    print(f"Вы промахнулись")
                    spos += 10
            
            elif "Доспех огня" not in gamebafdebuf2.values():
                xp_players -= 10
                spos += 15
            

        elif action == "2":
            if spos >= 100:
                spos = 100
            if spos == 100:
                if games == "Василису Огненкая":
                    print(f"Вы наложили на себя огненый доспех")
                    gamebafdebuf2["baf"] = "Доспех огня"
                    spos -= 100
                    continue
                elif games == "Алису Мгновенную":
                    print(f"Вы остановили время 2 игроку")
                    gamebafdebuf["debaf2"] = "Остановка времени"
                    time_stop2 = True
                    spos -= 100
                    continue
                elif games == "Дмитрия Теневеда":
                    print(f"Вы слились с тьмой и вероятность по вам попасть 40%")
                    gamebafdebuf2["baf"] = "Плащ тьмы"
                    spos -= 100
                    continue
            else:
                print(f"Ваша способность не готова {spos}")
        else:
            print(f"Такого хода нету")
            continue
        
    
        
    print (f"Жизни игроков {xp_players},{xp_players2}") 
    print (gamebafdebuf)
    print(gamebafdebuf2)
        
        
    if xp_players <= 0:
        print(f"Выиграл второй игрок")
        break
    elif xp_players2 <= 0:
        print(f"Выиграл первый игрок")
        break
        
    