import random

class Card:
    def __init__(self, num, shape):
        self.num = num
        self.shape = shape

    def __str__(self):
        return f"{self.num} {self.shape}"

        ######################


class Player:
    def __init__(self, player_name = "player"):
        self.player_name = player_name
        self.list_cards = []

    def get_card(self):
        return self.list_cards.pop(0)

    def add_card(self, win_card):
        self.list_cards.extend(win_card)

    def len_cards(self):
        return len(self.list_cards)


    ############################


class Game:
    def __init__(self):
        self.player = Player()
        self.computer = Player()
        self.all_cards = []


        for num in range(2, 15):
            for shape in ["C", "S", "D", "H"]:
                self.all_cards.append((num, shape))
        for i in range(1000):
            a = random.randint(1, 52)
            b = random.randint(1, 52)
            while a == b:
                b = random.randint(1, 52)
            self.all_cards[a-1], self.all_cards[b-1] = self.all_cards[b-1], self.all_cards[a-1]

        self.computer.list_cards = self.all_cards[0:26]
        self.player.list_cards = self.all_cards[26:]

    def play_round(self):
        player_card = self.player.get_card()
        computer_card = self.computer.get_card()
        print(f"""
        • ========== TURN ==========
        •{self.player.player_name}: {player_card}
        • Computer: {computer_card}
        """)

        if player_card[0] > computer_card[0]:
            print(f"• {self.player.player_name} won the round!")
            self.player.add_card(computer_card)
        elif player_card[0] < computer_card[0]:
            print("• computer won the round!")
            self.computer.add_card(player_card)
        else:
            print("• It's a draw!")


        print(f"• Player cards: {self.player.len_cards()} | Computer cards: {self.computer.len_cards()}")

    ##################################

def main():
    game = Game()
    flag = True
    while flag:
        game_flag = True
        while game_flag:
            choose = input("""
            • 1. Play turn
            • 2. Exit
            """).strip()

            if choose == "1":
                try:
                    game.play_round()
                except:
                    print("Game Over")
                    game_flag = False
            elif choose == "2":
                game_flag = False
            else:
                print("Illegal option. try again")
        end_choose = input("""
        • 1. Play turn
        • 2. Exit
                """).strip()
        if end_choose == "1":
            continue
        else:
            print("you are looser")
            flag = False




main()



