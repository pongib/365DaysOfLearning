class Body:
    """
    THis is body class
    """
    
    default_organ = 'cell'

    def __init__(self, name, organ):
        """
        Init class
        """
        self.name = name
        self.organ = organ

    @classmethod
    def bacteria(cls, name='Peter', organ=None):
        if not organ:
            organ = cls.default_organ
        return cls(name, organ)

    def printX(self):
        print('xxxxx')
        return 'THis is x'

    def lookup(self):
        print(f'Body name {self.name} and have {self.organ} organ. with {self.printX()}')