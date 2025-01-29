def rock_paper_scissor():

    import random
    bot=['rock','paper','scissor']

    while(True):
        user_input=input("Enter any one from ['rock','paper','scissor'] : ")
        bot_input=random.choice(bot)
        print()
        print("Your input :",user_input)
        print("Bot input :",bot_input)
        print()
        if (bot_input=='rock' and user_input=='scissor') or (bot_input=='scissor' and user_input=='paper') or (bot_input=='paper' and user_input=='rock'):
            print("Bot has won the game!")
        elif (bot_input==user_input):
            print("Match Draw..")
        elif (user_input not in bot):
            print("Enter a valid input <>")
        else:
            print("You have won the game!.. ")

        