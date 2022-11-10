# to start timing for every print.
import time
# to make the program choose randomly from the list below.
import random

random_list = ["Maus", "IS3", "OBJ430", "Tiger2"]
random_tank = random.choice(random_list)


# mixing the timing and print together.
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


# giving information for the player to know the game.
def intro():
    print_pause("Hello! I am BioBot.")

    print_pause("I'm going to be your assistant in this game.")

    print_pause("You will have to know somethings about this game.")

    print_pause("This game is about tanks battles.")

    print_pause("You will have 2 tanks to choose from.")

    print_pause("And your mission is to destroy an amount of tanks.")

    print_pause("Let's start, shall we.")


# giving the player 2 tanks to choose from.
def choosing():
    while True:
        response = input("Which one would you choose, "
                         "T62a or M1Abrams?\n").lower()

        if response == "t62a":
            print_pause("Good choice")
            break

        elif response == "m1abrams":
            print_pause("Great choice")
            break

        # if he entered something wrong it is going to tell him about it.
        else:
            print_pause("Sorry, We don't have this tank in our garage.")

    print("Your tank will be here soon.")
    time.sleep(4)


# letting the player know about what happened when he chose his tank.
def begin():
    print_pause("Great, You now have the tank let's start our mission.")

    print_pause("Now, you have been deployed with other tankers like you.")

    print_pause("All of you have the same mission "
                "to finish it you have to work together.")

    print_pause("An artillery tanker said he will cover you from the base.")

    print_pause("And another tanker that uses IS7 said "
                "that he is going to help you.")

    print_pause("You and IS7 went to fight and the artillery is covering you.")

    print_pause("you have spotted " + str(random_tank))


# putting the player in situation to make him think.
def thinking():
    while True:
        response = input("Would you like to fight with the other tanker?"
                         "please enter  'Yes' or 'No'\n").lower()

        if response == "yes":
            print_pause("Great, you have destroyed the enemy tank.")
            break

        elif response == "no":
            print_pause("You ran away and left the other tanker alone "
                        "then he died then the whole team lost. "
                        "SHAME ON YOU!!!!")
            play_again()

        else:
            print_pause("This choice isn't available.")


# if the player chose a choice that made him lose.
# he can play again because of this code.
def play_again():
    while True:
        response = input("Would you like to play again?"
                         "please enter  'Yes' or 'No'\n").lower()

        # this is the start of the loop.
        if response == "yes":
            print_pause("Great, let's start again.")
            intro()
            choosing()
            begin()
            thinking()
            last_enemy_tank()
            last_fight()

        elif response == "no":
            print_pause("Ok, Thanks for playing.")
            quit()

        else:
            print_pause("This choice isn't available.")


# telling him what happened next.
def last_enemy_tank():
    print_pause("Great, Now all you have to do is to find the last tank "
                "to destroy it.")

    print_pause("You are right now moving on the field "
                "to spot the last tank for your team.")

    print_pause("But, it didn't last long and you have found the last tank.")

    print_pause("And it was IS3")


# another choice so the player can make.
def last_fight():
    while True:
        response = input("Would you like to fight the last tank?"
                         "please enter  'Yes' or 'No'\n").lower()

        if response == "yes":
            print_pause("Great, you have destroyed the last enemy tank "
                        "and you got the kill.")
            play_again()

        elif response == "no":
            print_pause("You ran away and left the tank for your team"
                        "you have played well in this match by the way.")
            play_again()

        else:
            print_pause("This choice isn't available.")


# these are shortcuts for everything above and they make the codes work.
intro()
choosing()
begin()
thinking()
last_enemy_tank()
last_fight()
