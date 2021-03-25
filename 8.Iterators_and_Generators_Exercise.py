# 1.Take Skip
class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current_num = 0
        self.index_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index_num >= self.count:
            raise StopIteration
        current_num = self.current_num
        self.current_num += self.step
        self.index_num += 1
        return current_num


# 2.Dictionary Iteroator
class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.dictionary):
            raise StopIteration
        current_key = [key for key in self.dictionary][self.current_index]
        current_value = self.dictionary[current_key]
        self.current_index += 1
        return (current_key, current_value)



# 3.Countdown Iterator
class countdown_iterator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 0:
            raise StopIteration
        current_num = self.count
        self.count -= 1
        return current_num


# 4.Sequence Repeat
class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0
        self.repetition_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.repetition_count >= self.number:
            raise StopIteration
        if self.index >= len(self.sequence):
            self.index = 0
        char = self.sequence[self.index]
        self.index += 1
        self.repetition_count += 1
        return char



# 5.Take Halves
def solution():
    def integers():
        current_number = 1
        while True:
            yield current_number
            current_number += 1

    def halves():
        for i in integers():
            yield i/2

    def take(n, seq):
        nums = []
        for el in seq:
            if len(nums) == n:
                return nums
            nums.append(el)

    return (take, halves, integers)


# 6.Fibonacci Generator
def fibonacci():
    previous_num, current_num = 0, 1
    while True:
        yield previous_num
        previous_num, current_num = current_num, current_num + previous_num


# 7.Reader
def read_next(*args):
    for el in args:
        for sub_el in el:
            yield sub_el



# 8.Prime Numbers
def get_primes(numbers):
    for num in numbers:
        is_prime = True
        if num < 2:
            continue
        for divisor in range(2, num):
            if num % divisor == 0:
                is_prime = False
        if is_prime:
            yield num


# 9.Possible Permutations
from itertools import permutations
def possible_permutations(nums):
    for el in permutations(nums):
        yield list(el)





