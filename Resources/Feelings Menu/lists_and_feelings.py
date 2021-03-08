import random

happy_quotes = ["""This is an inspirational quote""",
                """Thhis is another qutoe.""",
                """OK one more.""",
                """The last one.""",
                """OK, one more after all"""]
# print( len(happy_quotes ) )
the_quote_number = random.randint(0,len( happy_quotes ) - 1 )
print( happy_quotes[the_quote_number] )

answer =input("Give me some input: ")
if answer in ("a", "A", "Happy", "Indeiferrent"):
    print("It's a.a")