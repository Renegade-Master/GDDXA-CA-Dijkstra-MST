'''	@author			Ciaran Bent [K00221230]
	@creationDate	20/10/2018
	@description	'Statistics, Algorithms, and AI' auxiliary functions 
	@version		1.0.0
	@deadline		31/10/2018
'''

import math

class Connection:
	def __init__(self,to,wt):
		self.nodeTo = to
		self.weight = wt

	def toString(self):
		return(	'to Node %r '
				'with a weight of %r, ' % (self.nodeTo,self.weight))

class shortPathTree:
	def __init__(self,n):
		self.distance 	= [math.inf] * n
		self.via 		= [0] * n
		self.known 		= [0] * n

	def debugTree(self):
		print('To\tDist\tVia')
		for nd in range(len(self.distance)):
			print('%s\t%s\t%s' % (self.distance[nd],self.via[nd],self.known[nd]))

class Graph:
	def __init__(self,n):
		self.nodes = n
		self.weight = 0
		self.shortPathTree = shortPathTree(n)
		
		# Creates a list containing 'n' lists
		self.connections = [[] for y in range(n)] 

	def addCon(self,fr,to,wt,max):
		# Node 5 == connections[4]
		self.connections[int(fr) - 1].append(Connection(to,wt))
		self.weight += int(wt)

	def listConns(self):
		for i in range(len(self.connections)):
			print('Connection %r:\t' % (i + 1))
			for j in range(len(self.connections[i])):
				print(self.connections[i][j].toString())
			print('\n')

########################################################################

def compileGraph(fileName):
	out = open(fileName + '.csv','r')
	fileFormat = out.readline().rstrip()
	nodes = int(out.readline())

	graph = Graph(nodes)

	for line in out.readlines():
		u = line.split(',')[0]
		v = line.split(',')[1]
		w = line.rstrip().split(',')[2]
		
		if u == v:
			continue

		if u > v:						# Improve readability of Nodes
			temp = u
			u = v
			v = temp

		graph.addCon(u,v,w,nodes)

	out.close()
	
	return(graph)
