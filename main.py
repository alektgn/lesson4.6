class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self):
        self.player = Hero(input("Введите имя вашего героя: "))
        self.computer = Hero("Компьютерный герой")

    def start(self):
        turn = 0
        while self.player.is_alive() and self.computer.is_alive():
            if turn % 2 == 0:
                self.player.attack(self.computer)
                print(f"У {self.computer.name} осталось {self.computer.health} здоровья.")
            else:
                self.computer.attack(self.player)
                print(f"У {self.player.name} осталось {self.player.health} здоровья.")
            turn += 1

        if self.player.is_alive():
            print(f"{self.player.name} побеждает!")
        else:
            print("Компьютерный герой побеждает!")

if __name__ == "__main__":
    game = Game()
    game.start()