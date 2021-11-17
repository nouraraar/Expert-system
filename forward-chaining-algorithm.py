import csv 
from Fact import Fact
from Rule import Rule
import logging
import copy


facts = Fact()
rules = Rule()


logging.basicConfig(filename='traces.log', level=logging.INFO,  format='%(message)s')

with open('BF2.txt', 'r') as BF :
    CSV_reader1 = csv.reader(BF, delimiter = ',')
    for line in CSV_reader1 : 
        facts.addFact(line, -1)

with open('BC2.txt', 'r') as BC :
    CSV_reader2 = csv.reader(BC, delimiter = ':')
    for line in  CSV_reader2 :
        rules.addRegle(line[0],line[1])

def butPrecis(but, facts, test):
    newRules = copy.deepcopy(test)

    for key, value in test.items() :
        tab = value["PREMISSES"].split(',')
        for i in range(len(tab)):
            if tab[i] not in facts.faits.keys():
                break 
            elif i == len(tab)-1 and tab[i] in facts.faits.keys():
                facts.faits[value["CONCLUSION"]] = key 
                logging.info("rule number  "+ key + "  is used")
                logging.info(facts.faits)
                del newRules[key]

    if but in facts.faits.keys() :
        print("but atteint") 
        logging.info("but atteint !!")
    else :
        butPrecis(but, facts, newRules)
    
def saturation(facts, test):
    newRules = copy.deepcopy(test)
    saturée = True

    for key, value in test.items() :
        tab = value["PREMISSES"].split(',')
        print(tab)
        print(facts.faits)
        for i in range(len(tab)):
            if tab[i] not in facts.faits.keys():
                break 
            elif i == len(tab)-1 and tab[i] in facts.faits.keys():
                facts.faits[value["CONCLUSION"]] = key 
                logging.info("rule number  "+ key + "  is used")
                logging.info(facts.faits)
                del newRules[key]
                logging.info(newRules)
                saturée = False
    if saturée == True :
        print("la base est saturée")
    else :
        saturation(facts, newRules)
    


response = input("choisir une strategie => 1 : saturer la base ou 2 : but precis   ")

if int(response) == 2 : 
    but = input("donner un but ")
    butPrecis(but, facts, rules.regles)
elif int(response) == 1 :
    saturation(facts, rules.regles)
else :
    print("choose between option 1 and 2")



