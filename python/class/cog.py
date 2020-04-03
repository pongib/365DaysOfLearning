from cat import Cat
from dog import Dog
from bacteria import Bacteria

class Cog(Cat, Bacteria, Dog):
    
    default_organ = 1

    def __init__(self, name='cog', organ=None, rank = 'S', **kwargs):
        # self.distance = distance
        if not organ:
            organ = self.default_organ
            
        print(f'{kwargs}')
        initial = super().__init__(name=name, organ=organ, **kwargs)        
        self.rank = rank

    def description(self):
        desc = super().description()
        print(f'Rank {self.rank} detail: {desc} cog.')

    def sound(self):
        self.meow(10)
        self.bark(15)


if __name__ == '__main__':
    cog = Cog(rank='S')
    cog.description()