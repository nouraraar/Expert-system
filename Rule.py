
class Rule :
    def __init__(self):
        self.regles = {}
        
    def addRegle(self,numRegle,regle):
        if 'et' in  regle[3:regle.index('alors')] :
            self.regles[numRegle]= {"PREMISSES" : self.unpackList(regle[3:regle.index('alors')].split(' et ')),
                                    "CONCLUSION" : regle.split('alors')[-1].strip()}
        else:
            self.regles[numRegle] = {"PREMISSES" : regle[3:regle.index('alors')].strip() ,
                                     "CONCLUSION" : regle.split('alors')[-1].strip()}


    def unpackList(self,liste):
        chaine = ""
        for i in liste :
            chaine += i + ","
        return chaine[:-1].strip()


