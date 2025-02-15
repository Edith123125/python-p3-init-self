#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed


fido = Dog("Fido", "Golden Retriever")
print(fido.name)  
print(fido.breed) 

buddy = Dog("Buddy")
print(buddy.name)  
print(buddy.breed) 
