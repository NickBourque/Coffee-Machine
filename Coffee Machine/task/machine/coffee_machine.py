class CoffeeMachine:
    
    cups = 9
    money = 550
    water = 400
    milk = 540
    beans = 120


    def print_quantities(self):
        # global cups
        # global money
        # global water
        # global milk
        # global beans
        
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.beans) + " of coffee beans")
        print(str(self.cups) + " of disposable cups")
        print(str(self.money) + " of money")

    def take(self):
        # global money
        print("I gave you $" + str(self.money))
        self.money = 0
        
    def fill(self):
        # global cups
        # global water
        # global milk
        # global beans
        
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))
        
    def buy(self):
        x = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        
        if x == "1":
            self.buy_espresso()
        elif x == "2":
            self.buy_latte()
        elif x == "3":
            self.buy_cappuccino()
            
    def buy_espresso(self):
        # global water
        # global beans
        # global money
        # global cups
        
        if self.water < 250:
            print("Sorry, not enough water!")
        elif self.beans < 16:
            print("Sorry, not enough coffee beans!")
        else:
            self.water -= 250
            self.beans -= 16
            self.money += 4
            self.cups -= 1
            print("I have enough resources, making you a coffee!")
            
        
    def buy_latte(self):
        # global water
        # global milk
        # global beans
        # global money
        # global cups
        
        if self.water < 350:
            print("Sorry, not enough water!")
        elif self.milk < 75:
            print("Sorry, not enough milk!")
        elif self.beans < 20:
            print("Sorry, not enough coffee beans!")
        else:
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.money += 7
            self.cups -= 1
            print("I have enough resources, making you a coffee!")
        
    def buy_cappuccino(self):
        # global water
        # global milk
        # global beans
        # global money
        # global cups
        
        if self.water < 200:
            print("Sorry, not enough water!")
        elif self.milk < 100:
            print("Sorry, not enough milk!")
        elif self.beans < 12:
            print("Sorry, not enough coffee beans!")
        else:
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.money += 6
            self.cups -= 1
            print("I have enough resources, making you a coffee!")


    def start(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):")

            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.print_quantities()
            elif action == "exit":
                break

coffee_machine = CoffeeMachine()
coffee_machine.start()
