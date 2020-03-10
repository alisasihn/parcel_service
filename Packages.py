import csv
from PackageHashTable import *


class Package:
    package_list = []

    def __init__(self, package_id, address, city, state, postal, deadline, mass, special_notes, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.postal = postal
        self.deadline = deadline
        self.mass = mass
        self.special_notes = special_notes
        self.status = status

    def add_package(self, package):
        Package.package_list.append(package)

    def get_packages(self):
        return Package.package_list


with open('WGUPS_Package_File.csv', encoding='utf-8-sig') as package_csv:
    read_package = csv.reader(package_csv, delimiter=',')
    for row in read_package:
        read_package_id = row[0]
        read_address = row[1]
        read_city = row[2]
        read_state = row[3]
        read_postal = row[4]
        read_deadline = row[5]
        read_mass = row[6]
        read_special_notes = row[7]
        read_status = row[8]
        new_package = Package(read_package_id, read_address, read_city, read_state, read_postal, read_deadline, read_mass, read_special_notes, read_status)
        new_package.add_package(row)
