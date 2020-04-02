from body import Body

class Bacteria(Body):
    
    default_organ = 1

    def __init__(self, name='bact', organ=None, rank='F'):
        if not organ:
            organ = self.default_organ
        initial = super().__init__(name, organ)
        self.rank = rank

    def description(self):
        desc = super().description()
        print(f'Rank {self.rank} detail: {desc}')


if __name__ == '__main__':
    bact = Bacteria(rank='S')
    bact.description()