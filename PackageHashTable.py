# create direct hash table class for package information
# average = O(1); worst case = O(n) for insert, delete, search
class PackageHashTable:
    def __init__(self, initial_capacity=41):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, package):
        bucket = hash(key)
        bucket_list = self.table[bucket]
        bucket_list.append(package)

    def search(self, key):
        bucket = hash(key)
        bucket_list = self.table[bucket]

        if key in bucket_list:
            item_index = bucket_list.index(key)
            return bucket_list[item_index]
        else:
            return None

    def remove(self, key):
        bucket = hash(key)
        bucket_list = self.table[bucket]

        if key in bucket_list:
            bucket_list.remove(key)
