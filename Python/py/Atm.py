class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber =  cardnumber
        self.pin = pin 

    def balanceinquiry(self):
        print("Your balance is: $100")

    def cashwidthdrawal(self, amount):
        new_amount = 100-amount
        print("You withdrawed: " + str(amount) + " Your remaining balance is: " + str(new_amount))

def main():
        name = input("Hello what is your name?")
        print("Hello, " + name)
        cardnumber = input("Insert your card number: ")
        pin = input("Enter your pin: ")
        new_user = Atm(cardnumber, pin)

        print("Choose your activity")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        activity = int(input("Enter activity choice: "))
        
        if (activity == 1):
            new_user.balanceinquiry()
        elif (activity == 2):
            amount = int(input("Enter the amount: "))
            new_user.cashwidthdrawal(amount)
        else:
            print("Enter a valid number")
            
if __name__ == "__main__":
    main()