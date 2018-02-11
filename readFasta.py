with open('cel39.fa', 'rb') as fp:
    lines = fp.read().splitlines()

geneDict = {}

geneName = 'dummy'
fastaSeq = ''

for line in lines:
    if line[0] == '>':
        geneDict.update({geneName: fastaSeq})
        geneName = line[1:]
        fastaSeq = ''
    else:
        fastaSeq += line

geneDict.update({geneName: fastaSeq})
geneDict.pop('dummy')

print geneDict['name1']
