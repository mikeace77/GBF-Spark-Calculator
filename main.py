from choices import Choices

print('''Welcome to GBF Spark Calculator by Mikey.
This is a simple project made from python.''')

user_choices = Choices()

while True:
    try:
        user_input  = int(input("1. Save your xtall\n2. Save your 1x tickets\n3. Save your 10x tickets\n4. Check your pulls\n5. Reset\n6. Gacha simulator\n7. Toggle gala\n8. Quit\nYour choice?: "))

        match user_input:

            case 1:
                user_choices.xtall()
            case 2:
                user_choices.one_tickets()
            case 3:
                user_choices.ten_tickets()
            case 4:
                user_choices.report()
            case 5:
                user_choices.reset()
            case 6:
                user_choices.gacha()
            case 7:
                user_choices.toggle_gala()
            case _:
                print("\n"*100)
                print("Goodbye!")
                break

    except NameError and ValueError:
        print("Please input the number!")
