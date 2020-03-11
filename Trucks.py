from math import floor

from Packages import *
from Distances import *

# create instance of Package class
new_package = Package(read_package_id, read_address, read_city, read_state, read_postal, read_deadline, read_mass,
                      read_special_notes, read_status)

# get all packages
package_list = new_package.get_packages()

# manually load truck 1
truck1 = [package_list[0], package_list[6], package_list[7], package_list[12], package_list[13], package_list[14],
          package_list[15], package_list[18], package_list[19], package_list[20], package_list[28], package_list[29],
          package_list[30], package_list[33], package_list[36], package_list[39]]

# manually load truck 2
truck2 = [package_list[1], package_list[2], package_list[3], package_list[4], package_list[9], package_list[10],
          package_list[17], package_list[21], package_list[22], package_list[23], package_list[26], package_list[32],
          package_list[34], package_list[35], package_list[37], package_list[38]]

# manually load truck 3
truck3 = [package_list[5], package_list[8], package_list[11], package_list[16], package_list[24], package_list[25],
          package_list[27], package_list[31]]


# change status of packages on departed truck to 'In Transit'
def in_transit(truck):
    for z in range(0, len(truck)):
        truck[z][8] = 'In Transit'


# change status of package to 'Delivered HH24:MM'
# O(n^2)
def package_delivered(truck, distance_traveled, location):
    # calculate the time of delivery
    elapsed_time = distance_traveled * (1 / 18) * 60
    delivered_hour = floor(elapsed_time / 60) + 8
    delivered_minute = str(round(elapsed_time % 60))
    if len(delivered_minute) == 1:
        delivered_minute = '0' + delivered_minute
    delivered_time = str(delivered_hour) + ':' + delivered_minute

    # parse the location to split into address and zip
    location_address = (location.split('(')[0]).rstrip()
    location_postal = (location.split('(')[1]).split(')')[0]
    for z in range(0, len(truck)):
        if location_address == truck[z][1] and location_postal == truck[z][4]:
            truck[z][8] = 'Delivered at ' + delivered_time


# truck 3 leaves HUB at different time
# O(n^2)
def package_delivered_truck3(truck, distance_traveled, location):
    # calculate the time of delivery
    elapsed_time = distance_traveled * (1 / 18) * 60
    delivered_hour = floor(elapsed_time / 60) + 9
    delivered_minute = str(round(elapsed_time % 60) + 5)
    if len(delivered_minute) == 1:
        delivered_minute = '0' + delivered_minute
    delivered_time = str(delivered_hour) + ':' + delivered_minute

    # parse the location to split into address and zip
    location_address = (location.split('(')[0]).rstrip()
    location_postal = (location.split('(')[1]).split(')')[0]
    for z in range(0, len(truck)):
        if location_address == truck[z][1] and location_postal == truck[z][4]:
            truck[z][8] = 'Delivered at ' + delivered_time


# map truck route
# O(n^2) overall
def truck_route(truck, current_vertex, time):
    in_transit(truck)
    dest_queue = []
    x = 0
    # these are all the stops the truck has to make
    # O(n)
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

    dist_traveled = float(0.0)
    dist_limit = float((time / 60) * 18)
    stop = False

    # go through the queue and create a route
    # outer loop = O(n), inner loop = O(n) -> O(n^2)
    while len(dest_queue) > 0 and not stop:
        index = 0
        # find adjacent vertex with shortest distance
        for y in range(0, len(dest_queue)):
            if float(distance_dict[current_vertex][dest_queue[y]]) < float(
                    distance_dict[current_vertex][dest_queue[index]]):
                index = y
        prev_vertex = current_vertex
        current_vertex = dest_queue[index]
        dist_traveled = float(dist_traveled) + float(distance_dict[prev_vertex][current_vertex])
        if dist_traveled <= dist_limit:
            package_delivered(truck, dist_traveled, current_vertex)
            current_vertex = dest_queue.pop(index)
        else:
            dist_traveled = dist_traveled - float(distance_dict[prev_vertex][current_vertex])
            stop = True

    print('Total distance traveled so far for one of the trucks: ' + str(round(dist_traveled, 1)) + ' miles')


# map truck route for truck 3
# O(n^2) overall
def truck3_route(truck, current_vertex, time):
    # correct delivery address for package #9 is received at 10:20
    if time >= 140:
        truck3[1][1] = '410 S State St'
        truck3[1][2] = 'Salt Lake City'
        truck3[1][3] = 'UT'
        truck3[1][4] = '84111'

    in_transit(truck)
    dest_queue = []
    x = 0
    # these are all the stops the truck has to make
    # O(n)
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

    path = []
    dist_traveled = float(0.0)
    dist_limit = float((time / 60) * 18)
    stop = False

    # go through the queue and create a route
    # outer loop = O(n), inner loop = O(n) -> O(n^2)
    while len(dest_queue) > 0 and not stop:
        index = 0
        # find adjacent vertex with shortest distance
        for y in range(0, len(dest_queue)):
            if float(distance_dict[current_vertex][dest_queue[y]]) < float(
                    distance_dict[current_vertex][dest_queue[index]]):
                index = y
        prev_vertex = current_vertex
        current_vertex = dest_queue[index]
        dist_traveled = float(dist_traveled) + float(distance_dict[prev_vertex][current_vertex])
        if dist_traveled <= dist_limit:
            package_delivered_truck3(truck, dist_traveled, current_vertex)
            path.append(current_vertex)
            current_vertex = dest_queue.pop(index)
        else:
            dist_traveled = dist_traveled - float(distance_dict[prev_vertex][current_vertex])
            stop = True

    print('Total distance traveled so far for one of the trucks: ' + str(round(dist_traveled, 1)) + ' miles')
