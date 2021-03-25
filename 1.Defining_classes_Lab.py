# 1.Rhombus of Stars
def draw_line(n, i, symbol):
    offset = " " * (n - i)
    line_of_stars = f"{symbol} " * i
    print(f'{offset}{line_of_stars}')

def draw_rhombus(n):
    for i in range(1, n + 1):
        draw_line(n, i, '*')
    for i in range(n - 1, 0, -1):
        draw_line(n, i, '*')

draw_rhombus(int(input()))


# 2.Class_Book
class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


# 3.Scope Mess
x = "global"

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()

print(x)
outer()
print(x)


# 4.Music
class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics

song = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())


# 5.Cup
class Cup:
    def __init__(self, size, quantity=0):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        self.quantity += milliliters
        if not self.quantity <= self.size:
            self.quantity -= milliliters
            return

    def status(self):
        free_space = self.size - self.quantity
        return free_space

cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())


# 6.Flower
class Flower:
    def __init__(self, name, water_requirements, is_happy=False):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = is_happy

    def water(self, quantity):
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        else:
            return f"{self.name} is not happy"

flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(100)
print(flower.status())







