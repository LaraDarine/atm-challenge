class ATM:

    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.cache_categories = [100, 50, 10, 5, 1]

    def withdraw(self, request):
        print("current balance = ", self.balance, "- your request = ", request)
        result = self.balance
        self.check_balance(request)

        return result

    def check_balance(self, request):
        if request > self.balance:
            print("Can't give you all this money!!")

        elif request < 0:
            print("More than zero plz!")

        else:
            self.balance -= request
            self.give_cache_category(request)

        return self.balance

    def give_cache_category(self, request):
        for cache_category in self.cache_categories:
            while request >= cache_category:
                request -= cache_category
                print("give " + str(cache_category))

        return self.balance


balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Saba Bank")
print("Welcome to " + atm1.bank_name)
atm2 = ATM(balance2, "Jeen Bank")
print("Welcome to " + atm2.bank_name)

atm1.withdraw(700)
atm1.withdraw(421)
atm1.withdraw(82)

atm2.withdraw(500)
atm2.withdraw(450)
atm2.withdraw(51)
