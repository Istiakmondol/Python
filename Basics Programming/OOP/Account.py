class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no

    def debit(self,amount):
        if self.balance<amount:
            print("Insufficient Balance...")
        else:
            self.balance-=amount
            print(f"TAKA BDT{amount} was debited. Your current balance is {self.balance}")

    def credit(self,amount):
        self.balance+=amount
        print(f"TAKA BDT{amount} was credited")

    def print(self):
        print(f"Your Reamin Balance at account {self.account_no} is {self.balance}")


acc1=Account(10000,"AC08374326829")
acc1.debit(4750)
acc1.credit(751)
acc1.print()