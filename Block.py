import hashlib
from time import gmtime, strftime


class Block:

    def __init__(self, index, prev_hash, data):
        self.index = index
        self.prevHash = prev_hash
        self.timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        self.data = data
        self.hash = self.calculate_hash(index, prev_hash, data)

    def calculate_hash(self, index, prev_hash, data):
        byte_input = str(index)+ str(prev_hash)+ str(self.timestamp)+ str(data)
        return hashlib.sha3_256(byte_input.encode()).hexdigest()





