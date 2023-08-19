import random
from decouple import config

class CasinoGame:
    def __init__(self):
        self.__starting_money = int(config('MY_MONEY'))
        self.__current_money = self.starting_money

    @property
    def starting_money(self):
        return self.__starting_money

    @property
    def current_money(self):
        return self.__current_money

    @current_money.setter
    def current_money(self, value):
        self.__current_money = value

    def play(self, bet):
        win_slot = random.randint(1, 30)
        chosen_slot = int(input(f"Выберите слот от 1 до 30 для ставки (${bet}): "))

        if chosen_slot == win_slot:
            self.current_money += bet * 2
            print(f"Замечательно! Вы выиграли ${bet * 2}. Ваш текущий баланс: ${self.current_money}")
        else:
            self.current_money -= bet
            print(f"Извините, но вы проиграли ${bet}. Ваш текущий баланс: ${self.current_money}")

        if self.current_money <= 0:
            print("Где деньги Лебовски? Game over.")
        else:
            self.play_again()

    def play_again(self):
        choice = input("Хотите сыграть еще раз? (y/n): ").lower()
        if choice == "y":
            bet = int(input("Ваша ставка: "))
            self.play(bet)
        else:
            self.end_game()

    def end_game(self):
        print(f"Ваш нынешний баланс: ${self.current_money}")
        if self.current_money > self.starting_money:
            print("Великолепно! Вы остались в плюсе!")
        elif self.current_money < self.starting_money:
            print("Прошу прощения, но вы в минусе!")
        else:
            print("Вы сохранили свои кровные, закончив с той же суммой, с которой начали!")


