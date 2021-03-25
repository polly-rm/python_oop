# 4.Random List
# import random
#
# class RandomList(list):
#     def get_random_element(self):
#         el_index = random.randint(0, len(self)-1)
#         element = self[el_index]
#         self.pop(el_index)
#         return element
#
# rl = RandomList([1, 2, 1, 3, 4, 5])
# while rl:
#     print(rl.get_random_element())


# 5.Stack of Strings
# class Stack:
#     def __init__(self):
#         self.data = []
#
#     def push(self, item):
#         self.data.append(item)
#
#     def pop(self):
#         return self.data.pop()
#
#     def peek(self):
#         return self.data[-1]
#
#     def is_empty(self):
#         return len(self.data) == 0
#
#     def __repr__(self):
#         return f"[{', '.join(reversed(self.data))}]"




