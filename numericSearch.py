def main():

    with open('data.txt', 'r') as searchfile:
            for line in searchfile:
                line = line.strip()
                if ("Run=true") in line: # This works because Python checks this substring in the line.
                    firstSplit = line.split("Idle=")[1]
                    idleNum = int(firstSplit.split('\s')[0]) 
                    if (idleNum >=10): # This had to be changed as you are comparing integers while the data is still of type string.
                        print line

    return 0

if __name__ == '__main__':
    main()
