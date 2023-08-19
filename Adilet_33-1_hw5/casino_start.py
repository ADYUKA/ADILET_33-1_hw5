from casino_logic import CasinoGame

if __name__ == "__main__":
    game = CasinoGame()
    bet = int(input("Введите свою ставку: "))
    game.play(bet)
