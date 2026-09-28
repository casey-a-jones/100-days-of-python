# AUTHOR: Casey Jones
# CREATED: 9/27/2026
# PROJECT: Udemy - 100 Days of Python - Day 003 - Train Game

# New things I learned:
# .lower() Add at the end of an input line.
# if, elif, else
# <, >, ==, !=, <=, >=
# +=
# ascii text on multiple lines using (''' ''')
# shorthand example if 45 <= age <= 55:


print('''
***************************
*         (               *
*     '( '                *
*    "'  //}              *
*   ( ''"                 *
*   _||__ ____ ____ ____  *
*  (o)___)}___}}___}}___} *
*  'U'0 0  0 0  0 0  0 0  *
***************************
''')

print("||-- Welcome to the Train Game --||")
print("||-- Where your choices matter --||\n")

age = int(input("Please enter your age: "))
if age >= 18:
    start = int(input("\nTo start the game, press 1: "))
    if start == 1:
        car = int(input("\nA train arrives and you have a choice of 3 cars to enter. Choose 1, 2, or 3: "))
        if car == 1:
            print("\nYou step on to car 1. A crazed maniac lunges at you...\n")
            print("cxxx|;:;:;:;:;:;:;:;>\n")
            print("You died\n")
            print("|-- Game Over --|")
        elif car == 2:
            print("\nYou step on to car 2. A scary creature appears...\n")
            print("┌∩┐(◣_◢)┌∩┐\n")
            print("You died\n")
            print("|-- Game Over --|")
        elif car == 3:
            print("\nYou step on to car 3. A friendly person greets you aboard.\n")
            print("@('_')@\n")
            print("You enjoy a nice and relaxing train ride to your destination.\n")
            print("You lived\n")
            print("|-- Game Over --|")
        else:
            print("\nPerhaps not getting on the train was the the safest choice of all.\n")
            print("You lived\n")
            print("|-- Game Over --|")
    else:
        print("\nYou chose not to play.\n")
        print("|-- Game Over --|")
else:
    print("\nYou must be 18 or older to play this game.")