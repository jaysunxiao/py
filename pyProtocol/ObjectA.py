
class ObjectA:

    a = 0  # int
    m = {}  # Dictionary<int, string>
    objectB = None  # ObjectB

    def protocolId(self):
        return 102

    @classmethod
    def write(cls, buffer, packet):
        if buffer.writePacketFlag(packet):
            return
        buffer.writeInt(packet.a)
        if packet.m is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(len(packet.m))
            for key0 in packet.m:
                value1 = packet.m[key0]
                buffer.writeInt(key0)
                buffer.writeString(value1)
        buffer.writePacket(packet.objectB, 103)
        pass

    @classmethod
    def read(cls, buffer):
        if not buffer.readBool():
            return None
        packet = ObjectA()
        result2 = buffer.readInt()
        packet.a = result2
        result3 = {}
        size4 = buffer.readInt()
        if size4 > 0:
            for index5 in range(size4):
                result6 = buffer.readInt()
                result7 = buffer.readString()
                result3[result6] = result7
        packet.m = result3
        result8 = buffer.readPacket(103)
        packet.objectB = result8
        return packet

