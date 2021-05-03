import random

ESCAPE_DISTANCE = 200


def print_blank_lines(number_of_lines=4):
    # Print out some white space.
    for i in range(number_of_lines):
        print("")


def calculate_pirate_movement():
    # The distance the pirates row in a turn is between these numbers.
    PIRATE_MINIMUM = 7
    PIRATE_MAXIMUM = 14

    # Calculate how far the pirates move this turn.
    pirate_distance_change = random.randint(PIRATE_MINIMUM, PIRATE_MAXIMUM)
    print("The pirates rowing furiously, move forward", pirate_distance_change, "miles")

    return pirate_distance_change


def update_pirate_distance(pirate_distance):
    pirate_distance = pirate_distance + calculate_pirate_movement()

    return pirate_distance


def calculate_full_speed_movement():
    # Calculate how far you row when going flat out.
    # The distance you move at full speed is between these numbers.
    FULL_SPEED_MINIMUM = 10
    FULL_SPEED_MAXIMUM = 20

    # Calculate how far the pirates move this turn.
    rowing_distance_change = random.randint(FULL_SPEED_MINIMUM, FULL_SPEED_MAXIMUM)

    print("You manage to row", rowing_distance_change, "miles.")
    return rowing_distance_change


def calculate_moderate_movement():
    # Calculate how far you row when going flat out.
    # The distance you move at full speed is between these numbers.
    MODERATE_MINIMUM = 5
    MODERATE_MAXIMUM = 12

    # Calculate how far the pirates move this turn.
    rowing_distance_change = random.randint(MODERATE_MINIMUM, MODERATE_MAXIMUM)

    print("You manage to row", rowing_distance_change, "miles.")
    return rowing_distance_change


def print_thirst(thirst):
    if thirst == 0:
        print("You are not thirsty.")
    elif thirst == 6:
        print("You are about to die of thirst!")
    elif thirst == 5:
        print("You are close to dieing of thirst!")
    elif thirst == 4:
        print("You are extremely thirsty.")
    else:  # thirst in [1, 2, 3]:
        print("You are thirsty, but you are coping well.")


def game_over():
    print_blank_lines()
    print("+========================================================+")
    print("|                       GAME OVER!                       |")
    print("+========================================================+")
    print("Thanks for playing Pirates!")


def main():
    # Setup the variables
    miles_rowed = 0
    thirst = 0
    shoulder_tiredness = 0

    pirate_distance = -20

    drinks_in_bottle = 3

    print("+========================================================+")
    print("|                Welcome to Pirates!                     |")
    print("+========================================================+")
    print("")
    print("You have stolen a long boat from the pirates!  Ohhh Arggghh")
    print("The pirates want their boat back and want to make you walk the plank!")
    print("Survive by rowing across the ocean and out run the pirates. Ohhh Arggggh")

    done = False
    while not done:
        print_blank_lines()
        # Give out instructions.
        print("You are in your boat. What do you do next?")
        print("")
        print("A. Drink from your water bottle.")
        print("B. Row at moderate speed.")
        print("C. Row as fast as you can.")
        print("D. Stop for a rest.")
        print("E. Check the boat.")
        print("Q. Drink the salt water and quit this game.")

        what_to_do = input("What do you do sailor? ")

        # All input will be upper case.
        what_to_do = what_to_do.upper()

        print_blank_lines()

        # The user wants to quit the game.
        if what_to_do == "Q":
            print("It's all too much for you. You are so thirsty you drink the salt water.")
            print("You start to have visions of a desert island with a palm tree.")
            print("Going mad, you slip over the side of the boat and start swimming towards")
            print("the plam tree island")
            print("Soon you get tired, slip below the water and dissapear forever.")
            game_over()

            done = True

        # Drink water
        elif what_to_do == "A":
            if drinks_in_bottle > 0:
                print("Feeling parched and thirsty you take a sip from your bottle.")
                print("A sip of cool liquid slides down your raw throat. You resist the urge")
                print("to drain the rest of the bottle and return to rowing.")
                drinks_in_bottle = drinks_in_bottle - 1
                thirst = 0
            else:
                print("Feeling parched and thirsty you uncork your bottle and riase it to your lips.")
                print("Nothing comes out! The water bottle is empty!")



        # Row at a moderate speed
        elif what_to_do == "B":
            print("Calmly you decide to row for a bit.")
            print("The oars cut the water and your shoulders flex and pull like a well oiled machine.")

            miles_rowed = miles_rowed + calculate_moderate_movement()
            thirst = thirst + 1
            shoulder_tiredness = shoulder_tiredness + 1

            # Calculate how far the pirates move this turn.
            pirate_distance = update_pirate_distance(pirate_distance)


        # Row at full speed
        elif what_to_do == "C":
            print("Filled with panic at the thought of what the pirates will do to you")
            print("if they catch you, you row as fast as you can for a spell.")
            print("The oars cut the water and your shoulders flex and pull like a well oiled machine.")

            miles_rowed = miles_rowed + calculate_full_speed_movement()
            thirst = thirst + 1
            shoulder_tiredness = shoulder_tiredness + random.randint(1, 3)

            # Calculate how far the pirates move this turn.
            pirate_distance = update_pirate_distance(pirate_distance)


        # Stop for a rest.
        elif what_to_do == "D":
            print("Your shoulders thank you for the rest.")
            shoulder_tiredness = 0

            # Calculate how far the pirates move this turn.
            pirate_distance = update_pirate_distance(pirate_distance)


        # The user wants to check the boat.
        elif what_to_do == "E":
            print("You check the boat, roll your shoulders to see how tired they are")
            print("and look behind you for the pirates.")
            print("")
            print("The boat has developed no leaks and is in good condition.")
            print("You have rowed", miles_rowed, "and still have",
                  ESCAPE_DISTANCE - miles_rowed, "miles to go to the safety of the fort!")
            print_thirst(thirst)

            print("Your shoulders are", shoulder_tiredness, "from rowing.")
            print("There are", drinks_in_bottle, "sips left in your water bottle.")
            print("The pirates are", miles_rowed - pirate_distance, "behind you.")

        print_blank_lines()

        # The things that can end the game.
        if pirate_distance > miles_rowed:
            print("The pirates row up behind you, they throw a grappling hook")
            print("which embeds itself into your thight. Screaming in pain they")
            print("Haul you out of your boat, across to them and into your boat.")
            print("They chop off a foot and a hand so you cannot escape again and")
            print("row you back to the pirate stronghold to hop the plank!")
            game_over()
            done = True
        elif thirst > 6:
            print("You died of thirst!")
            game_over()
            done = True
        elif shoulder_tiredness > 8:
            print("Too tired to row any further, you collapse unconsoius in your boat.")
            game_over()
            done = True
        elif miles_rowed > ESCAPE_DISTANCE:
            print("You made it!")
            done = True
        elif thirst > 4:
            print("You are very thirsty.")
        elif shoulder_tiredness > 5:
            print("Your shoulders are getting tired. You don't feel like you can go on much longer.")
        else:
            print("The ocean is still and flat and the moon shines on the water.")


if __name__ == "__main__":
    main()
