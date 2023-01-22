import datetime
import pytz


def sent():
    print("Your name has been registered at Mahendra Bank. All your money is safe here.")
    print("Your account details has been shared with HDFC bank successfully. Just for backup.")
    print("If you have any queries you can visit both banks.")
    print("You can mail us at mahindrabank.help@gmail.com, if you need any help.")
    print("Please download the Mahendra bank app to see your account status and do your task.")


class Account:
    """ Simple account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance, pin):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("An bank account for the person " + self.name)
        print("Your pin is {}".format(pin))
        sent()

    def deposit(self, amount):
        if 0 < amount <= 2000:
            self.balance += amount
            self.transaction_list.append((self._current_time(), amount))
            print()
            print("You have got ${}".format(amount))
            print(self.transaction_list)
            print()
        else:
            print("You have to type some amount and you can only get till $2000")

    def withdraw(self, amount, destination):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print()
            print("We have found a person called {} and the pin is {}".format(p_name, p_pin))
            print()
            print("You have successfully given ${} to {}".format(amount, destination))
            print()
        else:
            print("You have to type more than zero and less than ${}".format(self.balance))

    def show_balance(self):
        print()
        print("Currently your balance is ${}".format(self.balance))

    def show_transactions(self, w):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print()
            print("${:6} was {} at {}".format(w, tran_type, datetime.datetime.now()))
            print()


if __name__ == '__main__':
    print()
    y_name = input("Type your name here: ")
    y_pin = int(input("Type a transfer code. You can remember: "))
    print()
    details = Account(y_name, 0, y_pin)
    details.show_balance()
    print()
    input("Read the above information and press ENTER: ")

    deposit = float(input("How much money do you want. You can only get till $2000: "))
    details.deposit(deposit)
    details.show_balance()
    details.show_transactions(deposit)

    given = 0
    while True:
        withdraw = float(input("How much money do you want to give or type -0: "))
        if withdraw == -0:
            break
        else:
            p_name = input("Type the name of the person to whom you want to give: ")
            p_pin = int(input("Type the pin of {}: ".format(p_name)))
            details.withdraw(withdraw, p_name)
            details.show_balance()
            given = given + withdraw
            details.show_transactions(withdraw)