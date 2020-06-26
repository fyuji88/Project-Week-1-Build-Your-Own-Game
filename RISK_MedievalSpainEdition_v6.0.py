#!/usr/bin/env python
# coding: utf-8

# In[27]:


#Assigning initial players names

player1= input("Player 1 Whats your name?")
player2= input("Player 2 Whats your name?")
player3= input("Player 3 Whats your name?")

scoreboard = {player1:0, player2:0, player3:0}


# In[28]:


def playgame():

    active_player = 1

    from random import choice
    import time

    Spanish_Territories = ["Catalonia", "Castille", "Galicia_Leon"]


    territories_player1 = []
    territories_player2 = []
    territories_player3 = []


    initial_territory1 = choice(Spanish_Territories)
    territories_player1.append(initial_territory1)
    Spanish_Territories.remove(initial_territory1)

    initial_territory2 = choice(Spanish_Territories)
    territories_player2.append(initial_territory2)
    Spanish_Territories.remove(initial_territory2)


    initial_territory3= choice(Spanish_Territories)
    territories_player3.append(initial_territory3)
    Spanish_Territories.remove(initial_territory3)

    Allegiance = {"Catalonia":0, "Castille": 0, "Galicia_Leon":0 }


    for i in territories_player1:
        Allegiance[i]=player1
    for i in territories_player2:
        Allegiance[i]=player2
    for i in territories_player3:
        Allegiance[i]=player3
        
    army_balance = {player1:1, player2:2, player3:10}
        
    print(player1 + " starts with the kingdom of " + initial_territory1 + " and " + str(army_balance[player1]) + " soldiers.")
    print(player2 + " starts with the kingdom of " + initial_territory2 + " and " + str(army_balance[player2]) + " soldiers.")
    print(player3 + " starts with the kingdom of " + initial_territory3 + " and " + str(army_balance[player3]) + " soldiers.")


    players_alive = set()    
    for k, v in army_balance.items():
        if v != 0:
            players_alive.add(k)

    result = []
    
    
    def attacking_army(attacker):
        min_attack = 1
    
        if army_balance[attacker] -1 < 3:
            max_attack = army_balance[attacker] -1
        else:
            max_attack = 3
        
    
        rolls_attack = input(str(attacker) + ' how many soldiers are you attacking with:')
        while rolls_attack.isnumeric() == False:
            rolls_attack = input(str(attacker) + ' please deploy a NUMBER of soldiers! NOT A STRING, NO MATTER HOW ELOQUENT YOU ARE:')
        while int(rolls_attack) > max_attack or int(rolls_attack) < min_attack:
            rolls_attack = input(str(attacker) + ' Please deploy an army between:' + str(min_attack) + " and "  + str(max_attack) + " Soldiers")
            while rolls_attack.isnumeric() == False:
                rolls_attack = input(str(attacker) + ' please deploy a NUMBER of soldiers! NOT A STRING, NO MATTER HOW ELOQUENT YOU ARE:')

        return int(rolls_attack)

    def defending_army(defender):
        min_defense = 1
        if army_balance[defender] < 3:
            max_defense = army_balance[defender]
        else:
            max_defense = 3

        rolls_defense = input(str(defender) + ' how many soldiers are you defending with:')
        while rolls_defense.isnumeric() == False:
            rolls_defense = input(str(defender) + ' please deploy a NUMBER of soldiers! NOT A STRING, NO MATTER HOW ELOQUENT YOU ARE:')
        while int(rolls_defense) > max_defense or int(rolls_defense) < min_defense:
            rolls_defense = input(str(defender) + ' Please deploy an army between:' + str(min_defense) + " and "  + str(max_defense) + " Soldiers")   
            while rolls_defense.isnumeric() == False:
                rolls_defense = input(str(defender) + ' please deploy a NUMBER of soldiers! NOT A STRING, NO MATTER HOW ELOQUENT YOU ARE:')


        return int(rolls_defense)
    
        #Combat Dynamics(Dice Rolls)

    import random
    r = random.randint
    min = 1
    max = 6

    #lists are created to store dice rolls
    attacker_dice = []
    defender_dice = []

    #players choose how many soldiers to deploy, and dice are rolled

    def dice_rolls(attacker,defender):
        attacker_dice = []
        defender_dice = []


        rolls_attack = attacking_army(attacker)

        for x in range(rolls_attack):
            print ('you got a...')
            print("-----------------------------------------------------------")
            print(" ")
            time.sleep(.5)
            attacker_dice.append(r(min, max))
            print(attacker_dice[-1])


        rolls_defense = defending_army(defender)
        for x in range(rolls_defense):
            print ('you got a...')
            print("-----------------------------------------------------------")
            print(" ")
            time.sleep(.5)
            defender_dice.append(r(min, max))
            print(defender_dice[-1])

    #rolls are sorted descending

        attacker_dice.sort(reverse=True)
        defender_dice.sort(reverse=True)
        print(str(attacker) +  " Rolls: ")
        print(attacker_dice)
        print("-----------------------------------------------------------")
        print(" ")
        time.sleep(1)

        print(str(defender) +  " Rolls: ")
        print(defender_dice)
        print("-----------------------------------------------------------")
        print(" ")
        time.sleep(1)

    #both players rolls are paired.Rolls that can`t be paired are discarded by default by the Zip function.

        paired_dice = zip(attacker_dice, defender_dice)


    #each pair of rolls is compared and the wins of the combat are computed

        attacker_wins = 0
        defender_wins = 0
        for pair in paired_dice:
            att_roll, deff_roll = pair
            if att_roll > deff_roll:
                attacker_wins += 1
            else:
                defender_wins += 1

        print(str(attacker) + " won " + str(attacker_wins) + " times")
        print(str(defender) + " won " + str(defender_wins) + " times")
        return attacker_wins,defender, defender_wins
    
    
    
    #Function for target picking of Player1

    def p1_target():
        target=input("Choose a territory to attack or press enter to pass the turn")
        while True:
            if target in territories_player1:
                target=input("Can't attack own territory, please choose an enemy controlled territory, or press enter to pass")
            elif army_balance[player1]==1:
                print("-----------------------------------------------------------")
                print("You don't have enough Soldiers to attack, go back home and recruit")
                time.sleep(1)
                target= " "
                break

            else:
                break
        return target

    #Function for target picking of Player2

    def p2_target():
        target=input("Choose a territory to attack or press enter to pass the turn")
        while True:
            if target in territories_player2:
                target=input("Can't attack own territory, please choose an enemy controlled territory, or press enter to pass")
            elif army_balance[player2]==1:
                print("-----------------------------------------------------------")
                print("You don't have enough Soldiers to attack, go back home and recruit")
                time.sleep(1)
                target= " "
                break

            else:
                break
        return target

    #Function for target picking of Player1

    def p3_target():
        target=input("Choose a territory to attack or press enter to pass the turn")
        while True:
            if target in territories_player3:
                target=input("Can't attack own territory, please choose an enemy controlled territory, or press enter to pass")
            elif army_balance[player3]==1:
                print("-----------------------------------------------------------")
                print("You don't have enough Soldiers to attack, go back home and recruit")
                time.sleep(1)
                target= " "
                break

            else:
                break
        return target

    
    
    
    
    
    



    while len(players_alive) > 1:

    #PLAYER 1 TURN

        if active_player==1 and army_balance[player1]>0:

            print("-----------------------------------------------------------")
            print("------------------" + player1.upper() + " it`s your turn!" + "------------------")
            print("-----------------------------------------------------------")
            print(" ")
            time.sleep(2)


            print("-----------------------------------------------------------")
            print("The territories are Controlled by: " + str(Allegiance))
            print("-----------------------------------------------------------")
            print(" ")
            time.sleep(1)

            print("-----------------------------------------------------------")
            print("Current Army Balance: ")
            print(army_balance)
            print("-----------------------------------------------------------")
            print(" ")
            time.sleep(1)

            print("-------------------------------------------- "+ player1.upper() + " ATTACK PHASE--------------------------------------------")
            target =p1_target()

            if target in Allegiance.keys():
                result=dice_rolls(player1,Allegiance[target])
                army_balance[player1]-= result[2]
                army_balance[result[1]]-=result[0]


                print("--------------------------------------------ARMY BALANCE--------------------------------------------")
                print(army_balance)
                active_player=1

                if army_balance[result[1]]<1:
                    print(result[1].upper() + " WAS DEFEATED!!!!")
                    time.sleep(1)

                    Allegiance.pop(target)
                    Allegiance[target]=player1
                    territories_player1.append(target)

                    active_player==1
                    players_alive = set()    
                    for k, v in army_balance.items():
                        if v != 0:
                            players_alive.add(k)

            elif active_player==1 and army_balance[player1]<1:
                print(player1.upper() + " IS EXTINCT, passing turn to " + player2.upper())
                active_player=2

            else:
                print("-----------------------------------------------------------")
                print("You PASSED the turn and gained a soldiers for each territory controlled")
                time.sleep(1)
                print(str(len(territories_player1)) + " soldiers recruited from " + str(territories_player1))
                time.sleep(1)

                army_balance[player1]+=len(territories_player1)
                active_player=2




    #PLAYER 2 TURN

        if active_player==2 and army_balance[player2]>0:

            print(" ")
            print("-----------------------------------------------------------")
            print("------------------" + player2.upper() + " it`s your turn!" + "------------------")
            print("-----------------------------------------------------------")
            print(" ")
            time.sleep(2)


            print("-----------------------------------------------------------")
            print("The territories are Controlled by: " + str(Allegiance))
            print("-----------------------------------------------------------")
            print(" ")
            time.sleep(1)

            print("-----------------------------------------------------------")
            print("Current Army Balance: ")
            print(army_balance)
            print("-----------------------------------------------------------")
            print(" ")
            time.sleep(1)

            print("-------------------------------------------- "+ player2.upper() + " ATTACK PHASE--------------------------------------")
            target =p2_target()

            if target in Allegiance.keys():
                result=dice_rolls(player2,Allegiance[target])
                army_balance[player2]-= result[2]
                army_balance[result[1]]-=result[0]


                print("--------------------------------------------ARMY BALANCE--------------------------------------------")
                print(army_balance)
                active_player=2

                if army_balance[result[1]]<1:
                    print(result[1].upper() + " WAS DEFEATED!!!!")
                    time.sleep(1)

                    Allegiance.pop(target)
                    Allegiance[target]=player2
                    territories_player2.append(target)

                    active_player==2
                    players_alive = set()    
                    for k, v in army_balance.items():
                        if v != 0:
                            players_alive.add(k)


            else:
                print("-----------------------------------------------------------")
                print("You PASSED the turn and gained a soldiers for each territory controlled")
                time.sleep(1)
                print(str(len(territories_player2)) + " soldiers recruited from " + str(territories_player2))
                time.sleep(1)

                army_balance[player2]+=len(territories_player2)
                active_player=3

        elif active_player==2 and army_balance[player2]<1:
            print(player2.upper() + " IS EXTINCT, passing turn to " + player3.upper())
            active_player=3

    #PLAYER 3 TURN 


        if active_player==3 and army_balance[player3]>0:

            print(" ")
            print("-----------------------------------------------------------")
            print("------------------" + player3.upper() + " it`s your turn!" + "-----------------")
            print("-----------------------------------------------------------")
            print(" ")
            time.sleep(2)


            print("-----------------------------------------------------------")
            print("The territories are Controlled by: " + str(Allegiance))
            print("-----------------------------------------------------------")
            print(" ")
            time.sleep(1)

            print("-----------------------------------------------------------")
            print("Current Army Balance: ")
            print(army_balance)
            print("-----------------------------------------------------------")
            print(" ")
            time.sleep(1)

            print("-------------------------------------------- "+ player3.upper() + " ATTACK PHASE--------------------------------------------")
            target =p3_target()

            if target in Allegiance.keys():
                result=dice_rolls(player3,Allegiance[target])
                army_balance[player3]-= result[2]
                army_balance[result[1]]-=result[0]


                print("--------------------------------------------ARMY BALANCE--------------------------------------------")
                print(army_balance)
                active_player=3

                if army_balance[result[1]]<1:
                    print(result[1].upper() + " WAS DEFEATED!!!!")
                    time.sleep(1)

                    Allegiance.pop(target)
                    Allegiance[target]=player3
                    territories_player3.append(target)

                    active_player==2
                    players_alive = set()    
                    for k, v in army_balance.items():
                        if v != 0:
                            players_alive.add(k)

            else:
                print("-----------------------------------------------------------")
                print("You PASSED the turn and gained a soldiers for each territory controlled")
                time.sleep(1)
                print(str(len(territories_player3)) + " soldiers recruited from " + str(territories_player3))
                time.sleep(1)

                army_balance[player3]+=len(territories_player3)
                active_player=1

        elif active_player==3 and army_balance[player3]<1:
            print(player3.upper() + " IS EXTINCT, passing turn to " + player1.upper())
            active_player=1    


    print(players_alive)
    print("**WON THEGAME**")
    scoreboard[next(iter(players_alive))]+=1
    time.sleep(1)
    print("-----------------------------------------------------------")
    print("CURRENT SCOREBOARD:")
    time.sleep(1)
    print(scoreboard)
    time.sleep(1)
    playagain = input("Do you want to play again?(Y/N)")
    if playagain=="Y":
        playgame()
    else:
        print("BYE")
        time.sleep(3)
    


# In[ ]:


playgame()


# In[ ]:




