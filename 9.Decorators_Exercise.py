# 1.Logged
def logged(func):

    def wrapper(*args):

        result = func(*args)
        return f"you called {func.__name__}{args}\nit returned {result}"

    return wrapper


# 2.Even Parameters
def even_parameters(func):
    not_even_parameters = []

    def wrapper(*args):
        for el in args:
            if not isinstance(el, int) or not el % 2 == 0:
                not_even_parameters.append(el)
        if not_even_parameters:
            return "Please use only even numbers!"

        return func(*args)

    return wrapper



# 3.Bold, Italic, Underline
def make_bold(func):
    def wrapper(*args):
        return f"<b>{func(*args)}</b>"
    return wrapper

def make_italic(func):
    def wrapper(*args):
        return f"<i>{func(*args)}</i>"
    return wrapper

def make_underline(func):
    def wrapper(*args):
        return f"<u>{func(*args)}</u>"
    return wrapper



# 4.Type Check
def type_check(type):
    def decorator(func):
        def wrapper(param):
            if isinstance(param, type):
                return func(param)
            return "Bad Type"
        return wrapper
    return decorator


# 5.Cache
def cache(func):
    def wrapper(n):
        wrapper.log[n] = func(n)
        return func(n)
    wrapper.log = {}
    return wrapper



# 6.HTML Tags
def tags(tag):
    def decorator(func):
        def wrapper(*args):
            return f"<{tag}>{func(*args)}</{tag}>"
        return wrapper
    return decorator




# 7.Execution Time
from timeit import default_timer
def exec_time(func):
    def wrapper(*args):
        start = default_timer()
        func(*args)
        end = default_timer()
        return end - start
    return wrapper



# 8.Store Results
class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        with open("results.txt", "a") as file:
            file.write(f"Function {self.func.__name__} was add called. Result: {self.func(*args)}\n")










