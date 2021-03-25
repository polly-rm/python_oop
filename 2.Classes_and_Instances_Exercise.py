# 1.Point
# import math
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_x(self, new_x):
#         self.x = new_x
#
#     def set_y(self, new_y):
#         self.y = new_y
#
#     def distance(self, x, y):
#         a = self.x - x
#         b = self.y - y
#         c = a ** 2 + b ** 2
#         return math.sqrt(c)


# 2.Circle
# class Circle:
#     pi = 3.14
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def set_radius(self, new_radius):
#         self.radius = new_radius
#
#     def get_area(self):
#         area = Circle.pi * (self.radius ** 2)
#         return round(area, 2)
#
#     def get_circumference(self):
#         return 2 * Circle.pi * self.radius



# 3.Account
# class Account:
#     def __init__(self, id, name, balance=0):
#         self.id = id
#         self.name = name
#         self.balance = balance
#
#     def credit(self, amount):
#         self.balance += amount
#         return self.balance
#
#     def debit(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             return self.balance
#         return "Amount exceeded balance"
#
#     def info(self):
#         return f"User {self.name} with account {self.id} has {self.balance} balance"



# 4.Employee
# class Employee:
#     def __init__(self, id, first_name, last_name, salary):
#         self.id = id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary
#
#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     def get_annual_salary(self):
#         return 12 * self.salary
#
#     def raise_salary(self, amount):
#         self.salary += amount
#         return self.salary



# 5.Time
# from datetime import datetime, timedelta
# class Time:
#     max_hours = 23
#     max_minutes = 59
#     max_seconds = 59
#
#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#         self.time_object = datetime(100, 1, 1, hour=hours, minute=minutes, second=seconds)
#
#     def set_time(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def get_time(self):
#         return f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}"
#
#     def next_second(self):
#         self.time_object = self.time_object + timedelta(seconds=1)
#         self.hours = self.time_object.hour
#         self.minutes = self.time_object.minute
#         self.seconds = self.time_object.second
#         return self.get_time()



# 6.Pizza Delivery
# class PizzaDelivery:
#     def __init__(self, name, price, ingredients: dict):
#         self.name = name
#         self.price = price
#         self.ingredients = ingredients
#         self.ordered = False
#
#     def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
#         if self.ordered:
#             return f"Pizza {self.name} already prepared and we can't make any changes!"
#         if ingredient not in self.ingredients:
#             self.ingredients[ingredient] = 0
#         self.ingredients[ingredient] += quantity
#         self.price += quantity * ingredient_price
#
#     def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
#         if self.ordered:
#             return f"Pizza {self.name} already prepared and we can't make any changes!"
#         if ingredient not in self.ingredients:
#             return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
#         if quantity > self.ingredients[ingredient]:
#             return f"Please check again the desired quantity of {ingredient}!"
#         self.ingredients[ingredient] -= quantity
#         self.price -= quantity * ingredient_price
#
#     def make_order(self):
#         self.ordered = True
#         all_ingredients = ', '.join([f"{ingr}: {quant}" for ingr, quant in self.ingredients.items()])
#         return f"You've ordered pizza {self.name} prepared with {all_ingredients} and the price will be {self.price}lv."















