from Crypto.Hash import MD5

class Hashing (object):
    def __init__(self, string):
        #repr - convert string to byte code
        self.hash = MD5.new(repr(string))

    #return hex values as string
    def __str__(self):
        return str(self.hash.hexdigest())
