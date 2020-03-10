class PackageHashTable:
    def __init__(self, initial_capacity=100):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # average = O(1); worst case = O(n)
    def insert(self, key, package):
        key = int(key)
        bucket_list = self.table[key]
        bucket_list.append(package)

    # average = O(1); worst case = O(n)
    def search(self, key):
        key = int(key)
        bucket_list = self.table[key]

        if key in bucket_list:
            item_index = bucket_list.index(key)
            return bucket_list[item_index]
        else:
            return None

    # average = O(1); worst case = O(n)
    def remove(self, key):
        key = int(key)
        bucket_list = self.table[key]

        if key in bucket_list:
            bucket_list.remove(key)
