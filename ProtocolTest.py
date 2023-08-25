# encoding: UTF-8

from unittest import TestCase
import struct

class ByteBufferTestCase(TestCase):
    def test_bytearray(self):
        buffer = bytearray(10)
        for byte in buffer:
            print(byte)  # 以字节形式输出每个字节的值
