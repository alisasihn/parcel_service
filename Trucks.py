import operator

from Packages import *
from Distances import *

new_package = Package(read_package_id, read_address, read_city, read_state, read_postal, read_deadline, read_mass,
                      read_special_notes, read_status)
package_list = new_package.get_packages()

# manually load truck 1
truck1 = [package_list[0], package_list[6], package_list[7], package_list[12], package_list[13], package_list[14],
          package_list[15], package_list[18], package_list[19], package_list[20], package_list[28], package_list[29],
          package_list[30], package_list[33], package_list[36], package_list[39]]

# manually load truck 2
truck2 = [package_list[1], package_list[2], package_list[3], package_list[4], package_list[9], package_list[10],
          package_list[17], package_list[21], package_list[22], package_list[23], package_list[26], package_list[32],
          package_list[34], package_list[35], package_list[37], package_list[38]]

# truck 3 will not be loaded until 9:05
truck3 = [package_list[5], package_list[8], package_list[11], package_list[16], package_list[24], package_list[25],
          package_list[27], package_list[31]]


# map truck route
def truck_route(truck, current_vertex):
    dest_queue = []
    x = 0
    # these are all the stops the truck has to make
    while x < len(truck):
        # extract address information from packages and manipulate to match address format in distance data
        street_address = truck[x][1]
        postal_code = truck[x][4]
        vertex_address = street_address + ' (' + postal_code + ')'
        # don't add duplicates
        if vertex_address in dest_queue:
            pass
        else:
            dest_queue.append(vertex_address)
        x += 1

    path = current_vertex
    dist_traveled = float(0.0)
    dist_traveled_str = ''

    # go through the queue and create a route
    # O(n^2)
    while len(dest_queue) > 0:
        index = 0
        # find adjacent vertex with shortest distance
        for y in range(0, len(dest_queue)):
            if float(distance_dict[current_vertex][dest_queue[y]]) < float(distance_dict[current_vertex][dest_queue[index]]):
                index = y
        prev_vertex = current_vertex
        current_vertex = dest_queue.pop(index)
        path = path + ' -> ' + current_vertex
        dist_traveled = float(dist_traveled) + float(distance_dict[prev_vertex][current_vertex])
        dist_traveled_str = dist_traveled_str + ' + ' + distance_dict[prev_vertex][current_vertex]

    print(path)
    print(round(dist_traveled, 2))


truck_route(truck1, 'HUB')
truck_route(truck2, 'HUB')
truck_route(truck3, 'HUB')

# dijkstra's algorithm
# def shortest_path(truck, graph, start_vertex):
#     unvisited_vertices = []
#     x = 0
#     while x < len(truck):
#         # extract address information from packages and manipulate to match address format in distance data
#         street_address = truck[x][1]
#         postal_code = truck[x][4]
#         vertex_address = street_address + ' (' + postal_code + ')'
#         # don't add duplicate vertices
#         if vertex_address in unvisited_vertices:
#             pass
#         else:
#             unvisited_vertices.append(Vertex(vertex_address))
#         x += 1
#
#     start_vertex.distance = 0
#
#     while len(unvisited_vertices) > 0:
#         smallest_index = 0
#         for y in range(1, len(unvisited_vertices)):
#             if unvisited_vertices[y].distance < unvisited_vertices[smallest_index].distance:
#                 smallest_index = y
#         current_vertex = unvisited_vertices.pop(smallest_index)
#
#         for adj_vertex in graph.adjacency_list[current_vertex]:
#             edge_weight = graph.edge_weights[(current_vertex, adj_vertex)]
#             alternative_path_distance = current_vertex.distance + edge_weight
#
#             if alternative_path_distance < adj_vertex.distance:
#                 adj_vertex.distance = alternative_path_distance
#                 adj_vertex.pred_vertex = current_vertex
#
#
# def get_shortest_path(start_vertex, end_vertex):
#     path = ''
#     current_vertex = end_vertex
#     while current_vertex is not start_vertex:
#         path = ' -> ' + str(current_vertex.label) + path
#         current_vertex = current_vertex.pred_vertex
#     path = start_vertex.label + path
#     return path
#
#
# start = Vertex('HUB')
# shortest_path(truck1, dist_graph, start)
#
# for v in sorted(dist_graph.adjacency_list, key=operator.attrgetter('label')):
#     if v.pred_vertex is None and v is not start:
#         print("A to %s: no path exists" % v.label)
#     else:
#         print("A to %s: %s (total weight: %g)" % (v.label, get_shortest_path(start, v), v.distance))
