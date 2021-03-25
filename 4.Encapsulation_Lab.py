# 1.Person
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age


# 2.Email Validator
# class EmailValidator:
#     def __init__(self, min_length, mails, domains):
#         self.min_length = min_length
#         self.mails = mails
#         self.domains = domains
#
#     def __validate_name(self, name):
#         return len(name) >= self.min_length
#
#     def __validate_mail(self, mail):
#         return mail in self.mails
#
#     def __validate_domain(self, domain):
#         return domain in self.domains
#
#     def validate(self, mail):
#         name, mail_domain = mail.split("@")
#         mail, domain = mail_domain.split(".")
#         if self.__validate_name(name) and self.__validate_mail(mail) and self.__validate_domain(domain):
#             result = True
#         else:
#             result = False
#         return result



# 3.Mammal
# class Mammal:
#     __kingdom = "animals"
#
#     def __init__(self, name, type, sound):
#         self.name = name
#         self.type = type
#         self.sound = sound
#
#     def make_sound(self):
#         return f"{self.name} makes {self.sound}"
#
#     def get_kingdom(self):
#         return Mammal.__kingdom
#
#     def info(self):
#         return f"{self.name} is of type {self.type}"


# 4.Account
# class Account:
#     def __init__(self, id, balance, pin):
#         self.__id = id
#         self.balance = balance
#         self.__pin = pin
#
#     def get_id(self, pin):
#         if pin == self.__pin:
#             return self.__id
#         return "Wrong pin"
#
#     def change_pin(self, old_pin, new_pin):
#         if old_pin == self.__pin:
#             self.__pin = new_pin
#             return "Pin changed"
#         return "Wrong pin"




        
        







