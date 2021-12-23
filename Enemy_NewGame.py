import random


class Enemy:

    def __init__(self, speed, size): 

        print("New enemy created")

        self.speed = speed
        self.size = size

    def __str__(self):
        text = ""
        text += "Enemy information:\n"
        text += f"- speed: {self.speed}\n"
        text += f"- size: {self.size}\n"
        return text
    


if __name__ == "__main__":
    enemy = Enemy(speed=4, size=3)
    print(enemy)