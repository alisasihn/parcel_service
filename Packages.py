import csv
from PackageHashTable import PackageHashTable

# import package information from csv
# with open('WGUPS_Package_File.csv', encoding='utf-8-sig') as package_csv:
#     readPackage = csv.reader(package_csv, delimiter=',')
#     packageTable = PackageHashTable()
#     numRows = 0
#     for row in readPackage:
#         numRows +=1
#         package_id = row[0]
#         address = row[1]
#         city = row[2]
#         state = row[3]
#         postal = row[4]
#         deadline = row[5]
#         mass = row[6]
#         special_notes = row[7]
#         status = row[8]
#         package_info = package_id, address, city, state, postal, deadline, mass, special_notes, status
#         packageTable.insert(int(package_id), package_info)
#
#     # printing hash table to see the data
#     i = 1
#     while i <= numRows:
#         print(packageTable.table[i])
#         i += 1

# create empty dictionary to add package information
packageDict = {}
# create instance of PackageHashTable class
packages = PackageHashTable()

#import package information from csv file
with open('WGUPS_Package_File.csv', encoding='utf-8-sig') as package_csv:
    readPackage = csv.DictReader(package_csv, delimiter=',')
    i = 1
    for row in readPackage:
        packageDict[i] = row
        packages.insert(i, row)
        i += 1

    # printing to check the data in the dictionary
    x = 1
    while x < 41:
        print(packageDict[x])
        x += 1
