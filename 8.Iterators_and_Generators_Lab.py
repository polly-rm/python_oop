# 1.Custom Range
# class custom_range:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.current = start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current > self.end:
#             raise StopIteration
#         current = self.current
#         self.current += 1
#         return current


# 2.Reverse Iter
# class reverse_iter:
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.current_index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if abs(self.current_index) > len(self.iterable):
#             raise StopIteration
#         current_index = self.current_index
#         self.current_index -= 1
#         return self.iterable[current_index]


# 3.Vowels
# class vowels:
#     vowels_mapper = {'A', 'a', 'E', 'e', 'Y', 'y', 'U', 'u', 'O', 'o', 'I', 'i'}
#
#     def __init__(self, string):
#         self.string = string
#         self.current_index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current_index > len(self.string) - 1:
#             raise StopIteration
#         current_index = self.current_index
#         self.current_index += 1
#         if self.string[current_index] in vowels.vowels_mapper:
#             return self.string[current_index]
#         return self.__next__()



# 4.Squares
# def squares(n):
#     for num in range(1, n+1):
#         yield num ** 2


# 5.Generator Range
# def genrange(start, end):
#     for num in range(start, end+1):
#         yield num


# 6.Reverse String
def reverse_text(text):
    for i in range(-1, -len(text)-1, -1):
        yield text[i]