# define class - Animal
# def init w/ instances
# def list of animals
# endangered or not
# color/size/age
# habitat they live in


class Animal:

    def __init__(self,name,habitat,endangered):
        '''Instance properties:
            name: String
            habitat: String
            endangered: Integer
        '''
        self.name = name
        self.habitat = habitat
        self.endangered = endangered

animals = [
    Animal('Armadillo','desert',False),
    Animal('Camel','desert',False),
    Animal('Coyote','desert',False),
    Animal('Desert Shrew','desert',False),
    Animal('Vulture','desert',False),
    Animal('Desert Tortoise','desert',True),
    Animal('Lion','jungle',False),
    Animal('Elephant','jungle',False),
    Animal('Sloth','jungle',False),
    Animal('Jaguar','jungle',False),
    Animal('Sloth Bear','jungle',False),
    Animal('Bengal Tiger','jungle',True),
    Animal('Cougar','mountains',False),
    Animal('Mountain Goat','mountains',False),
    Animal('Brown Bear','moutains',False),
    Animal('Wolf','mountains',False),
    Animal('Marmot','mountains',False),
    Animal('Bighorn Sheep','mountains',True),
    Animal('Great White Shark','ocean',False),
    Animal('Blue Whale','ocean',False),
    Animal('Sea Turtle','ocean',False),
    Animal('Octopus','ocean',False),
    Animal('Seal','ocean',False),
    Animal('Clown Fish','ocean',True),
]

def get_animals_by_habitat(animals, habitat):
    animals = list(filter(lambda animal: (animal.habitat == habitat), animals))
    return animals

def list_animals(animals):
    for a in animals:
        print(a.name)



# photographs = []

if __name__ == "__main__":
    habitat = input("Choose a place you want to take pictures: desert, jungle, mountains, ocean: ")
    print("You have chosen " + habitat + "!")
    print("Here are the animals in the " + habitat + ":")
    animals = get_animals_by_habitat(animals, habitat)
    list_animals(animals)
    take_photo = input("Do you want to take a photo?")
    take_photo(self)
