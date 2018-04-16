import re
import csv

##########################################################




##########################################################



BuildingDictionary = {}
with open("combined.csv", 'r') as dictfile:
    csvreader = csv.reader(dictfile)
    for line in csvreader:
        key = line[0]
        value = ((line[1],line[2]))
        #print (key + ',' + val)
        BuildingDictionary[key] = value


with open("rosters.csv" , 'r') as numfile:
    csvread = csv.reader(numfile)
    for line in csvread:
        test = 0
        if line[1] in BuildingDictionary:
            line2 = '{},{},{},{}'.format(line[0],line[1],BuildingDictionary[line[1]][0],BuildingDictionary[line[1]][1])
            print (line2)
        else:
            print (line)

