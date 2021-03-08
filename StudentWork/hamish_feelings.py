import random

feelings = [[
            "Trust yourself. You’ve survived a lot, and you’ll survive whatever is coming.\n\n– Robert Tew",
            "Inner peace begins the moment you choose not to allow another person or event to control your emotions.\n\n— Pema Chodron",
            "Smile, breathe, and go slowly.\n\n- Thich Nhat Hanh ",
            "Nothing diminishes anxiety faster than action.\n\n— Walter Anderson",
            "Life is ten percent what you experience and ninety percent how you respond to it.\n\n — Dorothy M. Neddermeyer",
            "You don’t have to control your thoughts. You just have to stop letting them control you.\n\n— Dan Millman",
            "Good humor is a tonic for mind and body. It is the best antidote for anxiety and depression. It is a business asset. It attracts and keeps friends. It lightens human burdens. It is the direct route to serenity and contentment.\n\n— Grenville Kleiser",
            "Do not anticipate trouble, or worry about what may never happen. Keep in the sunlight.\n\n— Benjamin Franklin",
            "Nothing can bring you peace but yourself.\n\n— Ralph Waldo Emerson",
            "No amount of anxiety can change the future. No amount of regret can change the past.\n\n– Karen Salmansohn",
            "No longer forward nor behind I look in hope and fear; But grateful take the good I find, The best of now and here.\n\n— John G. Whittier",
            "Anxiety is a thin stream of fear trickling through the mind. If encouraged, it cuts a channel into which all other thoughts are drained.\n\n— Arthur Somers Roche",
            "Physical comforts cannot subdue mental suffering, and if we look closely, we can see that those who have many possessions are not necessarily happy. In fact, being wealthy often brings even more anxiety.\n\n— Dalai Lama",
            "If you want to conquer the anxiety of life, live in the moment, live in the breath.\n\n— Amit Ray",
            "Don’t let your mind bully your body into believing it must carry the burden of its worries.\n\n — Astrid Alauda",
            "Who’s not sat tense before his own heart’s curtain.\n\n— Rainer Maria Rilke",
            "Never let life’s hardships disturb you … no one can avoid problems, not even saints or sages.\n\n— Nichiren Daishonen",
            "I promise you nothing is as chaotic as it seems. Nothing is worth your health. Nothing is worth poisoning yourself into stress, anxiety, and fear.\n\n— Steve Maraboli",
            "Nothing is permanent in this wicked world — not even our troubles.\n\n— Charlie Chaplin",
            "The greatest weapon against stress is our ability to choose one thought over another.\n\n— William James",
            "We must be willing to let go of the life we’ve planned, so as to have the life that is waiting for us.\n\n— Joseph Campbell"],

        [
            "Ah, what happiness it is to be with people who are all happy, to press hands, press cheeks, smile into eyes.”\n\n― Katherine Mansfield",
            "Happy people can look back and say they chose their life, not settled for it.”\n\n― Shannon L. Alder",
            "Life’s good when it’s lived for oneself; it’s great when lived for others. The true means of happiness is to lose your mind by thinking for others!”\n\n― Israelmore Ayivor",
            "“Happy people are those who use a lower threshold in order to label an event positive.”\n\n― David Niven",
            "“I love happy people; they’re like smile magnets.”\n\n― Richelle E. Goodrich",
            "“You can’t afford to limit your joy. It has been proven several times that angry people are never happy people.”\n\n― Israelmore Ayivor,"],

        [
            "“Hardships often prepare ordinary people for an extraordinary destiny.”\n\n – C.S. Lewis",
            "“I am thankful for my struggle because without it I wouldn’t have come across my strength.”\n\n – Alex Elle",
            "“Never be ashamed of a scar. It means you were stronger than whatever tried to hurt you.”\n\n – Unknown",
            "“Once you choose hope, anything is possible.”\n\n – Christopher Reeve",
            "“Until you’re broken you don’t know what you’re made of. It gives you the ability to build yourself all over again, but stronger than ever…”\n\n – Melissa Molomo"],

        [
            "“I can be most colorful and inventive.”\n\n – Christopher Moore",
            "“You can get angry, you can get even, or you can get ahead.”\n\n – Jeffrey Fry",
            "“There is no time to be angry, always be busy with love.”\n\n – Debasish Mridha",
            "“Your smile can heal thousands; but your anger can kill millions. Your ‘hand-shake’ can encourage tens of people while your ‘finger-pointing’ can turn ten thousands away from you!”\n\n – Israelmore Ayivor",
            "“An angry man rarely stops to let facts get in the way of his fury.”\n\n – Nikki Sex"]]

play_again = True
alphabet = ['a','b','c','d']
while play_again == True:
    choice = "invalid"
    while choice != "valid":
        try:
            feeling_choice = input("How are you feeling?\nA) Anxious\nB) Happy\nC) Sad\nD) Angry\n").lower()
            alphabet.index(feeling_choice)
            choice = "valid"
        except:
            print("Please enter a letter corresponding to a feeling.")
    print(feelings[alphabet.index(feeling_choice)][random.randint(0,len(feelings[alphabet.index(feeling_choice)])-1)])

    if input("Would you like to feel more?\n").lower() == "no":
        play_again = False