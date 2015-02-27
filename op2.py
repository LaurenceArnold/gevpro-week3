#!/usr/local/bin/python3
# opdracht 2 van gevorderd programmeren
# Gemaakt door Laurence Arnold op 27 februari 2015

import json
from collections import namedtuple

def main():
    data=open('blood-die.json','r')
    bestand=json.load(data)
    outputfile=open('blood_and_die_result.json','w')

    #maak een namedtuple
    resultaat=namedtuple('resultaat',('Taal','Classificatie','bloed','sterven'))

    for taal in bestand:
        # creeër voor de 4 velden een licht object en roep deze aan
        resultaat2=resultaat(taal[0],taal[1],taal[2],taal[3])
        bloed=resultaat2.bloed.split()
        sterven=resultaat2.sterven.split()
        [json.dump(taal,outputfile) for i in bloed if i in sterven]

    data.close()
    outputfile.close()

if __name__== "__main__":
    main()