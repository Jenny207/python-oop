class Transaction:
    def __init__(self, id: int, before: int, after: int):
        self.id = id
        self.before = before
        self.after = after

    def changed(self) -> bool:
         return self.before != self.after

    def report(self):
        if self.changed():
            if self.after > self.before:
                return str(self.id) + ': ' + f'increased {self.before}->{self.after}'
            else:
                return str(self.id) + ': ' + f'decreased {self.before}->{self.after}'
        else:
            return str(self.id) + ': ' + f'no change'

class BankAccount:
    def __init__(self, account_holder: str):
        self.balance: int = 0
        self.holder = account_holder
        self.transactions: list[Transaction] = []

    def deposit(self, amount: int) -> int:
        before = self.balance
        self.balance += amount

        transaction = Transaction(
            len(self.transactions),
            before,
            self.balance
        )
        self.transactions.append(transaction)

        return self.balance

    def withdraw(self, amount: int) -> int | str:
        before = self.balance

        if amount > self.balance:

            self.transactions.append(
                Transaction(len(self.transactions), before, before)
            )
            return 'Insufficient funds'

        self.balance -= amount
        self.transactions.append(
            Transaction(len(self.transactions), before, self.balance)
        )
        return self.balance

