import math


class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __repr__(self):
        return f"{self.x}, {self.y}"

    
    def norm(self):
        return math.sqrt(self.x**2+self.y**2)
        


# p.norm() et Point.norm(p) donnent le même résultat
#Si on def norm sans self, on a un message d'erreur lorqu'on appelle p.norm() car on donne l'argument self à une fonction sans argument
#Sans __repr__, python affiche <__main__.Point object at 0x104d67fd0>
class Bad:
    items = []

    def add(self, x):
        self.items.append(x)

#a, b = Bad(), Bad()
#a.add(1)
#print(b.items)

#b voit l'élément ajouté à a car items est une variable globale
#Pour que chaque instance ait sa propre liste, il faut faire init

class Tirelire:
    def __init__(self):
        self.tirelire=[]
    def __len__(self):
        return len(self.tirelire)

    def deposit(self,value: float):
            self.tirelire.append(value)

    def total(self):
        a=0
        for e in self.tirelire:
            a=a+e
        return a
    

# pour tester


#t = Tirelire()
#t.deposit(0.5)
#t.deposit(1)
#print(len(t))

from collections import defaultdict

class Student:
    def __init__(self, first_name: str, last_name: str):
        self.first_name=first_name
        self.last_name=last_name
        self.grades=defaultdict(list)

    def __repr__(self):
        return f"{self.fist_name},{self.last_name}"

    def add_grade(self, course: str, grade: float):
        if 0<= grade <=20:
            self.grades[course].append(grade)
        else:
            raise ValueError

    def followed_topics(self):
        L=[]
        for a,e in self.grades.items():
            L.append(a)
        return L

    def compute_average(self, course: str):
        notes = self.grades[course]
        return sum(notes) / len(notes)


class Classe:
    def __init__(self, classname: str):
        self.classname=classname

    def add_student(self, student: Student):
        
   
    

 




    
    