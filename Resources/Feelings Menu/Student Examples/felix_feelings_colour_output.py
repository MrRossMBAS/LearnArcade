class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


print()
print(color.RED + "============================" + color.END)
print(color.RED + "=                          =" + color.END)
print(color.BOLD +"      Quote Generator       " + color.END)
print(color.RED + "=                          =" + color.END)
print(color.RED + "============================" + color.END)
print()
name = input(color.BOLD + "What is your name?" + color.END)
print(color.RED + "========================================" + color.END)
print((color.BLUE + 'Welcome,' + color.END),color.GREEN + name + color.END,color.BLUE + ', to the quote generator!' + color.END)
print(color.RED + "========================================" + color.END)
print()


run_feelings = True
while run_feelings:

    print(color.BLUE + "What would you like a quote for?" + color.END)
    print(color.RED + "-------------------------------------" + color.END)
    print(color.BOLD + "1. Inspiration" + color.END)
    print(color.RED + "-------------------------------------" + color.END)
    print(color.BOLD + "2. Friendship" + color.END)
    print(color.RED + "-------------------------------------" + color.END)
    print(color.BOLD + "3. Philosophy" + color.END)
    print(color.RED + "-------------------------------------" + color.END)
    print(color.BOLD + "4. Happiness" + color.END)
    print(color.RED + "-------------------------------------" + color.END)
    print(color.BOLD + "Q. I'd like to quit" + color.END)
    print(color.RED + "-------------------------------------" + color.END)
    print()

    print(color.BLUE + "Input Choice" + color.END)
    print(color.RED + "-------------------------------------" + color.END)
    choice = input(color.BOLD + "(1), (2), (3), (4), (Q): " + color.END)
    print(color.RED + "-------------------------------------" + color.END)


    if choice == "1":
        print()
        print(color.YELLOW + '"Have you realized that today is the tomorrow you talked about yesterday? It is your responsibility to change your life for the better."' + color.END)
        print()
        print(color.BLUE + "Jaachynyma N.E Agu" + color.END)
        print()
        run_feelings = False
    elif choice == "2":
            print()
            print(color.YELLOW + '"The friends you make in college are friends you will have for life, even if you don not talk for years at a time."' + color.END)
            print()
            print(color.BLUE + "Jessica Park" + color.END)
            print()
            run_feelings = False
    elif choice == "3":
            print()
            print(color.YELLOW + '"Like all magnificent things, it is very simple."' + color.END)
            print()
            print(color.BLUE + "Natalie Babbitt" + color.END)
            print()
            run_feelings = False
    elif choice == "4":
            print()
            print(color.YELLOW + '"Nothing says, "I love you!" more than those three words."' + color.END)
            print()
            print(color.BLUE + "Anthony T.Hincks" + color.END)
            print()
            run_feelings = False

    elif choice == "Q":
        print("OK, it was fun while it lasted.")

        # Stop the loop
        run_feelings = False
    else:
        print("I don't understand. Please try again")
print('Would you like another quote?')
again = input('Enter (Yes) or (No):')
if again == "Yes":
    run_feelings = True
elif again == "No":
    print("Bye!")