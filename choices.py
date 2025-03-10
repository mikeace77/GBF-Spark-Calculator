import random as rd

class Choices:
    
    def __init__(self):
        self.crystal = 0
        self.one_tix = 0
        self.ten_tix = 0
        self.accumulate = 0
        self.r = 0
        self.sr = 0
        self.ssr = 0
        self.gala = False
        self.odds = [0.82, 0.15, 0.03]
        self.rarity = ["R", "SR", "SSR"]
    
    def xtall(self):
        try:
            user_input = int(input("How much crystal you have?: "))
        except ValueError:
            print("Please input a number!")

        match [user_input < 0]:
            case [True]:
                print("\n"*100)
                print("Do not use negative numbers!")
            case _:
                self.crystal += user_input
                print("\n"*100)

    def one_tickets(self):
        try:
            user_input = int(input("How much tickets you have?: "))
        except ValueError:
            print("Please input a number!")
        
        match [user_input < 0]:
            case [True]:
                print("\n"*100)
                print("Do not use negative numbers!")
            case _:
                self.one_tix += user_input
                print("\n"*100)

    def ten_tickets(self):
        try:
            user_input = int(input("How much tickets you have?: "))
        except ValueError:
            print("Please input a number!")

        match [user_input < 0]:
            case [True]:
                print("\n"*100)
                print("Do not use negative numbers!")
            case _:
                self.ten_tix += user_input
                print("\n"*100)

    def report(self):
        total_pulls_xtall = round(self.crystal/300)
        total_pulls_ten_tix = round(self.ten_tix*10)
        total_all = round(total_pulls_xtall + total_pulls_ten_tix + self.one_tix)
        print("\n"*100)
        print(
            f"Your current crystal: {self.crystal} crystal\n"
            f"Your 1x tickets: {self.one_tix} tickets\n"
            f"Your 10x tickets: {self.ten_tix} tickets\n"
            f"Total pulls: {total_all}"
        )
        match [total_all<300, total_all>=300]:
            case [True, False]:
                print(f"You can't spark, you need {300-total_all} pulls more\n")
            case [False, True]:
                print(f"You can do {round(total_all/300)}x spark\n")

    def reset(self):
        self.crystal = 0
        self.one_tix = 0
        self.ten_tix = 0
    
    def toggle_gala(self):
        choosing = True
        while choosing:
            toggle = input("Do you want gala rate?(y/n): ").lower()
            match toggle:
                case 'y':
                    self.gala = True
                    self.odds = [0.805, 0.135, 0.06]
                    print("Gala is turned on")
                    choosing = False
                case 'n':
                    self.gala = False
                    self.odds = [0.82, 0.15, 0.03]
                    print("Gala is turned off")
                    choosing = False
                case _:
                    print("Please choose y/n only!")
                    continue
    def draw_ten(self):
        for i in range(10):
            self.crystal
            result = rd.choices(self.rarity, weights=self.odds, k=1)
            if self.rarity[0] in result:
                self.r +=1
            elif self.rarity[1] in result:
                self.sr +=1
            else:
                self.ssr += 1
            print(''.join(result),"",end="")
        print("\n")
        print(f"Total R: {self.r}, SR: {self.sr}, SSR: {self.ssr}")
    
    def draw_one(self):
        for i in range(1):
            self.crystal
            result = rd.choices(self.rarity, weights=self.odds, k=1)
            if self.rarity[0] in result:
                self.r +=1
            elif self.rarity[1] in result:
                self.sr +=1
            else:
                self.ssr += 1
            print(''.join(result),"",end="")
        print("\n")
        print(f"Total R: {self.r}, SR: {self.sr}, SSR: {self.ssr}")  

    def gacha(self):
        check_for_one_tix = self.one_tix * 300
        check_for_ten_tix = self.ten_tix * 3000
        print("\n"*100)
        print("Please choose how many draws you want!")

        ''' THIS GACHA METHOD IS USING YOUR TICKETS INSTEAD OF CONVERTING CRYSTAL TO TICKETS'''
        
        do_gacha = True
        while do_gacha:
            try:
                user_input = int(input("1. 10 Draw\n2. 1 Draw\n3. Exit\nYour choice?: "))
                match user_input:
                    case 3:
                        break
                gacha_input = int(input("1. Use crystal\n2. Use 1 tickets\n3. Use 10 tickets\nYour choice?: "))
            except ValueError and UnboundLocalError:
                print("Please input a number!")
                do_gacha = True

            match (user_input, gacha_input):
                case (1, 1):
                    match self.crystal < 3000:
                        case True:
                            print("Sorry, not enough crystal")
                        case _:
                            self.crystal -= 3000
                            Choices.draw_ten(self)
                case (1, 2):
                    match check_for_one_tix < 3000:
                        case True:
                            print("Sorry, not enough tickets")
                        case _:
                            self.one_tix -= 10
                            Choices.draw_ten(self)
                case (1, 3):
                    match check_for_ten_tix < 3000:
                        case True:
                            print("Sorry, not enough tickets")
                        case _:
                            self.ten_tix -= 1
                            Choices.draw_ten(self)
                case (2, 1):
                    match self.crystal < 300:
                        case True:
                            print("Sorry, not enough crystal")
                        case _:
                            self.crystal -= 300
                            Choices.draw_one(self)
                case (2, 2):
                    match check_for_one_tix < 300:
                        case True:
                            print("Sorry, not enough tickets")
                        case _:
                            self.one_tix -= 1
                            Choices.draw_one(self)
                case _:
                    break
                
            '''THIS METHOD BELOW IS USED IF YOU WANTED ALL TICKETS IS CONVERTED TO CRYSTAL'''            
            # self.one_tix *= 300
            # self.ten_tix *= 3000
            # all_curr = round(self.one_tix + self.ten_tix)
            # self.crystal += all_curr
            # print("All tickets are now converted to crystals")
            # self.one_tix = 0
            # self.ten_tix = 0
            # match user_input:
            #     case 1:
            #         match [self.crystal < 3000]:
            #             case [True]:
            #                 print("Sorry, not enough crystal")
            #             case _:
            #                 self.crystal -= 3000
            #                 for i in range(10):
            #                     result = rd.choices(rarity, weights=self.odds, k=1)
            #                     if rarity[0] in result:
            #                         self.r +=1
            #                     elif rarity[1] in result:
            #                         self.sr +=1
            #                     else:
            #                         self.ssr += 1
            #                     print(''.join(result),"",end="")
            #                 print("\n")
            #                 print(f"Total R: {self.r}, SR: {self.sr}, SSR: {self.ssr}")
            #     case 2:
            #         match [self.crystal < 300]:
            #             case [True]:
            #                 print("Sorry, not enough crystal")
            #             case _:
            #                 self.crystal -= 300
            #                 for i in range(1):
            #                     result = rd.choices(rarity, weights=self.odds, k=1)
            #                     if rarity[0] in result:
            #                         self.r +=1
            #                     elif rarity[1] in result:
            #                         self.sr +=1
            #                     else:
            #                         self.ssr += 1
            #                     print(''.join(result),"",end="")
            #                 print("\n")
            #                 print(f"Total R: {self.r}, SR: {self.sr}, SSR: {self.ssr}")
            #     case _:
            #         break
