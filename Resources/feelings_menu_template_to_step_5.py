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

# Output a feeling
print("A: I Feel a bit worried.")

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