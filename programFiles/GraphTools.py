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
				'with a weight of %r' % (self.nodeTo,self.weight))

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
				print('%s, ' % self.connections[i][j].toString())
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
	allKnown = False
	lookFor = 0

	print(	'Calculating Shortest Path Spanning Tree...\n\n'
			'Nodes in this Graph:\t: %r\n'
			'Max Graph Weight is:\t: %r\n'
			'Total Graph weight is:\t: %r\n'
			'Start Node is:\t\t: %r\n' 
			% (g.nodes,g.maxWeight,g.weight,stNd))

	g.shortPathTree.distance[stNd - 1] = 0
	g.shortPathTree.via[stNd - 1] = 'SELF'
	g.shortPathTree.known[stNd - 1] = True

	# Loop through list of lists looking for point 1 then point 2
	# Add weights as passing through points
	# If found, record total weight, add to SPT
	# If end of list found, look for next point

	for i in range(g.nodes * 2):
	#while lookFor < g.nodes + 1:
	#while not allKnown:
		lookFor += 1	# The Node we are looking for
		if lookFor == g.nodes + 1:
		  	lookFor = 1
		if lookFor == stNd:	# Don't look for shortest path to SELF
			continue
		currNode = 0	# The Node we are currently examining
		nextNode = 0
		
		for fr in g.connections:				# For each vertex
			#print('Looking for Node %r' % lookFor)
			searchWeight = 0
			currNode += 1
			if lookFor == stNd:					# Don't look for shortest path to SELF
	 			continue
			fr.sort(key=attrgetter('weight'))	# Sort list so shortest is First
			for to in fr:						# For every vertex connected to 'fr'
				#print('Looking for Node %r in %r->%r' % (lookFor,currNode,to.nodeTo))
				nextNode = to.nodeTo
				if currNode == lookFor:
					temp = nextNode
					nextNode = currNode
					currNode = temp
				print('\nLooking for Node %r in %r->%r' % (lookFor,currNode,to.nodeTo))
				print('At Node [%s]' % to.toString())
				if((nextNode == lookFor)):
					# ADD A NEW ENTRY TO THE SPT
					if not g.shortPathTree.known[nextNode - 1]:
						print('ShPt to Node %r IS NOT known' % int(nextNode))
						if((to.weight + g.shortPathTree.distance[currNode - 1]) < (g.shortPathTree.distance[nextNode - 1])):
							print('The Path via Node %r: %r is shorter than %r' % (currNode,(to.weight + int(g.shortPathTree.distance[currNode - 1])),(g.shortPathTree.distance[nextNode - 1])))
							g.shortPathTree.distance[nextNode - 1] = (to.weight + int(g.shortPathTree.distance[currNode - 1]))
							g.shortPathTree.via[nextNode - 1] = currNode
							#g.shortPathTree.known[nextNode - 1] = True
						else:
							print('The Path via Node %r: %r is not shorter than %r' % (currNode,(to.weight + g.shortPathTree.distance[currNode - 1]),(g.shortPathTree.distance[nextNode - 1])))
					else:
						print('ShPt to Node %r IS known' % int(nextNode))
		#g.shortPathTree.known[lookFor - 1] = True

		# Check for Completeness
		# for ent in g.shortPathTree.known:
		# 	if ent == True:
		# 		continue
		# 	elif ent == False:
		# 		break
		# 	allKnown = True
		g.shortPathTree.debugTree()
		print('---\n')
