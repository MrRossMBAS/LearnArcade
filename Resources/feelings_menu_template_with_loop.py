# This is the feelings menu exemplar.
#
# https://drive.google.com/drive/folders/1tD1FfW9UpQc-_9hjIiFpSaZiscEaCtbv
#

# Output a welcome message.

print()
print("############################")
print("#                          #")
print("# QUOTES FOR YOUR FEELINGS #")
print("#                          #")
print("############################")
print()
print("Welcome. You tell me how you are feeling and I will give you a quote.")
print()

# We set this to True. As long as it is true we run the next loop.
# To stop the loop we just set this to False.
run_feelings = True

# Starting the loop.
while run_feelings:
# We could also use while run_feelings == True. while run_feelings is shorter!

    print("You can choose from the following list of feelings. Which one best matches your mood right now?")
    print()
    # Output a feeling
    print("A: I feel really happy.")
    print("B: I feel really sad.")
    print("C: I feel a bit worried.")
    print("D: I feel excited.")
    print("Q: To quit.")
    print()

    # Output instructions
    print("Enter the letter that corresponds the most closely to how you feel.")

    # Creates a variable called feeling that stores the users input.
    # Notice the space. It's important.
    feeling = input("Choose a feeling from the options (A, B, C, D) or Q to quit: ")

    # Process the user input.
    if feeling == "A":
        print()
        print("You can destroy your now, by worrying about tomorrow.")
        print()
        print("Janis Joplin")
        print()
        if feeling == "A":
            # This is for worry
            print()
            print("You can destroy your now, by worrying about tomorrow.")
            print()
            print("Janis Joplin")
            print()
    elif feeling == "Q":
        print("OK, it was fun while it lasted.")

        # Stop the loop
        run_feelings = False
    else:
        print("I don't understand.")