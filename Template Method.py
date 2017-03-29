
"""
Template Method en Python
Adaptado de:
http://jpython.blogspot.com.co/2012/11/design-pattern-in-python-template-method.html
"""
class MakeMeal:

    def prepare(self):  pass
    def cook(self): pass
    def eat(self):  pass

    def go(self):
        self.prepare()
        self.cook()
        self.eat()

class MakePizza(MakeMeal):

    def prepare(self):
        print "Prepare Pizza"

    def cook(self):
        print "Cook Pizza"

    def eat(self):
        print "Eat Pizza"

class MakeTea(MakeMeal):

    def prepare(self):
        print "Prepare Tea"

    def cook(self):
        print "Cook Tea"

    def eat(self):
        print "Eat Tea"


if __name__ == "__main__":

    m = new MakePizza();
    m.go()

    n = new MakeTea();
    n.go()
        

        
