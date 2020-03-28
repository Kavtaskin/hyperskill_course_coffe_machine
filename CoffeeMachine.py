class CoffeeMachine:
    """
    A virtual coffee machine simulator
    """
    water = 0  # (milliliters)
    milk = 0  # (milliliters)
    beans = 0  # (grams)
    money = 0  # (us dollars)
    cups = 0 # (pieces)

    def __init__(self, water, milk, beans, cups, money):
        """
        Initializes a new CoffeeMachine object
        :return: A new CoffeeMachine object.
        """
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        # Available types of coffee with the necessary ingredients: water, milk, beans, cups, money
        self.espresso = [250, 0, 16, 1, 4]
        self.latte = [350, 75, 20, 1, 7]
        self.cappuccino = [200, 100, 12, 1, 6]

    def print_state(self):
        """
        Prints the current states of the coffee machine
        :return: None
        """
        print('The coffee machine has:')
        print(self.water, 'of water')
        print(self.milk, 'of milk')
        print(self.beans, 'of coffee beans')
        print(self.cups, 'of disposable cups')
        print(self.money, 'of money')

    def work(self):
        """
        A resources check is initiated if the user does not choose to exit
        :return: None
        """
        user_input = str(input("Write action (buy, fill, take, remaining, exit):")).lower()
        if user_input != 'exit':
            self.action_check(user_input)

    def action_check(self, action):
        """
        Checking the selected user action
        :param action: String
        :return: None
        """
        if action == 'remaining':
            self.print_state()
        elif action == 'fill':
            self.fill()
        elif action == 'take':
            self.take()
        elif action == 'buy':
            self.buy()
        else:
            print("Invalid Action")
        # Looping the program
        self.work()


    def buy(self):
        """
        Launch the function to check the necessary resources depending on the type of coffee selected by the user
        :return: None
        """
        coffee_type = str(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")).lower()
        if coffee_type == "back":
            self.work()
        elif coffee_type == "1":
            self.check_resources(self.espresso)
        elif coffee_type == "2":
            self.check_resources(self.latte)
        elif coffee_type == "3":
            self.check_resources(self.cappuccino)
        else:
            print("Invalid Action")

    def check_resources(self, coffee_type):
        """
        Checking that there are enough resources for the selected type of coffee,
        if so, existing resources are reduced, money is added
        :return: None
        """
        if self.water < coffee_type[0]:
                print("Sorry, not enough water!")
        elif self.milk < coffee_type[1]:
                print("Sorry, not enough milk")
        elif self.beans < coffee_type[2]:
                print("Sorry, not enough beans!")
        elif self.cups == coffee_type[3]:
                print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= coffee_type[0]
            self.beans -= coffee_type[1]
            self.milk -= coffee_type[2]
            self.cups -= 1
            self.money += coffee_type[4]

    def fill(self):
        """
        Makes changes to all elements in self.resources (except 'money') attribute by taking input from the user
        ( i.e the special worker ). The provided inputs must be integer values in respective units.
        On occurance of a ValueError it displays a a error message telling the user to try again.

        :return: None
        """
        self.water += int(input('Write how many ml of water do you want to add:'))
        self.milk += int(input('Write how many ml of milk do you want to add:'))
        self.beans += int(input('Write how many grams of coffee beans do you want to add:'))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add:'))

    def take(self):
        """
        If the value of the variable 'self.money' > 0 prints the value and resets it to zero
        (i.e it gives the virtual money to the user)
        :return: None
        """
        if self.money > 0:
            print('I gave you $' + str(self.money))
            self.money = 0
        else:
            print("Sorry, the Coffee Machine has no money left!")

def main():
    # Initialize a new CoffeeMachine object with current available resources.
    coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
    coffee_machine.work()

if __name__ == "__main__":
    main()
