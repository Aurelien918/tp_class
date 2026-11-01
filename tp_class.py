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

    def report(self):
        largeur = 15
        sep_double = "+" + "=" * largeur + "+" + "=" * largeur + "+"
        sep_simple = "+" + "-" * largeur + "+" + "-" * largeur + "+"
        lignes = [f"Report for student {self.first_name} {self.last_name}"]
        lignes.append(sep_double)
        lignes.append("|" + "Topic".center(largeur) + "|" + "Average".center(largeur) + "|")
        lignes.append(sep_double)
        
        for course in self.grades:
            moyenne = f"{self.compute_average(course):.2f}"
            lignes.append("|" + course.center(largeur) + "|" + moyenne.center(largeur) + "|")
            lignes.append(sep_simple)
        return "\n".join(lignes)

# pour tester

#try:
    #reference_lines = ['Report for student Albert Einstein',
                       '+===============+===============+',
                       '|     Topic     |    Average    |',
                       '+===============+===============+',
                       '|  Mathematics  |     12.80     |',
                       '+---------------+---------------+',
                       '|  Scubadiving  |     12.50     |',
                       '+---------------+---------------+']

   # student = Student("Albert", "Einstein")
   # student.add_grade("Mathematics", 12.80)
   # student.add_grade("Scubadiving", 12.50)
   # report = student.report()
   # report_lines = report.strip().split('\n')
   # assert len(report_lines) == len(reference_lines), \
   #     f"expected {len(reference_lines)} lines, got {len(report_lines)}"
    #for i, (lineref, linestudent) in enumerate(zip(reference_lines, report_lines), start=1):
    #    assert lineref == linestudent, f"Ligne {i} : \n attendu = {lineref}\n  obtenu = {linestudent}"
#except AssertionError as e:
    #print("Les deux chaines sont différentes")
    #print(e)
#except Exception as e:
    #print("OOPS - Something's wrong")
    #print(f"Error message : {e}")
#else:
    #print('Congrats ! Your implementation works !')

#try:
   #r = repr(student)
    #assert "Achille" in r and "Talon" in r, f"first and last name should appear in {r!r}"
#except Exception as e:
    #print('OOPS - There is an issue in your code.')
    #else:
   # print('Congrats ! Your implementation works !')

 

# pour tester

#try:
    #student = Student("Achille", "Talon")
    #student.add_grade("History", 10.)
    #student.add_grade("History", 12.)
    #try:
        #student.add_grade("History", 25.)
    #except ValueError:
        #pass
    #else:
        #raise Exception("a grade outside of [0, 20] should raise ValueError")
#except Exception as e:
    #print('OOPS - There is an issue in your add_grade method.')
    #print(f"Error message : {e}")
#else:
    #print('Congrats ! Your implementation works !')

# pour tester

#try:
    #student = Student("Achille", "Talon")
    #student.add_grade("History", 10.)
    #topics = student.followed_topics()
    #if len(topics) != 1 or "History" not in topics:
        #raise Exception(f"Expecting ['History'] got {topics}")
#except Exception as e:
    #print('OOPS - There is an issue in your followed_topics method')
    #print(f"Error message : {e}")
#else:
    #print('Congrats ! Your implementation works !')

# pour tester

#try:
    #student = Student("Achille", "Talon")
    #student.add_grade("History", 10.)
    #student.add_grade("History", 12.)
    #if (student.compute_average("History") != 11.):
        #raise Exception("Issue in your average calculation.")
    #try:
       # student.compute_average("French")
    #except ValueError:
        #pass
    #else:
        #raise Exception("If topic is not followed, a ValueError is expected")
    #if student.followed_topics() != ["History"]:
       # raise Exception(f"asking for the average of an unfollowed topic must not create it: {student.followed_topics()}")
#except Exception as e:
   # print('OOPS - There is an issue in your compute_average method.')
    #print(f"Error message : {e}")
#else:
    #print('Congrats ! Your implementation works !')




  


   
    

 




    
    