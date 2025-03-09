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
    
    def gacha(self):
        rarity = ["R", "SR", "SSR"]
        odds = [0.82, 0.15, 0.03]
        self.one_tix *= 300
        self.ten_tix *= 3000
        all_curr = round(self.one_tix + self.ten_tix)
        self.crystal += all_curr
        print("All tickets are now converted to crystals")
        print("\n"*100)
        self.one_tix = 0
        self.ten_tix = 0

        try:
            user_input = int(input("1. 10 Draw\n2. 1 Draw\nYour choice?: "))
        except ValueError:
            print("Please input a number!")
        
        choosing = True
        while choosing:
            is_gala = input("Do you want gala rate?(y/n): ").lower()
            print("\n")
            match is_gala:
                case 'y':
                    self.gala = True
                    odds = [0.82, 0.15, 0.06]
                    choosing = False
                case 'n':
                    self.gala = False
                    odds = [0.82, 0.15, 0.03]
                    choosing = False
                case _:
                    print("Please choose y/n only!")
                    continue
                    
        match user_input:
            case 1:
                match [self.crystal < 3000]:
                    case [True]:
                        print("Sorry, not enough crystal")
                    case _:
                        self.crystal -= 3000
                        for i in range(10):
                            result = rd.choices(rarity, weights=odds, k=1)
                            if rarity[0] in result:
                                self.r +=1
                            elif rarity[1] in result:
                                self.sr +=1
                            else:
                                self.ssr += 1
                            print(''.join(result),"",end="")
                        print("\n")
                        print(f"Total R: {self.r}, SR: {self.sr}, SSR: {self.ssr}")
            case 2:
                match [self.crystal < 300]:
                    case [True]:
                        print("Sorry, not enough crystal")
                    case _:
                        self.crystal -= 300
                        for i in range(1):
                            result = rd.choices(rarity, weights=odds, k=1)
                            if rarity[0] in result:
                                self.r +=1
                            elif rarity[1] in result:
                                self.sr +=1
                            else:
                                self.ssr += 1
                            print(''.join(result),"",end="")
                        print("\n")
                        print(f"Total R: {self.r}, SR: {self.sr}, SSR: {self.ssr}")
            case _:
                print("input a number!")
