

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class BinaryReader:
    """"
    A reader for binary files, with some extra methods.
    """

    def __init__(self, path):
        self.f = open(path, "rb", buffering=0)
        assert self.f.readable()

    def readBoolean(self):
        foobool = self.f.read(1)
        return bool(foobool)

    def readChar(self, r=8):
        foochar = self.f.read(r)
        return chr(foochar)

    def readByte(self, r=8):
        return self.f.read(r)

    def readShort(self, r=16):
        return int(self.f.read(r))

    def readInt(self, r=32):
        return int(self.f.read(r))

    def readDouble(self, r=64):
        return float(self.f.read(r))

    def readLong(self, r=64):
        return float(self.f.read(r))

    def isEmpty(self):
        return self.f.readable()

    def close(self):
        self.f.close()


class BinaryWriter():
    def __init__(self, path):
        self.w = open(path, "wb", buffering=0)
        assert self.w.writable()

    def writeBool(self, boolean):
        if boolean:
            self.w.write(1)
        else:
            self.w.write(0)

    def writeChar(self, c):
        self.w.write(c)

    def writeByte(self, b, r=8):
        self.w.write(b)

    def writeShort(self, s,  r=16):
        self.w.write(s)

    def writeInt(self, i,  r=32):
        self.w.write(i)

    def writeDouble(self, d,  r=64):
        self.w.write(d)

    def writeLong(self, l, r=64):
        self.w.write(l)

    def close(self):
        self.w.close()
