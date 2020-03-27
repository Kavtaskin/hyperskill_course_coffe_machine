class CoffeeMachine:
    state_coffee_machine = "choosing an action"
    n_coffee_machine = 0
    water = 0
    milk = 0
    beans = 0
    cups = 0
    money = 0

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def print_coffe_machine_state(self):
        print('The coffee machine has:')
        print(self.water, 'of water')
        print(self.milk, 'of milk')
        print(self.beans, 'of coffee beans')
        print(self.cups, 'of disposable cups')
        print(self.money, 'of money')

    def work(self, user_action):
        if user_action == 'remaining':
            self.print_coffe_machine_state()
        elif user_action == 'exit':
            return "exit"
        elif user_action == 'fill':
            self.fill()
        elif user_action == 'take':
            self.take()
        elif user_action == 'buy':
            self.buy()

    def buy(self):
        coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        if coffee == "1":
            if self.water < 250:
                print("Sorry, not enough water!")
                return "Sorry"
            if self.beans < 16:
                print("Sorry, not enough beans!")
                return "Sorry"
            if self.cups == 0:
                print("Sorry, not enough cups!")
                return "Sorry"
            print("I have enough resources, making you a coffee!")
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.money += 4
        elif coffee == "2":
            if self.water < 350:
                print("Sorry, not enough water!")
                return "Sorry"
            if self.milk < 75:
                print("Sorry, not enough milk")
                return "Sorry"
            if self.beans < 20:
                print("Sorry, not enough beans!")
                return "Sorry"
            if self.cups == 0:
                print("Sorry, not enough cups!")
                return "Sorry"
            print("I have enough resources, making you a coffee!")
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.money += 7
        elif coffee == "3":
            if self.water < 200:
                print("Sorry, not enough water!")
                return "Sorry"
            if self.milk < 100:
                print("Sorry, not enough milk")
                return "Sorry"
            if self.beans < 12:
                print("Sorry, not enough beans!")
                return "Sorry"
            if self.cups == 0:
                print("Sorry, not enough cups!")
                return "Sorry"
            print("I have enough resources, making you a coffee!")
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.money += 6

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add:'))
        self.milk += int(input('Write how many ml of milk do you want to add:'))
        self.beans += int(input('Write how many grams of coffee beans do you want to add:'))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add:'))

    def take(self):
        print('I gave you $' + str(self.money))
        self.money = 0


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    user_input = input("Write action (buy, fill, take, remaining, exit):")
    if coffee_machine.work(user_input) == "exit":
        break

