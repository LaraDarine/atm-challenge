class ATM:

    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name

    def withdraw(self, request):
        print("current balance =", self.balance, "your request =", request)
        result = self.balance

        if request > self.balance:
            print("Can't give you all this money !!")

        elif request < 0:
            print("More than zero plz!")

        else:
            self.balance -= request

            while request > 0:




                if request >= 100:
                    request -= 100
                    print("give 100")

                elif request >= 50:
                    request -= 50
                    print("give 50")

                elif request >= 10:
                    request -= 10
                    print("give 10")

                elif request >= 5:
                    request -= 5
                    print("give 5")

                elif request >= 1:
                    print("give 1")
                    request = 0

            result = self.balance - request

        return result
balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Saba Bank")
print("Welcome to Saba Bank")
atm2 = ATM(balance2, "Jeen Bank")
print("Welcome to Jeen Bank")

atm1.withdraw(700)
atm1.withdraw(421)
atm1.withdraw(82)

atm2.withdraw(500)
atm2.withdraw(450)
atm2.withdraw(51)
