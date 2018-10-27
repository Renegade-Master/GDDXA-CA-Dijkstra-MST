'''	@author			Ciaran Bent [K00221230]
	@creationDate	20/10/2018
	@description	'Statistics, Algorithms, and AI' auxiliary functions 
	@version		1.0.0
	@deadline		31/10/2018
'''

import math
##
class Connection:
	def __init__(self,to,wt):
		self.nodeTo = to
		self.weight = wt

	def toString(self):
		return(	'to Node %r '
				'with a weight of %r, ' % (self.nodeTo,self.weight))
##
class shortPathTree:
	def __init__(self,n):
		self.distance 	= [math.inf] * n
		self.via 		= [0] * n
		self.known 		= [True] * n

	def debugTree(self):
		i = 1
		print('To\tDist\tVia\tKnown')
		for nd in range(len(self.distance)):
			print('%s\t%s\t%s\t%s' % (i,self.distance[nd],self.via[nd],self.known[nd]))
			i += 1

##
class Graph:
	def __init__(self,n):
		self.nodes = n
		self.weight = 0
		self.maxWeight = 0
		self.shortPathTree = shortPathTree(n)
		
		# Creates a list containing 'n' lists
		self.connections = [[] for y in range(n)] 

	def addCon(self,fr,to,wt,max):
		# Node 5 == connections[4]
		self.connections[int(fr) - 1].append(Connection(to,wt))
		self.weight += int(wt)
		if int(wt) > int(self.maxWeight):
			self.maxWeight = int(wt)

	def listConns(self):
		for i in range(len(self.connections)):
			print('Connection %r:\t' % (i + 1))
			for j in range(len(self.connections[i])):
				print(self.connections[i][j].toString())
			print('\n')

########################################################################
##
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
##
def Dijkstra(g):
	known = False

	print(	'Calculating Shortest Path Spanning Tree...\n\n'
			'Nodes in this Graph:\t%r\n'
			'Max Graph Weight is:\t%r\n'
			'Total Graph weight is:\t%r\n' 
			% (g.nodes,g.maxWeight,g.weight))

	while not known:
		for fr in g.connections:
			for to in fr:
				print(to.toString())
			print('\n')

		for i in g.shortPathTree.known:
			if i == True:
				continue
			if i == False:
				break
			known = True
