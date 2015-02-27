#!/usr/local/bin/python3

import json
from collections import namedtuple

def main():
    data=open('blood-die.json','r')
    bestand=json.load(data)
    outputfile=open('test.json','w')

    resultaat=namedtuple('resultaat',('Taal','Classificatie','bloed','sterven'))

    for taal in bestand:
        resultaat2=resultaat(taal[0],taal[1],taal[2],taal[3])
        bloed=resultaat2.bloed.split()
        sterven=resultaat2.sterven.split()
        [json.dump(taal,outputfile) for i in bloed if i in sterven]

    data.close()
    outputfile.close()

if __name__== "__main__":
    main()