import csv
from DistanceGraph import *


headerList = []
# create instance of Graph class
g = Graph()
# create empty dictionary for distance data
distanceDict = {}

# import package information from csv
with open('WGUPS_Distance_Table.csv', encoding='utf-8-sig') as distance_csv:
    readDistance = csv.reader(distance_csv, delimiter=',')
    # grab headers from first row of csv
    headers = next(readDistance)[1:]
    # add nodes to graph
    for header in headers:
        g.add_vertex(header)
        headerList.append(header)

    # add distance data to dictionary
    for row in readDistance:
        distanceDict[row[0]] = {key: value for key, value in zip(headers, row[1:])}

    # add edges to graph
    i = 0
    j = 0
    while j < len(headerList):
        g.add_undirected_edge(headerList[i], headerList[j], distanceDict[headerList[i]][headerList[j]])
        j += 1

    # printing to check the data
    print(distanceDict)
    print(distanceDict['1330 2100 S (84106)']['HUB'])
    print(distanceDict['HUB']['1330 2100 S (84106)'])
    print(g.adjacency_list)
    print(g.edge_weights)
