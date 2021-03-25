# 1.Vehicle
# from abc import ABC, abstractmethod
#
# class Vehicle(ABC):
#     def __init__(self, fuel_quantity, fuel_consumption):
#         self.fuel_quantity = fuel_quantity
#         self.fuel_consumption = fuel_consumption
#
#     @abstractmethod
#     def drive(self, distance):
#         pass
#
#     @abstractmethod
#     def refuel(self, fuel):
#         pass
#
# class Car(Vehicle):
#
#     def drive(self, distance):
#         if self.fuel_quantity >= distance * (self.fuel_consumption + 0.9):
#             self.fuel_quantity -= distance * (self.fuel_consumption + 0.9)
#
#     def refuel(self, fuel):
#         self.fuel_quantity += fuel
#
# class Truck(Vehicle):
#
#     def drive(self, distance):
#         if self.fuel_quantity >= distance * (self.fuel_consumption + 1.6):
#             self.fuel_quantity -= distance * (self.fuel_consumption + 1.6)
#
#     def refuel(self, fuel):
#         self.fuel_quantity += 0.95 * fuel



# 2.Groups
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __add__(self, other):
#         return Person(self.name, other.surname)
#
#     def __str__(self):
#         return f"{self.name} {self.surname}"
#
# class Group:
#     def __init__(self, name, people):
#         self.name = name
#         self.people = people
#
#     def __len__(self):
#         return len(self.people)
#
#     def __str__(self):
#         return f"Group {self.name} with members {', '.join([p.__str__() for p in self.people])}"
#
#     def __add__(self, other):
#         return Group(name=self.name, people=self.people + other.people)
#
#     def __getitem__(self, item):
#         return f"Person {item}: {self.people[item]}"


# 3.Account
# class Account:
#     def __init__(self, owner, amount=0):
#         self.owner = owner
#         self.amount = amount
#         self._transactions = []
#
#     def add_transaction(self, amount):
#         if not isinstance(amount, int):
#             raise ValueError("please use int for amount")
#         self._transactions.append(amount)
#
#     @property
#     def balance(self):
#         return self.amount + sum(self._transactions)
#
#     @staticmethod
#     def validate_transaction(account, amount_to_add):
#         if account.amount + amount_to_add < 0:
#             raise ValueError("sorry cannot go in debt!")
#         account._transactions.append(amount_to_add)
#         return f"New balance: {account.balance}"
#
#     def __len__(self):
#         return len(self._transactions)
#
#     def __getitem__(self, index):
#         return self._transactions[index]
#
#     def __reversed__(self):
#         return reversed(self._transactions)
#
#     def __gt__(self, other):
#         return self.balance > other.balance
#
#     def __ge__(self, other):
#         return self.balance >= other.balance
#
#     def __lt__(self, other):
#         return self.balance < other.balance
#
#     def __le__(self, other):
#         return self.balance <= other.balance
#
#     def __eq__(self, other):
#         return self.balance == other.balance
#
#     def __ne__(self, other):
#         return self.balance != other.balance
#
#     def __str__(self):
#         return f"Account of {self.owner} with starting amount: {self.amount}"
#
#     def __repr__(self):
#         return f"Account({self.owner}, {self.amount})"
#
#     def __add__(self, other):
#         acc = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
#         acc._transactions = self._transactions + other._transactions
#         return acc













