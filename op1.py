#!/usr/local/bin/python3

import xml.etree.ElementTree as ET

def main():
    tree = ET.parse('spontal.xml')
    root = tree.getroot()