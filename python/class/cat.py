from body import Body

class Cat(Body):
    
    default_organ = 1

    def __init__(self, name='bact', organ=None, rank='F', distance_traveled=0, meow=True, **kwargs):
        if not organ:
            organ = self.default_organ
        initial = super().__init__(name=name, organ=organ, rank=rank, **kwargs)
        self.rank = rank

    def meow(self, distance):
        self.distance_traveled += distance
