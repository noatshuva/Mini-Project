class suspicious:
    def __init__(self, name, signature, size):
        self.name = name
        self.signature = signature
        self.size = size


# size 2 bytes, name 16 bytes,  signature $size bytes
def virus_list_from_file(file):
    virus_list = []
    with open(file, "rb") as fd:
        next2bytes = fd.read(2)
        while next2bytes:
            size = int.from_bytes(next2bytes, byteorder='little') - 18
            name = fd.read(16).decode("utf-8")
            signature = fd.read(size)
            v = suspicious(name, signature, size)
            virus_list.append(v)
            next2bytes = fd.read(2)
    return virus_list
