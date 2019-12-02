
class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Owner: {self.owner}, Balance: $ {self.balance}'
        return self.owner, self.balance

    def deposit(self, importo):
        self.balance = self.balance + importo
        print('Deposit Accepted, new balance: {}'.format(self.balance))

    def withdraw(self, importo):
        if self.balance - importo < 0:
            print('Funds Unavailable!')
        else:
            self.balance = self.balance - importo
            print('Withdrawal Accepted, new balance: {}'.format(self.balance))


acct1 = Account('Jose', 100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)
