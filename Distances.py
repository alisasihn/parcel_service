import csv
from DistanceGraph import *


header_list = []
# create instance of Graph class
dist_graph = Graph()
# create empty dictionary for distance data
distance_dict = {}

# import package information from csv
with open('WGUPS_Distance_Table.csv', encoding='utf-8-sig') as distance_csv:
    read_distance = csv.reader(distance_csv, delimiter=',')
    # grab headers from first row of csv
    headers = next(read_distance)[1:]
    # add nodes to graph
    for header in headers:
        dist_graph.add_vertex(header)
        header_list.append(header)
    # add distance data to dictionary
    for row in read_distance:
        distance_dict[row[0]] = {key: value for key, value in zip(headers, row[1:])}

    # add edges to graph
    i = 0
    j = 0
    while j < len(header_list):
        dist_graph.add_undirected_edge(header_list[i], header_list[j], float(distance_dict[header_list[i]][header_list[j]]))
        j += 1
