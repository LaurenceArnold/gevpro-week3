#!/usr/local/bin/python3

import sys
import xml.etree.ElementTree as ET

def main(argv):
    bestand=argv[1]
    output=argv[2]

    tree = ET.parse(bestand)
    root = tree.getroot()

    # vind via de points de bijhorende data
    for point in root.findall('POINT'):
        Bottom=int(point.find('BOTTOM_HZ').text)
        Top=int(point.find('TOP_HZ').text)
        Start=float(point.find('F0_START').text)
        End=float(point.find('F0_END').text)

        if (not Bottom <= Start <= Top) or (not Bottom <= End <= Top):
            root.remove(point)
    tree.write(output)


if __name__== "__main__":
    main(sys.argv)