#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name='Fido', breed='Mastiff'):
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)

#     def  __init__(self, name):
#         self.name = name
#         # if breed in APPROVED_BREEDS:
#         #     self.breed = breed
#         # else:
#         #     print(f'{breed} must be in list of approved breeds.')
 
#         if self.name == "":
#             print("Name must be string between 1 and 25 characters.")
#         elif self.name != "":
#             print("Name must be string between 1 and 25 characters.") 
#         elif self.name > 25 :
#             print("Name must be string between 1 and 25 characters.") 
#         else:
#             print(f"{self.name}")
          
# puppy = Dog("Rusty")
# print(f"{puppy.name}")

