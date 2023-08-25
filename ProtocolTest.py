# encoding: UTF-8

from unittest import TestCase
import struct

import protocol.buffer.byte_buffer as byte_buffer


def print_bytearray(bytes):
    for byte in bytes:
        print(byte)  # 以字节形式输出每个字节的值


class ByteBufferTestCase(TestCase):
    def test_bytearray(self):
        buffer = bytearray(10)
        for byte in buffer:
            print(byte)  # 以字节形式输出每个字节的值

    def test_buffer(self):
        byteBuffer = byte_buffer.ByteBuffer()
        print(byteBuffer.writeOffset)
        print(byteBuffer.readOffset)
        print(byteBuffer.getCapacity())
        byteBuffer.writeByte(-100)
        self.assertEqual(byteBuffer.readByte(), -100)
        byteBuffer.writeShort(256)
        self.assertEqual(byteBuffer.readShort(), 256)

        print("----------------------------------------------------------------")
        print_bytearray(byteBuffer.buffer)
