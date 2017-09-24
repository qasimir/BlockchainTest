import hashlib

class Block:

    def __init__(self, index, prev_hash, timestamp, data):
        self.index = index
        self.prevHash = prev_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash(index, prev_hash, timestamp, data)

    def calculate_hash(self, index, prev_hash, timestamp, data):
        return hashlib.sha3_256("{}{}{}{}".format(str(index), str(prev_hash), str(timestamp), str(data)))





