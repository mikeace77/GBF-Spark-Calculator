class Choices:
    
    def __init__(self):
        self.crystal = 0
        self.one_tix = 0
        self.ten_tix = 0
    
    def xtall(self):
        try:
            user_input = int(input("How much crystal you have?: "))
        except ValueError:
            print("Please input a number!")
        self.crystal += user_input
        print("\n"*100)

    def one_tickets(self):
        try:
            user_input = int(input("How much tickets you have?: "))
        except ValueError:
            print("Please input a number!")
        self.one_tix += user_input
        print("\n"*100)

    def ten_tickets(self):
        try:
            user_input = int(input("How much tickets you have?: "))
        except ValueError:
            print("Please input a number!")
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