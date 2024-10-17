import pytermgui as ptg
from pytermgui import tim, Container, boxes

constants = {
    "enemies": [],
    "items": []
}


class Player:
    def __init__(self, max_health: int, health: int, money: int, inventory: list[object], armor: list[object]):
        self.maxHealth = max_health
        self.health = health
        self.money = money
        self.inventory = inventory
        self.armor = armor

    def obtain(self, item: object) -> int:
        if item in self.inventory:
            self.inventory.item.quantity += item.quantity
        else:
            self.inventory.append(item)

    def lose(self, item: object) -> int:
        # can only lose 1 item at a time
        # doesnt check if item is in inventory

        self.inventory.item.quantity -= 1

        if self.inventory.item.quantity < 1:
            self.inventory.remove(item)


class EventClass:
    ''' turn is -1 if not ingame '''
    def __init__(self, player: object):
        self.player = player
        self.turn = -1
        self.currentEnemy = None

    def main(self):
        pass

    def buy(self, item: object) -> bool:
        if self.player.money >= item.price:
            self.player.money -= item.price
            self.player.obtain(item)
            return True
        else:
            tim.print("[red bold]You do not have the funds to purchase this item.")
            return False

    def sell(self, item: object) -> int:
        self.player.money += (item.price/item.quantity)/2
        self.player.lose(item)
        return self.player.inventory.item.quantity

    def use(self, item: object) -> object:
        if item.type == "a":
            # armor
            pass
        elif item.type == "w":
            # weapon
            pass
        elif item.type == "c":
            # consumable
            pass

        return item
    
    def forfeit(self):
        pass

    def enemyTurn(self):
        pass

    def checkArmor(self, armor: list[object], damage: int) -> int:
        pass

    ''' called every turn to determine if the game has been won and calls the next function '''
    def check(self):
        pass


class Item:
    ''' types include armor (a), weapon (w), consumable (c) '''
    def __init__(self, name: str, item_type: str, description: str, price: int, quantity: int, armor: int,
                 armor_piece: int, damage: int, damageType: str, effect: str):
        self.name = name
        self.type = item_type
        self.description = description
        self.price = price
        self.quantity = quantity
        self.armor = armor
        self.armorPiece = armor_piece
        self.damage = damage
        self.damageType = damageType
        self.effect = effect
        constants["items"].append(self)


class Enemy:
    def __init__(self, name: str, description: str, reward: int, armor: list[object], attacks: list[list]):
        self.name = name
        self.description = description
        self.reward = reward
        self.armor = armor
        self.attacks = attacks
        constants["enemies"].append(self)

    def challenge() -> object:
        pass


def main():
    tim.define("!buzz", lambda: print("Hello world"))
    tim.print("[bold aqua] HELLO WORLD!!")
    window = ptg.Window(
        "[bold]Title",
        "[red]content",
        box="SINGLE",
        title="[bold aqua]Shop:"
    )
    # for line in window.get_lines():
    #     print(line)


if __name__ == '__main__':
    main()
