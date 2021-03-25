# 1.Store
# class Store:
#     def __init__(self, name, type, capacity):
#         self.name = name
#         self.type = type
#         self.capacity = capacity
#         self.items = {}
#         self.items_count = 0
#
#     @staticmethod
#     def can_add_item(count, capacity):
#         return count < capacity
#
#     @staticmethod
#     def can_remove_item(items, item_name, amount):
#         return item_name in items and amount <= items[item_name]
#
#     @classmethod
#     def from_size(cls, name, type, size):
#         return cls(name, type, size // 2)
#
#     def add_item(self, item_name):
#         if not self.can_add_item(self.items_count, self.capacity):
#             return "Not enough capacity in the store"
#         self.items_count += 1
#         if item_name not in self.items:
#             self.items[item_name] = 0
#         self.items[item_name] += 1
#         return f"{item_name} added to the store"
#
#     def remove_item(self, item_name, amount):
#         if not self.can_remove_item(self.items, item_name, amount):
#             return f"Cannot remove {amount} {item_name}"
#         self.items_count -= 1
#         self.items[item_name] -= amount
#         return f"{amount} {item_name} removed from the store"
#
#     def __repr__(self):
#         return f"{self.name} of type {self.type} with capacity {self.capacity}"



# 2.Integer
# import math
# class Integer:
#     def __init__(self, value):
#         self.value = value
#
#     @classmethod
#     def from_float(cls, value):
#         if type(value) != float:
#             return "value is not a float"
#         return cls(math.floor(value))
#
#     @classmethod
#     def from_roman(cls, value):
#         roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         result = 0
#         for i, c in enumerate(value):
#             if (i + 1) == len(value) or roman_numerals[c] >= roman_numerals[value[i + 1]]:
#                 result += roman_numerals[c]
#             else:
#                 result -= roman_numerals[c]
#         return cls(result)
#
#     @classmethod
#     def from_string(cls, value):
#         if type(value) != str:
#             return "wrong type"
#         return cls(int(value))
#
#     def add(self, integer):
#         if type(integer) != Integer:
#             return "number should be an Integer instance"
#         return self.value + integer.value



# 3.Calculator
# class Calculator:
#     @staticmethod
#     def add(*args):
#         return sum(args)
#
#     @staticmethod
#     def multiply(*args):
#         result = 1
#         for arg in args:
#             result *= arg
#         return result
#
#     @staticmethod
#     def divide(argum, *args):
#         result = argum
#         for arg in args:
#             result /= arg
#         return result
#
#     @staticmethod
#     def subtract(argum, *args):
#         result = argum
#         for arg in args:
#             result -= arg
#         return result


