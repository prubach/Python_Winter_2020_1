class Customer:
    last_id = 0

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        Customer.last_id += 1
        self.customer_id = Customer.last_id

    def __repr__(self):
        return 'Customer[{0}, {1}, {2}]'.format(self.customer_id, self.first_name, self.last_name)


class Account:
    last_id = 0

    def __init__(self, customer):
        self.customer = customer
        self._balance = 0
        Account.last_id += 1
        self.account_id = Account.last_id
        self.interest_rate = 0.01

    def deposit(self, amount):
        #TODO - add validation to prevent misuse
        self._balance += amount

    def charge(self, amount):
        #TODO - add validation to prevent misuse
        self._balance -= amount

    def get_balance(self):
        return self._balance

    def calc_interest(self):
        #TODO - add implementation based on self.interest_rate
        pass

    def __repr__(self):
        return 'Account[{0}, {1}, {2}, {3}, {4}]'.format(self.account_id, self.customer.customer_id, self.customer.last_name, self._balance, self.interest_rate)


class Bank:
    def __init__(self):
        self._accounts = []
        self._customers = []

    def create_customer(self, first_name, last_name, email):
        c = Customer(first_name, last_name, email)
        self._customers.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        self._accounts.append(a)
        return a

    def transfer(self, acc_from, acc_to, amount):
        #TODO - implement it
        pass

    def __str__(self):
        return 'Bank[{0}, {1}]'.format(self._customers, self._accounts)


bank = Bank()


c = bank.create_customer('John', 'Brown', 'john@brown.com')
print(c)

a1 = bank.create_account(c)
a1.deposit(-100.08)
print(a1)


c2 = bank.create_customer('Anne', 'Brown', 'anne@brown.com')
print(c2)
a2 = bank.create_account(c2)
a2.deposit(576.89)
print(a2)

print(bank)


# c = Customer('John', 'Brown', 'john@brown.com')
# print(c)
#
# a1 = Account(c)
# a1.deposit(-100.08)
# print(a1)
#
#
# c2 = Customer('Anne', 'Brown', 'anne@brown.com')
# print(c2)
# a2 = Account(c2)
# a2.deposit(576.89)
# print(a2)
