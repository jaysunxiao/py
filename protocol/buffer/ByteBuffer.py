import struct


class ByteBuffer(object):
    writeOffset = 0
    readOffset = 0
    buffer = bytearray(64)

    def setWriteOffset(self, writeOffset):
        if self.writeOffset > len(self.buffer):
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
