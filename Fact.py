
class Fact: 
    def __init__(self):
        self.faits = {}

    def addFact(self, faits, hint):
        for fact in faits :
            self.faits[fact] = hint

    
