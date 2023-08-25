import struct

maxSize = 655537
maxInt = 2147483647
minInt = -2147483648
maxLong = 9223372036854775807
minLong = -9223372036854775808


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

    def writeBool(self, value):
        if value:
            self.writeByte(1)
        else:
            self.writeByte(0)

    def readBool(self):
        if self.readByte():
            return True
        else:
            return False

    def writeByte(self, value):
        self.ensureCapacity(1)
        struct.pack_into('>b', self.buffer, self.writeOffset, value)
        self.writeOffset = self.writeOffset + 1

    def readByte(self):
        value = struct.unpack_from('>b', self.buffer, self.readOffset)[0]
        self.readOffset = self.readOffset + 1
        return value

    def writeUByte(self, value):
        self.ensureCapacity(1)
        struct.pack_into('>B', self.buffer, self.writeOffset, value)
        self.writeOffset = self.writeOffset + 1

    def readUByte(self):
        value = struct.unpack_from('>B', self.buffer, self.readOffset)[0]
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

    def writeInt(self, value):
        if not (minInt <= value <= maxInt):
            raise ValueError('value must range between minInt:-2147483648 and maxInt:2147483647')
        value = (value << 1) ^ (value >> 31)
        self.ensureCapacity(5)
        if value >> 7 == 0:
            self.writeUByte(value)
            return

        if value >> 14 == 0:
            self.writeUByte(value & 0x7F | 0x80)
            self.writeUByte((value >> 7) & 0x7F)
            return

        if value >> 21 == 0:
            self.writeUByte((value & 0x7F) | 0x80)
            self.writeUByte(((value >> 7) & 0x7F | 0x80))
            self.writeUByte((value >> 14) & 0x7F)
            return

        if value >> 28 == 0:
            self.writeUByte(value & 0x7F | 0x80)
            self.writeUByte(((value >> 7) & 0x7F | 0x80))
            self.writeUByte(((value >> 14) & 0x7F | 0x80))
            self.writeUByte((value >> 21) & 0x7F)
            return

        self.writeUByte(value & 0x7F | 0x80)
        self.writeUByte(((value >> 7) & 0x7F | 0x80))
        self.writeUByte(((value >> 14) & 0x7F | 0x80))
        self.writeUByte(((value >> 21) & 0x7F | 0x80))
        self.writeUByte((value >> 28) & 0x7F)
        pass

    def readInt(self):
        b = self.readUByte()
        value = b & 0x7F
        if (b & 0x80) != 0:
            b = self.readUByte()
            value |= (b & 0x7F) << 7
            if (b & 0x80) != 0:
                b = self.readUByte()
                value |= (b & 0x7F) << 14
                if (b & 0x80) != 0:
                    b = self.readUByte()
                    value |= (b & 0x7F) << 21
                    if (b & 0x80) != 0:
                        b = self.readUByte()
                        value |= (b & 0x7F) << 28
        return (value >> 1) ^ -(value & 1)

    def writeLong(self, value):
        if not (minLong <= value <= maxLong):
            raise ValueError('value must range between minLong:-9223372036854775808 and maxLong:9223372036854775807')
        value = (value << 1) ^ (value >> 63)
        self.ensureCapacity(9)
        if value >> 7 == 0:
            self.writeUByte(value)
            return

        if value >> 14 == 0:
            self.writeUByte(value & 0x7F | 0x80)
            self.writeUByte((value >> 7) & 0x7F)
            return

        if value >> 21 == 0:
            self.writeUByte((value & 0x7F) | 0x80)
            self.writeUByte(((value >> 7) & 0x7F | 0x80))
            self.writeUByte((value >> 14) & 0x7F)
            return

        if value >> 28 == 0:
            self.writeUByte(value & 0x7F | 0x80)
            self.writeUByte(((value >> 7) & 0x7F | 0x80))
            self.writeUByte(((value >> 14) & 0x7F | 0x80))
            self.writeUByte((value >> 21) & 0x7F)
            return
        if value >> 35 == 0:
            self.writeUByte(value & 0x7F | 0x80)
            self.writeUByte(((value >> 7) & 0x7F | 0x80))
            self.writeUByte(((value >> 14) & 0x7F | 0x80))
            self.writeUByte(((value >> 21) & 0x7F | 0x80))
            self.writeUByte((value >> 28) & 0x7F)
            return
        if value >> 42 == 0:
            self.writeUByte(value & 0x7F | 0x80)
            self.writeUByte(((value >> 7) & 0x7F | 0x80))
            self.writeUByte(((value >> 14) & 0x7F | 0x80))
            self.writeUByte(((value >> 21) & 0x7F | 0x80))
            self.writeUByte(((value >> 28) & 0x7F | 0x80))
            self.writeUByte((value >> 35) & 0x7F)
            return
        if value >> 49 == 0:
            self.writeUByte(value & 0x7F | 0x80)
            self.writeUByte(((value >> 7) & 0x7F | 0x80))
            self.writeUByte(((value >> 14) & 0x7F | 0x80))
            self.writeUByte(((value >> 21) & 0x7F | 0x80))
            self.writeUByte(((value >> 28) & 0x7F | 0x80))
            self.writeUByte(((value >> 35) & 0x7F | 0x80))
            self.writeUByte((value >> 42) & 0x7F)
            return
        if value >> 56 == 0:
            self.writeUByte(value & 0x7F | 0x80)
            self.writeUByte(((value >> 7) & 0x7F | 0x80))
            self.writeUByte(((value >> 14) & 0x7F | 0x80))
            self.writeUByte(((value >> 21) & 0x7F | 0x80))
            self.writeUByte(((value >> 28) & 0x7F | 0x80))
            self.writeUByte(((value >> 35) & 0x7F | 0x80))
            self.writeUByte(((value >> 42) & 0x7F | 0x80))
            self.writeUByte((value >> 49) & 0x7F)
            return
        self.writeUByte(value & 0x7F | 0x80)
        self.writeUByte(((value >> 7) & 0x7F | 0x80))
        self.writeUByte(((value >> 14) & 0x7F | 0x80))
        self.writeUByte(((value >> 21) & 0x7F | 0x80))
        self.writeUByte(((value >> 28) & 0x7F | 0x80))
        self.writeUByte(((value >> 35) & 0x7F | 0x80))
        self.writeUByte(((value >> 42) & 0x7F | 0x80))
        self.writeUByte(((value >> 49) & 0x7F | 0x80))
        self.writeUByte(value >> 56)
        pass

    def readLong(self):
        b = self.readUByte()
        value = b & 0x7F
        if (b & 0x80) != 0:
            b = self.readUByte()
            value |= (b & 0x7F) << 7
            if (b & 0x80) != 0:
                b = self.readUByte()
                value |= (b & 0x7F) << 14
                if (b & 0x80) != 0:
                    b = self.readUByte()
                    value |= (b & 0x7F) << 21
                    if (b & 0x80) != 0:
                        b = self.readUByte()
                        value |= (b & 0x7F) << 28
                        if (b & 0x80) != 0:
                            b = self.readUByte()
                            value |= (b & 0x7F) << 35
                            if (b & 0x80) != 0:
                                b = self.readUByte()
                                value |= (b & 0x7F) << 42
                                if (b & 0x80) != 0:
                                    b = self.readUByte()
                                    value |= (b & 0x7F) << 49
                                    if (b & 0x80) != 0:
                                        b = self.readUByte()
                                        value |= b << 56
        return (value >> 1) ^ -(value & 1)
