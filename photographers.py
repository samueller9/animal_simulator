#def class - Photographer (user)
# attributes: bag (camera, lenses,)
# trying to take pictures of the endangered animals in each habititat
# you get to take 10 pictures per habitat, if you don't take the ones of the endangered ones, you lose
# randomly take pictures and hope you get a picture of an endangered species
# has a balance from selling pictures
# have different cameras/lenses

from photograph import Photograph

class Photographer:

    def __init__(self, name, camera):
        '''Instance properties:
            name: String
            camera: List
            catalog: List
            picture: String, Integer
            balance: Integer
        '''
        self.name = name
        self.camera = list()
        self.catalog = list()
        self.balance = 0

    def take_picture(self, picture):
        self.catalog.append(picture)

    # def camera(self):

    def catalog(self):
        self.catalog = []
        print(self.catalog)

    def balance(self):
        sum(self.catalog)
        # print(sum)

if __name__ == "__main__":
    print(sum)
