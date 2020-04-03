from body import Body

class Dog(Body):
    
    default_organ = 1

    def __init__(self, color='red', name='dog', rank='s', organ=None, distance_traveled=0, bark=True, **kwargs):
        if not organ:
            organ = self.default_organ
        initial = super().__init__(name=name, organ=organ, **kwargs)
        self.rank = rank
    
    def bark(self, distance):
        self.distance_traveled += distance
