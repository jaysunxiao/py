import struct

class ByteBuffer(object):

    writeOffset = 0
    readOffset = 0
    buffer = bytearray(64)