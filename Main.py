# Alisa Sihn
# 001241143

from PackageHashTable import *
from Trucks import *

# add package objects to hash table
# O(n) for while loop
# average = O(1); worst case = O(n) for insert
new_package = Package(read_package_id, read_address, read_city, read_state, read_postal, read_deadline, read_mass,
                      read_special_notes, read_status)
package_list = new_package.get_packages()
package_table = PackageHashTable()
i = 1
j = 0
while i <= len(package_list):
    package_table.insert(i, package_list[j])
    i += 1
    j += 1


# CLI functions
# main menu
def main_menu():
    selection = input('Please type in your selection from these options: INSERT PACKAGE, START SIMULATION: ')
    menu_select(selection.lower())


# direct to other function after user selection
def menu_select(selection):
    if selection == 'insert package':
        insert_package()
    elif selection == 'start simulation':
        start_simulation()
    else:
        print('Selection was not valid - redirecting to main menu.')
        main_menu()


# insert new package
# O(n^2) overall
def insert_package():
    package_id = input(
        'Enter package ID or enter EXIT to exit to main menu. Please note that new packages will not be loaded on trucks and delivered today.: ')

    # if user enters nothing, restart insert_package
    if package_id.lower() == '':
        insert_package()

    # go back to main menu
    if package_id.lower() == 'exit':
        main_menu()

    # error handling for package ID to prevent collision
    package_id_exists = False
    x = 0
    while x < len(package_list) and not package_id_exists:
        if package_id == package_list[x][0]:
            package_id_exists = True
        x += 1
    if package_id_exists:
        print('Error: Package ID already exists.')
        insert_package()

    # if package ID is valid, begin gathering information for new package
    else:
        address = input('Enter street address: ')
        city = input('Enter city: ')
        state = input('Enter state abbreviation (e.g. UT): ')
        postal = input('Enter postal code: ')
        deadline = input('Enter delivery deadline in format HH24:MM (e.g. 14:15): ')
        mass = input('Enter weight of package in kg: ')
        special_notes = input('Enter special instructions (if applicable): ')
        status = ''
        ask_status = input('Is the package at the HUB? (YES/NO): ')
        if ask_status == 'yes':
            status = 'HUB'
        new_package_info = [package_id, address, city, state, postal, deadline, mass, special_notes, status]
        ins_package = Package(package_id, address, city, state, postal, deadline, mass, special_notes, status)
        ins_package.add_package(new_package_info)
        package_table.insert(package_id, new_package_info)
        new_package_list = ins_package.get_packages()
        print('Printing updated package list: ')
        for x in range(0, len(new_package_list)):
            print(new_package_list[x])
        main_menu()


# look for individual packages
# O(n^2) overall
def check_status():
    search_parameter = input('Please select the parameter you would like to use to search for packages - ID, STREET ADDRESS, CITY, POSTAL CODE, DEADLINE, WEIGHT, STATUS. Enter EXIT to go back.: ')

    # exit search
    if search_parameter.lower() == 'exit':
        start_simulation()

    # by ID
    elif search_parameter.lower() == 'id':
        search_input = input('Enter the ID of the package: ')
        print('Package with that ID found on truck 1: ')
        for x in range(0, len(truck1)):
            if search_input == truck1[x][0]:
                print(truck1[x])
        print('Package with that ID found on truck 2: ')
        for x in range(0, len(truck2)):
            if search_input == truck2[x][0]:
                print(truck2[x])
        print('Package with that ID found on truck 3: ')
        for x in range(0, len(truck3)):
            if search_input == truck3[x][0]:
                print(truck3[x])
        check_status()

    # by street address
    elif search_parameter.lower() == 'street address':
        search_input = input('Enter the street address of the package: ')
        print('Package with that street address found on truck 1: ')
        for x in range(0, len(truck1)):
            if search_input.lower() == truck1[x][1].lower():
                print(truck1[x])
        print('Package with that street address found on truck 2: ')
        for x in range(0, len(truck2)):
            if search_input.lower() == truck2[x][1].lower():
                print(truck2[x])
        print('Package with that street address found on truck 3: ')
        for x in range(0, len(truck3)):
            if search_input.lower() == truck3[x][1].lower():
                print(truck3[x])
        check_status()

    # by city
    elif search_parameter.lower() == 'city':
        search_input = input('Enter the city of the package: ')
        print('Package with that city found on truck 1: ')
        for x in range(0, len(truck1)):
            if search_input.lower() == truck1[x][2].lower():
                print(truck1[x])
        print('Package with that city found on truck 2: ')
        for x in range(0, len(truck2)):
            if search_input.lower() == truck2[x][2].lower():
                print(truck2[x])
        print('Package with that city found on truck 3: ')
        for x in range(0, len(truck3)):
            if search_input.lower() == truck3[x][2].lower():
                print(truck3[x])
        check_status()

    # by postal code
    elif search_parameter.lower() == 'postal code':
        search_input = input('Enter the postal code of the package: ')
        print('Package with that postal code found on truck 1: ')
        for x in range(0, len(truck1)):
            if search_input == truck1[x][4]:
                print(truck1[x])
        print('Package with that postal code found on truck 2: ')
        for x in range(0, len(truck2)):
            if search_input == truck2[x][4]:
                print(truck2[x])
        print('Package with that postal code found on truck 3: ')
        for x in range(0, len(truck3)):
            if search_input == truck3[x][4]:
                print(truck3[x])
        check_status()

    # by deadline
    elif search_parameter.lower() == 'deadline':
        search_input = input('Enter the deadline of the package in HH24:MM format or EOD if no deadline: ')
        print('Package with that deadline found on truck 1: ')
        for x in range(0, len(truck1)):
            if search_input.lower() == truck1[x][5].lower():
                print(truck1[x])
        print('Package with that deadline found on truck 2: ')
        for x in range(0, len(truck2)):
            if search_input.lower() == truck2[x][5].lower():
                print(truck2[x])
        print('Package with that deadline found on truck 3: ')
        for x in range(0, len(truck3)):
            if search_input.lower() == truck3[x][5].lower():
                print(truck3[x])
        check_status()

    # by weight
    elif search_parameter.lower() == 'weight':
        search_input = input('Enter the weight of the package: ')
        print('Package with that weight found on truck 1: ')
        for x in range(0, len(truck1)):
            if search_input == truck1[x][6]:
                print(truck1[x])
        print('Package with that weight found on truck 2: ')
        for x in range(0, len(truck2)):
            if search_input == truck2[x][6]:
                print(truck2[x])
        print('Package with that weight found on truck 3: ')
        for x in range(0, len(truck3)):
            if search_input == truck3[x][6]:
                print(truck3[x])
        check_status()

    # by status
    elif search_parameter.lower() == 'status':
        search_input = input('Enter the status of the package (HUB, In Transit, or Delivered: ')
        print('Package with that status found on truck 1: ')
        for x in range(0, len(truck1)):
            if search_input.lower() == truck1[x][8][0:9].lower():
                print(truck1[x])
        print('Package with that status found on truck 2: ')
        for x in range(0, len(truck2)):
            if search_input.lower() == truck2[x][8][0:9].lower():
                print(truck2[x])
        print('Package with that status found on truck 3: ')
        for x in range(0, len(truck3)):
            if search_input.lower() == truck3[x][8][0:9].lower():
                print(truck3[x])
        check_status()

    else:
        print('Not a valid option. Please try again.')
        check_status()


# start simulation
# O(n) overall
def start_simulation():
    input_time = input('Please enter the time you would like simulate to in HH24:MM (e.g. 14:15) format. Enter EXIT to exit to main menu. Enter SEARCH to look up individual packages.: ')

    # navigate back to main menu
    if input_time.lower() == 'exit':
        main_menu()

    # check status of individual packages
    if input_time.lower() == 'search':
        check_status()

    # proceed to simulation
    else:
        minutes = (int(input_time[:-3]) * 60 + int(input_time[-2:])) - 480
        if minutes <= 0:
            print('No trucks have yet to leave the HUB.')
            start_simulation()
        # truck 3 will not leave HUB until 9:05
        elif minutes >= 65:
            truck_route(truck1, 'HUB', minutes)
            truck_route(truck2, 'HUB', minutes)
            truck3_route(truck3, 'HUB', minutes)
            print('Status of truck 1 as of ' + input_time + ': ')
            for x in range(0, len(truck1)):
                print(truck1[x])
            print('Status of truck 2 as of ' + input_time + ': ')
            for x in range(0, len(truck2)):
                print(truck2[x])
            print('Status of truck 3 as of ' + input_time + ': ')
            for x in range(0, len(truck3)):
                print(truck3[x])
            start_simulation()
        else:
            truck_route(truck1, 'HUB', minutes)
            truck_route(truck2, 'HUB', minutes)
            print('Status of truck 1 as of ' + input_time + ': ')
            for x in range(0, len(truck1)):
                print(truck1[x])
            print('Status of truck 2 as of ' + input_time + ': ')
            for x in range(0, len(truck2)):
                print(truck2[x])
            print('Status of truck 3 as of ' + input_time + ': ')
            print('Truck 3 has not yet left the HUB')
            start_simulation()


# start CLI program
main_menu()
