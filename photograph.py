#def class - Photograph
#sell Photograph
#price depends on what animal is captured in photograph, (endangered or not)
#amount of money goes into photographers balance
#different photographers make different amounts based on luck of what they see

import random
# from photographers import Photographer
from animals import Animal

class Photograph:

    def __init__(self, name, id, value):
        '''Instance properties:
            name: String
            id: Integer
            value: Integer
        '''
        self.name = name
        self.id = id
        self.value = value

    def take_photo(self):
        photo_id = 0
        for photo in self.id:
            photo_id += 1
        return photo_id

    def photo_id(self, id):
        self.catalog.append(self.id)

    # def photo_value(self):
    #     value =

if __name__ == "__main__":
    print(())
