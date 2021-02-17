# This is the feelings menu template for the resources.
#
# https://drive.google.com/drive/folders/1tD1FfW9UpQc-_9hjIiFpSaZiscEaCtbv
#

# Output a welcome message.
print("Write a welcome message here.")
print("Add more of these to output more lines.")
print("You can make fancy boxes with characters.")
print()
print("#############")
print("#           #")
print("# Like this #")
print("#           #")
print("#############")

# We set this to True. As long as it is true we run the next loop.
# To stop the loop we just set this to False.
run_feelings = True

# Starting the loop.
while run_feelings:
# We could also use while run_feelings == True. while run_feelings is shorter!


    # Output a feeling
    print("A: I Feel a bit worried.")
    print("Q: To quit.")

    # Output instructions
    print("Enter the letter that corresponds the most closely to how you feel.")

    # Creates a variable called feeling that stores the users input.
    # Notice the space. It's important.
    feeling = input("Choose a feeling from the options (A): ")

    # Process the user input.
    if feeling == "A":
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