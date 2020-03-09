class EmptyBucket:
    pass


# create hash table class for package information
class PackageHashTableLinear:
    def __init__(self, initial_capacity=40):
        self.EMPTY_SINCE_START = EmptyBucket()
        self.EMPTY_AFTER_REMOVAL = EmptyBucket()
        self.table = [self.EMPTY_SINCE_START] * initial_capacity

    def insert(self, key, package):
        bucket = hash(key) % len(self.table)
        buckets_probed = 0
        while buckets_probed < len(self.table):
            # add package to bucket
            if type(self.table[bucket]) is EmptyBucket:
                self.table[bucket] = package
                return True

            # bucket is not empty, go the next bucket
            bucket = (bucket + 1) % len(self.table)
            buckets_probed = buckets_probed + 1

        # was not able to insert package
        return False

    def search(self, key):
        bucket = hash(key) % len(self.table)
        buckets_probed = 0
        while self.table[bucket] is not self.EMPTY_SINCE_START and buckets_probed < len(self.table):
            if self.table[bucket] == key:
                return self.table[bucket]

            bucket = (bucket + 1) % len(self.table)
            buckets_probed = buckets_probed + 1

        # not found
        return None

    def remove(self, key):
        bucket = hash(key) % len(self.table)
        buckets_probed = 0
        while self.table[bucket] is not self.EMPTY_SINCE_START and buckets_probed < len(self.table):
            if self.table[bucket] == key:
                self.table[bucket] = self.EMPTY_AFTER_REMOVAL

            bucket = (bucket + 1) % len(self.table)
            buckets_probed = buckets_probed + 1
