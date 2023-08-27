
class NormalObject:

    a = 0  # byte
    aaa = []  # byte[]
    b = 0  # short
    c = 0  # int
    d = 0  # long
    e = 0.0  # float
    f = 0.0  # double
    g = False  # bool
    jj = ""  # string
    kk = None  # ObjectA
    l = []  # List<int>
    ll = []  # List<long>
    lll = []  # List<ObjectA>
    llll = []  # List<string>
    m = {}  # Dictionary<int, string>
    mm = {}  # Dictionary<int, ObjectA>
    s = {}  # HashSet<int>
    ssss = {}  # HashSet<string>

    def protocolId(self):
        return 101

    @classmethod
    def write(cls, buffer, packet):
        if buffer.writePacketFlag(packet):
            return
        buffer.writeByte(packet.a)
        if packet.aaa is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(len(packet.aaa))
            for element0 in packet.aaa:
                buffer.writeByte(element0)
        buffer.writeShort(packet.b)
        buffer.writeInt(packet.c)
        buffer.writeLong(packet.d)
        buffer.writeFloat(packet.e)
        buffer.writeDouble(packet.f)
        buffer.writeBool(packet.g)
        buffer.writeString(packet.jj)
        buffer.writePacket(packet.kk, 102)
        if packet.l is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(len(packet.l))
            for element1 in packet.l:
                buffer.writeInt(element1)
        if packet.ll is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(len(packet.ll))
            for element2 in packet.ll:
                buffer.writeLong(element2)
        if packet.lll is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(len(packet.lll))
            for element3 in packet.lll:
                buffer.writePacket(element3, 102)
        if packet.llll is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(len(packet.llll))
            for element4 in packet.llll:
                buffer.writeString(element4)
        if packet.m is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(len(packet.m))
            for key5 in packet.m:
                value6 = packet.m[key5]
                buffer.writeInt(key5)
                buffer.writeString(value6)
        if packet.mm is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(len(packet.mm))
            for key7 in packet.mm:
                value8 = packet.mm[key7]
                buffer.writeInt(key7)
                buffer.writePacket(value8, 102)
        if packet.s is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(len(packet.s))
            for element9 in packet.s:
                buffer.writeInt(element9)
        if packet.ssss is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(len(packet.ssss))
            for element10 in packet.ssss:
                buffer.writeString(element10)
        pass

    @classmethod
    def read(cls, buffer):
        if not buffer.readBool():
            return None
        packet = NormalObject()
        result11 = buffer.readByte()
        packet.a = result11
        result12 = []
        size14 = buffer.readInt()
        if size14 > 0:
            for index13 in range(size14):
                result15 = buffer.readByte()
                result12.append(result15)
        packet.aaa = result12
        result16 = buffer.readShort()
        packet.b = result16
        result17 = buffer.readInt()
        packet.c = result17
        result18 = buffer.readLong()
        packet.d = result18
        result19 = buffer.readFloat()
        packet.e = result19
        result20 = buffer.readDouble()
        packet.f = result20
        result21 = buffer.readBool() 
        packet.g = result21
        result22 = buffer.readString()
        packet.jj = result22
        result23 = buffer.readPacket(102)
        packet.kk = result23
        result24 = []
        size26 = buffer.readInt()
        if size26 > 0:
            for index25 in range(size26):
                result27 = buffer.readInt()
                result24.append(result27)
        packet.l = result24
        result28 = []
        size30 = buffer.readInt()
        if size30 > 0:
            for index29 in range(size30):
                result31 = buffer.readLong()
                result28.append(result31)
        packet.ll = result28
        result32 = []
        size34 = buffer.readInt()
        if size34 > 0:
            for index33 in range(size34):
                result35 = buffer.readPacket(102)
                result32.append(result35)
        packet.lll = result32
        result36 = []
        size38 = buffer.readInt()
        if size38 > 0:
            for index37 in range(size38):
                result39 = buffer.readString()
                result36.append(result39)
        packet.llll = result36
        result40 = {}
        size41 = buffer.readInt()
        if size41 > 0:
            for index42 in range(size41):
                result43 = buffer.readInt()
                result44 = buffer.readString()
                result40[result43] = result44
        packet.m = result40
        result45 = {}
        size46 = buffer.readInt()
        if size46 > 0:
            for index47 in range(size46):
                result48 = buffer.readInt()
                result49 = buffer.readPacket(102)
                result45[result48] = result49
        packet.mm = result45
        result50 = []
        size52 = buffer.readInt()
        if size52 > 0:
            for index51 in range(size52):
                result53 = buffer.readInt()
                result50.append(result53)
        packet.s = result50
        result54 = []
        size56 = buffer.readInt()
        if size56 > 0:
            for index55 in range(size56):
                result57 = buffer.readString()
                result54.append(result57)
        packet.ssss = result54
        return packet

