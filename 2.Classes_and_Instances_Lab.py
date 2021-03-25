# 1.Smartphone
class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = not self.is_on

    def install(self, app, app_memory):
        if app_memory > self.memory:
            return f"Not enough memory to install {app}"
        if self.is_on:
            self.apps.append(app)
            self.memory -= app_memory
            return f"Installing {app}"
        return f"Turn on your phone to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


# 2.Vet
class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        if len(Vet.animals) >= Vet.space:
            return "Not enough space"
        Vet.animals.append(animal_name)
        self.animals.append(animal_name)
        return f"{animal_name} registered in the clinic"

    def unregister_animal(self, animal_name):
        if animal_name not in self.animals:
            return f"{animal_name} not in the clinic"
        self.animals.remove(animal_name)
        Vet.animals.remove(animal_name)
        return f"{animal_name} unregistered successfully"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space-len(Vet.animals)} space left in clinic"



# 3.Glass
class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml):
        if self.content + ml > Glass.capacity:
            return f"Cannot add {ml} ml"
        self.content += ml
        return f"Glass filled with {ml} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        return f"{Glass.capacity-self.content} ml left"








