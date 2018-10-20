#
#	@author			Ciaran Bent [K00221230]
#	@creationDate	22/09/2018
#	@description	'Statistics, Algorithms, and AI' testing
#					script for learning Python
#	@version		0.0.0

from array 			import array
from collections	import deque
#from numpy			import array

############################
#	Getting Objects working	COMPLETE
############################

class Connection:
	def __init__(self,n1,n2,wt):
		self.node1 = n1
		self.node2 = n2
		self.weight = wt

	def nodeFrom(self):
		return(self.node1)

	def nodeTo(self):
		return(self.node2)

	def edgeWeight(self):
		return(self.weight)

class Graph:
	def __init__(self,graph):
		graph = []

conn1 = Connection(1,2,7)

print('Connection 1')
print('Node 1:\t%r' % conn1.node1)
print('Node 2:\t%r' % conn1.node2)
print('Weight:\t%r' % conn1.weight)

print('------------------------')

arryOfConns = []
arryOfConns.append(conn1)
arryOfConns.append(Connection(2,3,5))

print('Connection 1')
print('Node 1:\t%r' % arryOfConns[0].node1)
print('Node 2:\t%r' % arryOfConns[0].node2)
print('Weight:\t%r\n' % arryOfConns[0].weight)
print('Connection 2')
print('Node 1:\t%r' % arryOfConns[1].node1)
print('Node 2:\t%r' % arryOfConns[1].node2)
print('Weight:\t%r\n' % arryOfConns[1].weight)

print('------------------------')

print('Connection 1 connects %r to %r with a weight of %r\n' % (arryOfConns[0].nodeFrom(),arryOfConns[0].nodeTo(),arryOfConns[0].edgeWeight()))
print('Connection 2 connects %r to %r with a weight of %r\n' % (arryOfConns[1].nodeFrom(),arryOfConns[1].nodeTo(),arryOfConns[1].edgeWeight()))

print('There are %s Connections.' % len(arryOfConns))

print('------------------------')
print('------------------------')
print('------------------------')

#################################
#		ARRAY MAGIC BELOW		#
#################################

multiArray = [[0 for x in range(5)] for y in range(2)]
#multiArray = [[0 for x in range(5)]]

multiArray[0].append(2)

for i in range(len(multiArray)):
	for j in range(len(multiArray[i])):
		print('[%r][%r] = %r' % (i,j,multiArray[i][j]))

#multiArray = [[]]
#multiArray.append(Connection(1,1,1))
#multiArray[0].append(Connection(2,2,2))

# multiArray[0][0] = Connection(1,5,8)
# multiArray[0][1] = Connection(2,5,8)
# multiArray[1][0] = Connection(3,5,8)
# multiArray[1][1] = Connection(4,5,8)

#print('%r' % multiArray[0][0].nodeFrom())
#print('%r' % multiArray[1][0].nodeFrom())
# print('%r' % multiArray[1][0].nodeFrom())
# print('%r' % multiArray[1][1].nodeFrom())

#################################
#		ARRAY MAGIC ABOVE		#
#################################



#mixArray = array('i',[Connection(1,2,7),Connection(3,2,4)])

#mixArray = array('u',[deque('1,2,3'),deque('4,5,6'),deque('7,8,9')])

# for row in mixArray:
# 	print(mixArray[row])

############################
#	Getting 'deques' working	COMPLETE
############################

# dblLst = deque('abc')

# for elem in dblLst:
# 	print(elem.upper())

############################
#	Getting arrays working		COMPLETE
############################

# testArray = array("I",[1,2,3])

# print(testArray[0])
# print(testArray[1])
# print(testArray[2])
