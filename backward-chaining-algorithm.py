import csv 
from Fact import Fact
from Rule import Rule
import logging
import copy


facts = Fact()
rules = Rule()


logging.basicConfig(filename='traces.log', level=logging.INFO,  format='%(message)s')

with open('BF1.txt', 'r') as BF :
    CSV_reader1 = csv.reader(BF, delimiter = ',')
    for line in CSV_reader1 : 
        facts.addFact(line, -1)

with open('BC1.txt', 'r') as BC :
    CSV_reader2 = csv.reader(BC, delimiter = ':')
    for line in  CSV_reader2 :
        rules.addRegle(line[0],line[1])


def testTout(but):
    found = False
    for value in rules.regles.values() :
        if but == value["CONCLUSION"] :
            found = True
    return found 
    

def butPrecis(but):
    reglesDeclenchées = []
    for key, value in rules.regles.items() :
        if but in value["CONCLUSION"] :
            reglesDeclenchées.append(key)
            tab = value["PREMISSES"].split(',')
            for i in range(len(tab)):
                if tab[i] in facts.faits.keys():
                    logging.info( tab[i]  +" premisse de la regle " + key + " ok")
                    facts.faits[value["CONCLUSION"]] =  key
                elif tab[i] not in facts.faits.keys() and testTout(tab[i]) == False:
                    logging.info( tab[i] +" premisse de la regle " + key  + " echec")
                else:
                    butPrecis(tab[i])
    logging.info("les regles declenchees :" + str(reglesDeclenchées))

response = input("donner un but   ")
butPrecis(response)
logging.info(facts.faits)
if response in facts.faits.keys() :
    logging.info("but atteint !!")
    print("but atteint !! ")
