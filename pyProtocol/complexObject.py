# 复杂的对象，包括了各种复杂的结构，数组，List，Set，Map
class ComplexObject:

    # byte类型，最简单的整形
    a = 0  # byte
    # byte的包装类型，优先使用基础类型，包装类型会有装箱拆箱
    aa = 0  # byte
    # 数组类型
    aaa = []  # byte[]
    aaaa = []  # byte[]
    b = 0  # short
    bb = 0  # short
    bbb = []  # short[]
    bbbb = []  # short[]
    c = 0  # int
    cc = 0  # int
    ccc = []  # int[]
    cccc = []  # int[]
    d = 0  # long
    dd = 0  # long
    ddd = []  # long[]
    dddd = []  # long[]
    e = 0.0  # float
    ee = 0.0  # float
    eee = []  # float[]
    eeee = []  # float[]
    f = 0.0  # double
    ff = 0.0  # double
    fff = []  # double[]
    ffff = []  # double[]
    g = False  # bool
    gg = False  # bool
    ggg = []  # bool[]
    gggg = []  # bool[]
    h = ""  # char
    hh = ""  # char
    hhh = []  # char[]
    hhhh = []  # char[]
    jj = ""  # string
    jjj = []  # string[]
    kk = None  # ObjectA
    kkk = []  # ObjectA[]
    l = []  # List<int>
    ll = []  # List<List<List<int>>>
    lll = []  # List<List<ObjectA>>
    llll = []  # List<string>
    lllll = []  # List<Dictionary<int, string>>
    m = {}  # Dictionary<int, string>
    mm = {}  # Dictionary<int, ObjectA>
    mmm = {}  # Dictionary<ObjectA, List<int>>
    mmmm = {}  # Dictionary<List<List<ObjectA>>, List<List<List<int>>>>
    mmmmm = {}  # Dictionary<List<Dictionary<int, string>>, HashSet<Dictionary<int, string>>>
    s = {}  # HashSet<int>
    ss = {}  # HashSet<HashSet<List<int>>>
    sss = {}  # HashSet<HashSet<ObjectA>>
    ssss = {}  # HashSet<string>
    sssss = {}  # HashSet<Dictionary<int, string>>
    # 如果要修改协议并且兼容老协议，需要加上Compatible注解，按照增加的顺序添加order
    myCompatible = 0  # int
    myObject = None  # ObjectA

    def protocolId(self):
        return 100

    @classmethod
    def write(cls, buffer, packet):
        if buffer.writePacketFlag(packet):
            return
        buffer.writeByte(packet.a)
        buffer.writeByte(packet.aa)
        if packet.aaa is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.aaa.size())
            for element0 in packet.aaa:
                buffer.writeByte(element0)
        if packet.aaaa is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.aaaa.size())
            for element1 in packet.aaaa:
                buffer.writeByte(element1)
        buffer.writeShort(packet.b)
        buffer.writeShort(packet.bb)
        if packet.bbb is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.bbb.size())
            for element2 in packet.bbb:
                buffer.writeShort(element2)
        if packet.bbbb is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.bbbb.size())
            for element3 in packet.bbbb:
                buffer.writeShort(element3)
        buffer.writeInt(packet.c)
        buffer.writeInt(packet.cc)
        if packet.ccc is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.ccc.size())
            for element4 in packet.ccc:
                buffer.writeInt(element4)
        if packet.cccc is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.cccc.size())
            for element5 in packet.cccc:
                buffer.writeInt(element5)
        buffer.writeLong(packet.d)
        buffer.writeLong(packet.dd)
        if packet.ddd is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.ddd.size())
            for element6 in packet.ddd:
                buffer.writeLong(element6)
        if packet.dddd is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.dddd.size())
            for element7 in packet.dddd:
                buffer.writeLong(element7)
        buffer.writeFloat(packet.e)
        buffer.writeFloat(packet.ee)
        if packet.eee is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.eee.size())
            for element8 in packet.eee:
                buffer.writeFloat(element8)
        if packet.eeee is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.eeee.size())
            for element9 in packet.eeee:
                buffer.writeFloat(element9)
        buffer.writeDouble(packet.f)
        buffer.writeDouble(packet.ff)
        if packet.fff is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.fff.size())
            for element10 in packet.fff:
                buffer.writeDouble(element10)
        if packet.ffff is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.ffff.size())
            for element11 in packet.ffff:
                buffer.writeDouble(element11)
        buffer.writeBool(packet.g)
        buffer.writeBool(packet.gg)
        if packet.ggg is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.ggg.size())
            for element12 in packet.ggg:
                buffer.writeBool(element12)
        if packet.gggg is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.gggg.size())
            for element13 in packet.gggg:
                buffer.writeBool(element13)
        buffer.writeChar(packet.h)
        buffer.writeChar(packet.hh)
        if packet.hhh is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.hhh.size())
            for element14 in packet.hhh:
                buffer.writeChar(element14)
        if packet.hhhh is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.hhhh.size())
            for element15 in packet.hhhh:
                buffer.writeChar(element15)
        buffer.writeString(packet.jj)
        if packet.jjj is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.jjj.size())
            for element16 in packet.jjj:
                buffer.writeString(element16)
        buffer.writePacket(packet.kk, 102)
        if packet.kkk is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.kkk.size())
            for element17 in packet.kkk:
                buffer.writePacket(element17, 102)
        if packet.l is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.l.size())
            for element18 in packet.l:
                buffer.writeInt(element18)
        if packet.ll is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.ll.size())
            for element19 in packet.ll:
                if element19 is None:
                    buffer.writeInt(0)
                else:
                    buffer.writeInt(element19.size())
                    for element20 in element19:
                        if element20 is None:
                            buffer.writeInt(0)
                        else:
                            buffer.writeInt(element20.size())
                            for element21 in element20:
                                buffer.writeInt(element21)
        if packet.lll is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.lll.size())
            for element22 in packet.lll:
                if element22 is None:
                    buffer.writeInt(0)
                else:
                    buffer.writeInt(element22.size())
                    for element23 in element22:
                        buffer.writePacket(element23, 102)
        if packet.llll is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.llll.size())
            for element24 in packet.llll:
                buffer.writeString(element24)
        if packet.lllll is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.lllll.size())
            for element25 in packet.lllll:
                if element25 is None:
                    buffer.writeInt(0)
                else:
                    buffer.writeInt(element25.size())
                    for key26 in element25:
                        value27 = element25[key26]
                        buffer.writeInt(key26)
                        buffer.writeString(value27)
        if packet.m is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.m.size())
            for key28 in packet.m:
                value29 = packet.m[key28]
                buffer.writeInt(key28)
                buffer.writeString(value29)
        if packet.mm is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.mm.size())
            for key30 in packet.mm:
                value31 = packet.mm[key30]
                buffer.writeInt(key30)
                buffer.writePacket(value31, 102)
        if packet.mmm is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.mmm.size())
            for key32 in packet.mmm:
                value33 = packet.mmm[key32]
                buffer.writePacket(key32, 102)
                if value33 is None:
                    buffer.writeInt(0)
                else:
                    buffer.writeInt(value33.size())
                    for element34 in value33:
                        buffer.writeInt(element34)
        if packet.mmmm is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.mmmm.size())
            for key35 in packet.mmmm:
                value36 = packet.mmmm[key35]
                if key35 is None:
                    buffer.writeInt(0)
                else:
                    buffer.writeInt(key35.size())
                    for element37 in key35:
                        if element37 is None:
                            buffer.writeInt(0)
                        else:
                            buffer.writeInt(element37.size())
                            for element38 in element37:
                                buffer.writePacket(element38, 102)
                if value36 is None:
                    buffer.writeInt(0)
                else:
                    buffer.writeInt(value36.size())
                    for element39 in value36:
                        if element39 is None:
                            buffer.writeInt(0)
                        else:
                            buffer.writeInt(element39.size())
                            for element40 in element39:
                                if element40 is None:
                                    buffer.writeInt(0)
                                else:
                                    buffer.writeInt(element40.size())
                                    for element41 in element40:
                                        buffer.writeInt(element41)
        if packet.mmmmm is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.mmmmm.size())
            for key42 in packet.mmmmm:
                value43 = packet.mmmmm[key42]
                if key42 is None:
                    buffer.writeInt(0)
                else:
                    buffer.writeInt(key42.size())
                    for element44 in key42:
                        if element44 is None:
                            buffer.writeInt(0)
                        else:
                            buffer.writeInt(element44.size())
                            for key45 in element44:
                                value46 = element44[key45]
                                buffer.writeInt(key45)
                                buffer.writeString(value46)
                if value43 is None:
                    buffer.writeInt(0)
                else:
                    buffer.writeInt(value43.size())
                    for element47 in value43:
                        if element47 is None:
                            buffer.writeInt(0)
                        else:
                            buffer.writeInt(element47.size())
                            for key48 in element47:
                                value49 = element47[key48]
                                buffer.writeInt(key48)
                                buffer.writeString(value49)
        if packet.s is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.s.size())
            for element50 in packet.s:
                buffer.writeInt(element50)
        if packet.ss is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.ss.size())
            for element51 in packet.ss:
                if element51 is None:
                    buffer.writeInt(0)
                else:
                    buffer.writeInt(element51.size())
                    for element52 in element51:
                        if element52 is None:
                            buffer.writeInt(0)
                        else:
                            buffer.writeInt(element52.size())
                            for element53 in element52:
                                buffer.writeInt(element53)
        if packet.sss is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.sss.size())
            for element54 in packet.sss:
                if element54 is None:
                    buffer.writeInt(0)
                else:
                    buffer.writeInt(element54.size())
                    for element55 in element54:
                        buffer.writePacket(element55, 102)
        if packet.ssss is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.ssss.size())
            for element56 in packet.ssss:
                buffer.writeString(element56)
        if packet.sssss is None:
            buffer.writeInt(0)
        else:
            buffer.writeInt(packet.sssss.size())
            for element57 in packet.sssss:
                if element57 is None:
                    buffer.writeInt(0)
                else:
                    buffer.writeInt(element57.size())
                    for key58 in element57:
                        value59 = element57[key58]
                        buffer.writeInt(key58)
                        buffer.writeString(value59)
        buffer.writeInt(packet.myCompatible)
        buffer.writePacket(packet.myObject, 102)
        pass

    @classmethod
    def read(cls, buffer):
        if not buffer.readBool():
            return None
        packet = ComplexObject()
        result60 = buffer.readByte()
        packet.a = result60
        result61 = buffer.readByte()
        packet.aa = result61
        result62 = []
        size64 = buffer.readInt()
        if size64 > 0:
            for index63 in range(size64):
                result65 = buffer.readByte()
                result62.append(result65)
        packet.aaa = result62
        result66 = []
        size68 = buffer.readInt()
        if size68 > 0:
            for index67 in range(size68):
                result69 = buffer.readByte()
                result66.append(result69)
        packet.aaaa = result66
        result70 = buffer.readShort()
        packet.b = result70
        result71 = buffer.readShort()
        packet.bb = result71
        result72 = []
        size74 = buffer.readInt()
        if size74 > 0:
            for index73 in range(size74):
                result75 = buffer.readShort()
                result72.append(result75)
        packet.bbb = result72
        result76 = []
        size78 = buffer.readInt()
        if size78 > 0:
            for index77 in range(size78):
                result79 = buffer.readShort()
                result76.append(result79)
        packet.bbbb = result76
        result80 = buffer.readInt()
        packet.c = result80
        result81 = buffer.readInt()
        packet.cc = result81
        result82 = []
        size84 = buffer.readInt()
        if size84 > 0:
            for index83 in range(size84):
                result85 = buffer.readInt()
                result82.append(result85)
        packet.ccc = result82
        result86 = []
        size88 = buffer.readInt()
        if size88 > 0:
            for index87 in range(size88):
                result89 = buffer.readInt()
                result86.append(result89)
        packet.cccc = result86
        result90 = buffer.readLong()
        packet.d = result90
        result91 = buffer.readLong()
        packet.dd = result91
        result92 = []
        size94 = buffer.readInt()
        if size94 > 0:
            for index93 in range(size94):
                result95 = buffer.readLong()
                result92.append(result95)
        packet.ddd = result92
        result96 = []
        size98 = buffer.readInt()
        if size98 > 0:
            for index97 in range(size98):
                result99 = buffer.readLong()
                result96.append(result99)
        packet.dddd = result96
        result100 = buffer.readFloat()
        packet.e = result100
        result101 = buffer.readFloat()
        packet.ee = result101
        result102 = []
        size104 = buffer.readInt()
        if size104 > 0:
            for index103 in range(size104):
                result105 = buffer.readFloat()
                result102.append(result105)
        packet.eee = result102
        result106 = []
        size108 = buffer.readInt()
        if size108 > 0:
            for index107 in range(size108):
                result109 = buffer.readFloat()
                result106.append(result109)
        packet.eeee = result106
        result110 = buffer.readDouble()
        packet.f = result110
        result111 = buffer.readDouble()
        packet.ff = result111
        result112 = []
        size114 = buffer.readInt()
        if size114 > 0:
            for index113 in range(size114):
                result115 = buffer.readDouble()
                result112.append(result115)
        packet.fff = result112
        result116 = []
        size118 = buffer.readInt()
        if size118 > 0:
            for index117 in range(size118):
                result119 = buffer.readDouble()
                result116.append(result119)
        packet.ffff = result116
        result120 = buffer.readBool() 
        packet.g = result120
        result121 = buffer.readBool() 
        packet.gg = result121
        result122 = []
        size124 = buffer.readInt()
        if size124 > 0:
            for index123 in range(size124):
                result125 = buffer.readBool() 
                result122.append(result125)
        packet.ggg = result122
        result126 = []
        size128 = buffer.readInt()
        if size128 > 0:
            for index127 in range(size128):
                result129 = buffer.readBool() 
                result126.append(result129)
        packet.gggg = result126
        result130 = buffer.readChar()
        packet.h = result130
        result131 = buffer.readChar()
        packet.hh = result131
        result132 = []
        size134 = buffer.readInt()
        if size134 > 0:
            for index133 in range(size134):
                result135 = buffer.readChar()
                result132.append(result135)
        packet.hhh = result132
        result136 = []
        size138 = buffer.readInt()
        if size138 > 0:
            for index137 in range(size138):
                result139 = buffer.readChar()
                result136.append(result139)
        packet.hhhh = result136
        result140 = buffer.readString()
        packet.jj = result140
        result141 = []
        size143 = buffer.readInt()
        if size143 > 0:
            for index142 in range(size143):
                result144 = buffer.readString()
                result141.append(result144)
        packet.jjj = result141
        result145 = buffer.readPacket(102)
        packet.kk = result145
        result146 = []
        size148 = buffer.readInt()
        if size148 > 0:
            for index147 in range(size148):
                result149 = buffer.readPacket(102)
                result146.append(result149)
        packet.kkk = result146
        result150 = []
        size152 = buffer.readInt()
        if size152 > 0:
            for index151 in range(size152):
                result153 = buffer.readInt()
                result150.append(result153)
        packet.l = result150
        result154 = []
        size156 = buffer.readInt()
        if size156 > 0:
            for index155 in range(size156):
                result157 = []
                size159 = buffer.readInt()
                if size159 > 0:
                    for index158 in range(size159):
                        result160 = []
                        size162 = buffer.readInt()
                        if size162 > 0:
                            for index161 in range(size162):
                                result163 = buffer.readInt()
                                result160.append(result163)
                        result157.append(result160)
                result154.append(result157)
        packet.ll = result154
        result164 = []
        size166 = buffer.readInt()
        if size166 > 0:
            for index165 in range(size166):
                result167 = []
                size169 = buffer.readInt()
                if size169 > 0:
                    for index168 in range(size169):
                        result170 = buffer.readPacket(102)
                        result167.append(result170)
                result164.append(result167)
        packet.lll = result164
        result171 = []
        size173 = buffer.readInt()
        if size173 > 0:
            for index172 in range(size173):
                result174 = buffer.readString()
                result171.append(result174)
        packet.llll = result171
        result175 = []
        size177 = buffer.readInt()
        if size177 > 0:
            for index176 in range(size177):
                result178 = {}
                size179 = buffer.readInt()
                if size179 > 0:
                    for index180 in range(size179):
                        result181 = buffer.readInt()
                        result182 = buffer.readString()
                        result178[result181] = result182
                result175.append(result178)
        packet.lllll = result175
        result183 = {}
        size184 = buffer.readInt()
        if size184 > 0:
            for index185 in range(size184):
                result186 = buffer.readInt()
                result187 = buffer.readString()
                result183[result186] = result187
        packet.m = result183
        result188 = {}
        size189 = buffer.readInt()
        if size189 > 0:
            for index190 in range(size189):
                result191 = buffer.readInt()
                result192 = buffer.readPacket(102)
                result188[result191] = result192
        packet.mm = result188
        result193 = {}
        size194 = buffer.readInt()
        if size194 > 0:
            for index195 in range(size194):
                result196 = buffer.readPacket(102)
                result197 = []
                size199 = buffer.readInt()
                if size199 > 0:
                    for index198 in range(size199):
                        result200 = buffer.readInt()
                        result197.append(result200)
                result193[result196] = result197
        packet.mmm = result193
        result201 = {}
        size202 = buffer.readInt()
        if size202 > 0:
            for index203 in range(size202):
                result204 = []
                size206 = buffer.readInt()
                if size206 > 0:
                    for index205 in range(size206):
                        result207 = []
                        size209 = buffer.readInt()
                        if size209 > 0:
                            for index208 in range(size209):
                                result210 = buffer.readPacket(102)
                                result207.append(result210)
                        result204.append(result207)
                result211 = []
                size213 = buffer.readInt()
                if size213 > 0:
                    for index212 in range(size213):
                        result214 = []
                        size216 = buffer.readInt()
                        if size216 > 0:
                            for index215 in range(size216):
                                result217 = []
                                size219 = buffer.readInt()
                                if size219 > 0:
                                    for index218 in range(size219):
                                        result220 = buffer.readInt()
                                        result217.append(result220)
                                result214.append(result217)
                        result211.append(result214)
                result201[result204] = result211
        packet.mmmm = result201
        result221 = {}
        size222 = buffer.readInt()
        if size222 > 0:
            for index223 in range(size222):
                result224 = []
                size226 = buffer.readInt()
                if size226 > 0:
                    for index225 in range(size226):
                        result227 = {}
                        size228 = buffer.readInt()
                        if size228 > 0:
                            for index229 in range(size228):
                                result230 = buffer.readInt()
                                result231 = buffer.readString()
                                result227[result230] = result231
                        result224.append(result227)
                result232 = []
                size234 = buffer.readInt()
                if size234 > 0:
                    for index233 in range(size234):
                        result235 = {}
                        size236 = buffer.readInt()
                        if size236 > 0:
                            for index237 in range(size236):
                                result238 = buffer.readInt()
                                result239 = buffer.readString()
                                result235[result238] = result239
                        result232.append(result235)
                result221[result224] = result232
        packet.mmmmm = result221
        result240 = []
        size242 = buffer.readInt()
        if size242 > 0:
            for index241 in range(size242):
                result243 = buffer.readInt()
                result240.append(result243)
        packet.s = result240
        result244 = []
        size246 = buffer.readInt()
        if size246 > 0:
            for index245 in range(size246):
                result247 = []
                size249 = buffer.readInt()
                if size249 > 0:
                    for index248 in range(size249):
                        result250 = []
                        size252 = buffer.readInt()
                        if size252 > 0:
                            for index251 in range(size252):
                                result253 = buffer.readInt()
                                result250.append(result253)
                        result247.append(result250)
                result244.append(result247)
        packet.ss = result244
        result254 = []
        size256 = buffer.readInt()
        if size256 > 0:
            for index255 in range(size256):
                result257 = []
                size259 = buffer.readInt()
                if size259 > 0:
                    for index258 in range(size259):
                        result260 = buffer.readPacket(102)
                        result257.append(result260)
                result254.append(result257)
        packet.sss = result254
        result261 = []
        size263 = buffer.readInt()
        if size263 > 0:
            for index262 in range(size263):
                result264 = buffer.readString()
                result261.append(result264)
        packet.ssss = result261
        result265 = []
        size267 = buffer.readInt()
        if size267 > 0:
            for index266 in range(size267):
                result268 = {}
                size269 = buffer.readInt()
                if size269 > 0:
                    for index270 in range(size269):
                        result271 = buffer.readInt()
                        result272 = buffer.readString()
                        result268[result271] = result272
                result265.append(result268)
        packet.sssss = result265
        if not buffer.isReadable():
            return packet
        pass
        result273 = buffer.readInt()
        packet.myCompatible = result273
        if not buffer.isReadable():
            return packet
        pass
        result274 = buffer.readPacket(102)
        packet.myObject = result274
        return packet

