
class ObjectB():

    flag = False # bool

    def protocolId(self):
        return 103

    @classmethod
    def write(cls, buffer, packet):
        if (buffer.writePacketFlag(packet)):
            return
        buffer.writeBool(packet.flag)

    @classmethod
    def read(cls, buffer):
        var result0 = buffer.readBool() 
        packet.flag = result0
        pass