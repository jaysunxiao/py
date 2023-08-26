import veryBigObject as veryBigObject
import complexObject as complexObject
import normalObject as normalObject
import objectA as objectA
import objectB as objectB
import simpleObject as simpleObject

protocols = {}

protocols[0] = veryBigObject.VeryBigObject
protocols[100] = complexObject.ComplexObject
protocols[101] = normalObject.NormalObject
protocols[102] = objectA.ObjectA
protocols[103] = objectB.ObjectB
protocols[104] = simpleObject.SimpleObject

def getProtocol(protocolId):
	return protocols[protocolId]

def write(buffer, packet):
	protocolId = packet.protocolId()
	buffer.writeShort(protocolId)
	protocol = protocols[protocolId]
	protocol.write(buffer, packet)

def read(buffer):
	protocolId = buffer.readShort()
	protocol = protocols[protocolId]
	packet = protocol.read(buffer)
	return packet
