#!/usr/bin/env python
import sys
from xml.etree import ElementTree

def run(files):
    first = None
    for filename in files:
        data = ElementTree.parse(filename).getroot()
        if first is None:
            first = data
        else:
            first.extend(data)
    print first
    # Creating without duplicates here, which contains the unique list of elements determined by values of subelements
    withoutDuplicates = []
    if first is not None:
        for row in first.findall('row'):
            if ( row[0].text) in withoutDuplicates:
                first.remove(row) # Removing duplicate row
            else:
                withoutDuplicates.append(row[0].text)
        print ElementTree.tostring(first)
        
if __name__ == "__main__":
    run(sys.argv[1:])
