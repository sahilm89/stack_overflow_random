#!/usr/bin/env python
import sys
from xml.etree import ElementTree
from lxml import etree

def run(fileName):
    parser = etree.XMLParser(ns_clean=True)
    data = ElementTree.parse(fileName, parser).getroot()
    namespaces = data.nsmap
    namespaces['some_url'] = 'some_url'
    # Creating without duplicates here, which contains the unique list of elements determined by values of subelements
    for row in data.findall('.//SOAP:Body/some_url:Server_Reply', namespaces = namespaces):
        print row
        
if __name__ == "__main__":
    run(sys.argv[1])
