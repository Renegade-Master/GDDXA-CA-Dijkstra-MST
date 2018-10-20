#
#	@author			Ciaran Bent [K00221230]
#	@creationDate	18/09/2018
#	@description	'Statistics, Algorithms, and AI' Python containing
#					several utilities used in the 'minSpanTree.py' program.
#	@version		1.0.4

import random

# class Node:
# 	def __init__(self):

# class Graph:
#  	graph[] = 

class Connection: 						#EXAMINE LECTURE 5 - PG. 54
	def __init__(self,n1,n2,wt):
		self.node1 = n1
		self.node2 = n2
		self.weight = wt

	# int from():
	# 	#

	# int to():
	# 	#

	# int capacity():
	# 	#

# def compileGraph(fileName): 			#EXAMINE LECTURE 5 - PG. 58
# 	out = open(fileName + '.csv','r')
# 	fileFormat = out.readline().rstrip()
# 	nodes = int(out.readline())

# 	#Array/list of Connection objects GOES HERE

# 	for line in out.readlines():
		
# 		u = line.split(',')[0]
# 		v = line.split(',')[1]
# 		w = line.rstrip().split(',')[2]
# 		print('%r,%r,%r' % (u,v,w))

# 	out.close()

def printGraphData(fileName):
	out = open(fileName + '.csv','r')
	fileFormat = out.readline().rstrip()
	nodes = int(out.readline())
	print('File Format: %r\nNodes: %r' % (fileFormat,nodes))

	for line in out.readlines():
		u = line.split(',')[0]
		v = line.split(',')[1]
		w = line.rstrip().split(',')[2]
		print('%r,%r,%r' % (u,v,w))

	out.close()

def generateFile(fileName,nodeMin,nodeMax,conns,wt):
	nodes = random.randint(nodeMin,nodeMax)
	out = open(fileName + '.csv','w')
	out.write('s\n%r\n' % nodes)

	for x in range(conns):
		u = random.randint(0,nodes)
		v = random.randint(0,nodes)
		w = random.randint(1,wt)
		out.write('%r,%r,%r\n' % (u,v,w))

	out.close()

def customFile():
	print('Please enter the following information to generate your test file...\n\n')
	fileName = input('Name of custom file:\n>>')
	nodeMin = input('Minimum Nodes:\n>>')
	nodeMax = input('Maximum Nodes:\n>>')
	connections = input('Connection Count:\n>>')
	wtMax = input('Maximum Path Weight:\n>>')
	generateFile(fileName,int(nodeMin),int(nodeMax),int(connections),int(wtMax))

	return(fileName)