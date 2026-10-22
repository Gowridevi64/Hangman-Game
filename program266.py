class Animal:
    def sound(self):
        print("Animalsound")
        
class Dog(Animal):
    def sound(self):
        print("Bark")
        
dog = Dog()
dog.sound()
