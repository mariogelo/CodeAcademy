"""

Add a method, description, to your Animal class.
Using two separate print statements, it should print out the name and age of the animal it's called on.
Then, create an instance of Animal, hippo (with whatever name and age you like), and call its description method.

Hint
Remember to pass self as an argument to description. Otherwise, printing self.name and self.age won't work, since Python won't know which self (that is, which object) you're talking about!

Your method should look something like this:

def description(self):
    print self.name
    print self.age
After that, all you need to do is create a hippo and call its description method with hippo.description()!
Q&A Forum

"""
class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print self.name
        print self.age

hippo = Animal("Don", 24)
hippo.description()
