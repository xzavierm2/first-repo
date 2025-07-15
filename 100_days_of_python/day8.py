import random

symbols = ['🍒 ',' 🍇 ', '🍉 ', '7️⃣']

class Player:
    def __init__(self,name,customer_balance = 10,):
        self.name = name
        self.customer_balance = customer_balance

    def deposit(self,amount):
        self.customer_balance -= amount
        print(f'How much do you want to deposit: {amount}')

    def withdraw(self,amount):
        self.customer_balance += amount
        print('Withdraw?: ')

    def win(self, amount):
        self.customer_balance += amount
        print(f' You won: ${amount}')

    def lose(self, amount):
        self.customer_balance -= amount
        print(f'Subtracted: ${amount}')

    def amount_money(self):
        return self.customer_balance > 0



class SlotMachine:
    def __init__(self,player):
        self.player = player
    
    def spin(self):
        return random.choices(symbols, k=3)
    
    def play(self):
        print(f'This is the balance of the slot machine: ${self.balance}')
        while self.player.amount_money():
            print("You can Spin again, please Deposit Bet:")
            results = self.spin()
            print(" | ".join(results))
            if results.count('7️⃣') == 3:
                print("Jackpot | 💰 ")
            else:
                print("Thank you for playing!")

            player = str(input("Do you want to continue playing? Y or N: "))

            if player == "Y":
                print("Again")
            elif player == "N":
                print("Goodbye")
                break
            else:
                print("Wrong answer.")

player = Player("John",balance = 10)
game = SlotMachine(player)
game.play()
