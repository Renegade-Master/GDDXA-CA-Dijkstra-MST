'''	@author			Ciaran Bent [K00221230]
	@creationDate	20/10/2018
	@description	'Statistics, Algorithms, and AI' auxiliary functions 
	@version		1.0.0
	@deadline		11/11/2018
'''

import math						# For infinity value
import os						# For directory manipulation
from operator import attrgetter	# For sorting

'''
	@desc	A class to create a Connection object.
	@param	to	- The Node that this Connection connects TO
			wt	- The Weight of this Connection
	@funct	toString	- Easily access important Connection information
'''
class Connection:
	def __init__(self,to,wt):
		self.nodeTo = int(to)
		self.weight = int(wt)

	def toString(self):
		return(	'to Node %r '
				'with a weight of %r' % (self.nodeTo,self.weight))

'''
	@desc	The Shortest Path Tree structure.
	@param	n	- The number of Nodes in the Graph.  Used to create lists
	@funct	listTree	- Print important contents of the Tree object
			debugTree	- Print ALL contents of the Tree object
'''
class shortPathTree:
	def __init__(self,n):
		self.distance 	= [math.inf] * n
		self.via 		= [0] * n
		self.known 		= [False] * n

	def listTree(self):
		i = 1
		print('To\tDist\tVia')
		for nd in range(len(self.distance)):
			print('%s\t%s\t%s' % (i,self.distance[nd],self.via[nd]))
			i += 1

	def debugTree(self):
		i = 1
		print('To\tDist\tVia\tKnown')
		for nd in range(len(self.distance)):
			print('%s\t%s\t%s\t%s' % (i,self.distance[nd],self.via[nd],self.known[nd]))
			i += 1

'''
	@desc	A class to create a Graph object
	@param	n	- The number of Nodes in the Graph
	@funct	addConn		- Add a new Connection to the Graph
			listConns	- List the Connections in the Graph
			getNodes	- Return the number of Nodes in the Graph
'''
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

	def getNodes(self):
		return(int(self.nodes))

########################################################################

'''
	@desc	Compile a new Graph object from a text file
	@param	fileName	- The STRING title of the desired text file
'''
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

		if u > v:	# Improve readability of Nodes
			temp = u
			u = v
			v = temp

		graph.addCon(int(u),int(v),int(w),nodes)

	out.close()
	
	return(graph)

'''
	@desc	List the files in a specified directory
	@param	pathName	- The STRING path (absolute or relative) of the directory
'''
def listDir(pathName):
	try:
		print('__Listing all files in Test Directory__\n')

		i = int (0)
		for line in os.listdir(pathName):
			v = line.split('.csv')[0]
			i += int(1)
			print('\t%s' % v)

		print('\n')
	except:
		print('Cannot access \'os\' module.  It is safe to ignore this warning.')

'''
	@desc	Dijkstra function receives a Graph object, and finds the Shortest Path
			Tree from the node that was also passed in.
	@param	g		- The Graph object
			stNd	- The Starting Node for SPT Calculation
'''
def Dijkstra(g,stNd):
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

	# Loop through list of lists looking for point 1; point 2...
	# Add weights as passing through points
	# If found, record total weight, add to SPT
	# If end of list found, look for next point

	for i in range(g.nodes * 2):
		currNode = 0		# The Node we are currently examining
		nextNode = 0
		lookFor += 1		# The Node we are looking for
		if lookFor == g.nodes + 1:
		  	lookFor = 1
		if lookFor == stNd:	# Don't look for shortest path to SELF
			continue
		
		for fr in g.connections:				# For each vertex
			searchWeight = 0
			currNode += 1
			if lookFor == stNd:					# Don't look for shortest path to SELF
	 			continue
			fr.sort(key=attrgetter('weight'))	# Sort list so shortest is First
			for to in fr:						# For every vertex connected to 'fr'
				nextNode = to.nodeTo
				
				if currNode == lookFor:			# Swap 'from' and 'to' when looking
					temp = nextNode				# for a node currently assigned to
					nextNode = currNode			# 'from'
					currNode = temp
				
				if((nextNode == lookFor)):
					if not g.shortPathTree.known[nextNode - 1]:
						if((to.weight + g.shortPathTree.distance[currNode - 1]) <	# If the Path weight is less
							(g.shortPathTree.distance[nextNode - 1])):				# than the current Shortest Path
							
							# Update the Shortest Path
							g.shortPathTree.distance[nextNode - 1] = (to.weight + int(g.shortPathTree.distance[currNode - 1]))
							g.shortPathTree.via[nextNode - 1] = currNode
						else:
							# Do nothing
							pass
					else:
						# Do nothing
						pass

		# Check for Completeness
		for ent in g.shortPathTree.known:
			if ent == False:
				ent = True
				break
			allKnown = True
