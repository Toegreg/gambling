import random

money = 0
debt = 0
chance = [True] + [False] * 99  # Adjusted the odds

def gamble(bet):
    global money, debt
    a = random.choice(chance)
    
    if a:
        print("You DOUBLED YOUR MONEY!")
        winnings = bet * 2
        print(f"You earned {winnings}!!!!!")
        money += winnings
    else:
        print("Womp womp womp womp I just ate your money hahahaha")
        debt = debt * 2 + bet
        money -= bet
        print(f"You are now {debt} in debt")
    
    print(f"You have {money} dollar(s) and {debt} in debt")
    
    if input("Do you want to gamble again? ").lower() == "yes":
        new_bet = input("How much money do you want to gamble????? ")
        while not new_bet.isdigit() or int(new_bet) > money:
            print("Invalid input, please enter a valid amount within your money.")
            new_bet = input("How much money do you want to gamble????? ")
        gamble(int(new_bet))
    else:
        print("Goodbye!")

print(f"You have {money} dollar(s)")
a = input("How much money do you want to gamble????? ")

while not a.isdigit():
    print("Invalid input, please enter a number.")
    a = input("How much money do you want to gamble????? ")

a = int(a)

if a > money:
    if input("You don't have that much money. Want to take a loan? ").lower() == "yes":
        debt = input("How much money do you wish to take? ")
        while not debt.isdigit():
            print("Invalid input, please enter a number.")
            debt = input("How much money do you wish to take? ")
        debt = int(debt)
        money += debt

gamble(a)
