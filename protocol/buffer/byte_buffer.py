import struct


maxSize = 655537

class ByteBuffer():
    writeOffset = 0
    readOffset = 0
    buffer = bytearray(8)

    def setWriteOffset(self, writeOffset):
        if writeOffset > len(self.buffer):
            raise ValueError("index out of bounds exception:readerIndex:" + str(self.readOffset) +
                             ", writerIndex:" + str(self.writeOffset) +
                             "(expected:0 <= readerIndex <= writerIndex <= capacity:" + str(len(self.buffer)))
        self.writeOffset = writeOffset

    def setReadOffset(self, readOffset):
        if readOffset > self.writeOffset:
            raise ValueError("index out of bounds exception:readerIndex:" + str(self.readOffset) +
                             ", writerIndex:" + str(self.writeOffset) +
                             "(expected:0 <= readerIndex <= writerIndex <= capacity:" + str(len(self.buffer)))
        self.readOffset = readOffset

    def getCapacity(self):
        return len(self.buffer) - self.writeOffset


    def ensureCapacity(self, minCapacity):
        while (minCapacity - self.getCapacity() > 0):
            newSize = len(self.buffer) * 2
            if newSize > maxSize:
                raise ValueError("out of memory error")
            # auto grow capacity
            self.buffer.extend(bytearray(len(self.buffer)))

    def writeByte(self, value):
        self.ensureCapacity(1)
        struct.pack_into('>b', self.buffer, self.writeOffset, value)
        self.writeOffset = self.writeOffset + 1

    def readByte(self):
        value = struct.unpack_from('>b', self.buffer, self.readOffset)[0]
        self.readOffset = self.readOffset + 1
        return value

    def writeShort(self, value):
        self.ensureCapacity(1)
        struct.pack_into('>h', self.buffer, self.writeOffset, value)
        self.writeOffset = self.writeOffset + 2

    def readShort(self):
        value = struct.unpack_from('>h', self.buffer, self.readOffset)[0]
        self.readOffset = self.readOffset + 2
        return value