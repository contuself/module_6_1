class Animal: #Родительский
    def __init__(self, name):
        self.name = name
        self.alive = True  # Состояния здоровья
        self.fed = False  # Накормленный

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant: #Родительский
    def __init__(self, name):
        self.name = name
        self.edible = False  # Съедобность

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

a1 = Predator('Волк с Уолл-Стрит')

a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')

p2 = Fruit('Заводной апельсин')



print(a1.name)

print(p1.name)



print(a1.alive)

print(a2.fed)

a1.eat(p1)

a2.eat(p2)

print(a1.alive)

print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.



# Вывод на консоль:
#
# Волк с Уолл-Стрит
#
# Цветик семицветик
#
# True
#
# False
#
# Волк с Уолл-Стрит не стал есть Цветик семицветик
#
# Хатико съел Заводной апельсин
#
# False
#
# True
# Примечания:

# Помните, обращаясь к атрибутам объекта текущего класса используйте параметр self.
# Передавая объекты классов Fruit и Flower в метод eat, так же можно обращаться к их атрибутам внутри.
# Обращайте внимание на то, где атрибут класса, а где атрибут объекта.