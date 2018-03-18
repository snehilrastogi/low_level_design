class Cache:
    def __init__(self, level, read_time, write_time, capacity=10):
        self.level = level
        self.read_time = read_time
        self.write_time = write_time
        self.capacity = capacity
        self.data_list = []