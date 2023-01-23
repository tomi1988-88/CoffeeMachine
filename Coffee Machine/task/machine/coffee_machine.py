SUPPLIES = (400, 540, 120, 9, 550)


class CoffeeMachine:

    def __init__(self, supplies):

        self.water, self.milk, self.coffee, self.cups, self.money = supplies

        self.options = {
                        "buy": self.__buy,
                        "fill": self.__fill,
                        "take": self.__take,
                        "remaining": self.__str__
                        }
        self.coffee_types = {
                             "1": {"water": 250, "coffee": 16, "cost": 4},
                             "2": {"water": 350, "milk": 75, "coffee": 20, "cost": 7},
                             "3": {"water": 200, "milk": 100, "coffee": 12, "cost": 6},
                             "back": False
                             }

    def __str__(self):
        print(f"""The coffee machine has:
{self.water} ml of water
{self.milk} ml of milk
{self.coffee} g of coffee beans
{self.cups} disposable cups
${self.money} of money
""")

    def user_input(self):
        while True:
            user = input("Write action (buy, fill, take):\n")

            if user == "exit":
                break
            elif user not in self.options:
                continue
            else:
                self.options.get(user)()

    def __buy(self):
        while True:
            user = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")

            if user in self.coffee_types:
                choice = self.coffee_types.get(user)
                ### if user == "back" -> choice == False so we leave the loop
                ### and we are back in user_input loop
                if choice:
                    lack_resources = self.__check_lack_resources(choice)

                    if lack_resources:
                        print(f"Sorry, not enough {', '.join(lack_resources)}!")
                    else:
                        print("I have enough resources, making you a coffee!")

                        self.water -= choice.get("water", 0)
                        self.milk -= choice.get("milk", 0)
                        self.coffee -= choice.get("coffee", 0)
                        self.cups -= 1
                        self.money += choice.get("cost", 0)
                break
            else:
                continue

    def __fill(self):
        to_add = ["Write how many ml of water you want to add:\n", "Write how many ml of milk you want to add:\n",
                  "Write how many grams of coffee beans you want to add:\n",
                  "Write how many disposable cups you want to add:\n"]

        to_add = [int(input(i)) for i in to_add]

        self.water += to_add[0]
        self.milk += to_add[1]
        self.coffee += to_add[2]
        self.cups += to_add[3]

    def __take(self):
        print(f"I gave you {self.money}")
        self.money = 0

    def __check_lack_resources(self, choice):

        supplies = [("water", self.water - choice.get("water")),
                    ("milk", self.milk - choice.get("milk", 0)),
                    ("coffee beans", self.coffee - choice.get("coffee")),
                    ("cups", self.cups - 1)]

        lack_resources = [i[0] for i in supplies if i[1] < 0]

        if lack_resources:
            return lack_resources
        else:
            return False


if __name__ == "__main__":
    coffee_machine = CoffeeMachine(SUPPLIES)
    coffee_machine.user_input()

