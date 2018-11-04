'''	@author			Ciaran Bent [K00221230]
	@creationDate	20/10/2018
	@description	'Statistics, Algorithms, and AI' auxiliary functions 
	@version		1.0.0
	@deadline		31/10/2018
'''

import math
from operator import attrgetter

##
class Connection:
	def __init__(self,to,wt):
		self.nodeTo = int(to)
		self.weight = int(wt)

	def toString(self):
		return(	'to Node %r '
				'with a weight of %r, ' % (self.nodeTo,self.weight))

##
class shortPathTree:
	def __init__(self,n):
		self.distance 	= [math.inf] * n
		self.via 		= [0] * n
		self.known 		= [False] * n

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

		graph.addCon(int(u),int(v),int(w),nodes)

	out.close()
	
	return(graph)

##
def traceback(start,node):
		totalWeight = 0

		return(totalWeight)

##
def Dijkstra(g,stNd):
	#known = False
	known = 0
	lookFor = 0

	print(	'Calculating Shortest Path Spanning Tree...\n\n'
			'Nodes in this Graph:\t: %r\n'
			'Max Graph Weight is:\t: %r\n'
			'Total Graph weight is:\t: %r\n'
			'Start Node is:\t\t: %r\n' 
			% (g.nodes,g.maxWeight,g.weight,stNd))

	g.shortPathTree.distance[stNd - 1] = 'N/A'
	g.shortPathTree.via[stNd - 1] = 'SELF'
	g.shortPathTree.known[stNd - 1] = True

	# Loop through list of lists looking for point 1 then point 2
	# Add weights as passing through points
	# If found, record total weight, add to SPT
	# If end of list found, look for next point

	while lookFor < g.nodes:
		lookFor += 1
		currNode = 0
		for fr in g.connections:				# For each vertex
			searchWeight = 0
			currNode += 1
			fr.sort(key=attrgetter('weight'))	# Sort list so shortest is First
			print('Looking for [%r] from [%r]' % (lookFor,currNode))
			for to in fr:						# For every vertex connected to 'fr'
				searchWeight += to.weight
				if to.nodeTo == lookFor:
					print('\tFound [%s]; Total Weight %r' % (to.toString(),searchWeight))
					# ADD A NEW ENTRY TO THE SPT
			print('\n')
		#known += 1
		print('---\n')

	#while not known:
	# while known < 1:
	# 	for fr in g.connections:				# For each vertex
	# 		fr.sort(key=attrgetter('weight'))	# Sort list so shortest is First
	# 		for to in fr:						# For every vertex attached to 'fr'
	# 			if(not g.shortPathTree.known[to.nodeTo - 1] and 
	# 			    g.shortPathTree.distance[to.nodeTo - 1] > traceback(stNd,currNode)):
	# 					g.shortPathTree.distance[to.nodeTo - 1] = to.weight
	# 					g.shortPathTree.via[to.nodeTo - 1] = 1
	# 		g.shortPathTree.known[currNode] = True
	# 	known += 1

		# for i in g.shortPathTree.known:
		# 	if i == True:
		# 		continue
		# 	if i == False:
		# 		break
		# 	known = True
