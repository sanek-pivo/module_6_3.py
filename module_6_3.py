class Horse: # Horse - класс описывающий лошадь
    def __init__(self):
        super().__init__()
        self.x_distance = 0 # пройденный путь
        self.sound = "Frrr"  # звук, который издаёт лошадь

    def run(self, dx): #  изменение дистанции
        self.x_distance += dx # увеличивает x_distance на dx
        return self.x_distance

class Eagle:  # класс описывающий орла
    def __init__(self):
        super().__init__()
        self.y_distance = 0 #  высота полёта
        self.sound = 'I train, eat, sleep, and repeat' # звук, который издаёт орёл

    def fly(self, dy): # изменение дистанции
        self.y_distance += dy #  увеличивает y_distance на dy.
        return self.y_distance

class Pegasus(Horse, Eagle): # класс описывающий пегаса,наследуется от Horse и Eagle
    def __init__(self):
        super().__init__()
        Eagle.__init__(self)

    def move(self,dx, dy): # метод move
        self.run(dx),    # запускать наследованные методы run и fly соответственно.
        self.fly(dy)

    def get_pos(self): # метод get_pos
        return self.x_distance, self.y_distance #возвращает текущее положение пегаса

    def voice(self): # метод voice
        print(f"{self.sound}") #печатает значение унаследованного атрибута

# по условиям домашнего задания
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()