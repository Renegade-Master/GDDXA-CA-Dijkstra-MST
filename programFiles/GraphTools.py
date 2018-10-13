'''	@author			Ciaran Bent [K00221230]
	@creationDate	18/09/2018
	@description	'Statistics, Algorithms, and AI' Python containing
					several utilities used in the 'minSpanTree.py' program.
	@version		1.5.1
	@deadline		14/10/2018
'''

from operator import attrgetter
import math
import random

#################################
#			OBJECTS				#
#################################

'''	@descr	- An object to represent a node connection in a Graph.
	@param	- 
			n1	- The node FROM
			n2	- The node TO
			wt	- The connection WEIGHT
	@funct	-
			nodeFrom	- Returns INTEGER iterator assigned to the PREVIOUS node
			nodeTo		- Returns INTEGER iterator assigned to the NEXT node
			edgeWeight	- Returns INTEGER value assigned to the WEIGHT of this connection
'''
class Connection:
	def __init__(self,n1,n2,wt):
		self.node1 = n1
		self.node2 = n2
		self.weight = wt

	def nodeFrom(self):
		return(int(self.node1))

	def nodeTo(self):
		return(int(self.node2))

	def edgeWeight(self):
		return(int(self.weight))

	def toString(self):
		return(	'Node %r to Node %r '
				'with a weight of %r' % (self.nodeFrom(),self.nodeTo(),self.edgeWeight()))

'''	@descr	- An object to represent Dijkstra's Shortest Path Tree.
	@funct	-
			listTree	- Prints the contents of the Shortest Path Tree
'''
class shortPathTree:
	def __init__(self):
		self.vertex 	= []
		self.known 		= []
		self.distance 	= []
		self.via 		= []

	def setup(self,n):
		for i in range(n):
			self.vertex.append(i + 1)
			self.known.append(0)
			self.distance.append(math.inf)
			self.via.append(math.nan)

	def update(self,sel,idx,val):
		if sel == 'vtx':
			self.vertex[idx] = val
		elif sel == 'kwn':
			self.known[idx] = val
		elif sel == 'dst':
			self.distance[idx] = val
		elif sel == 'via':
			self.via[idx] = val
		else:
			print('Invalid entry for function: shortPathTree::update()')
		
		print('\nTable Update Complete\n')

	def listTree(self,st):
		i = 0
		print('\nStarting Node: %r' % st)
		print('NODE \t TOTAL DIST \t VIA')
		for vtx in self.vertex:
			if i == (st - 1):
				print('%r \t N/A \t\t SELF' % self.vertex[i])

			else:
				print('%r \t %r \t\t %r' % (self.vertex[i],self.distance[i],self.via[i]))
			i += 1
		i = 0

'''	@descr	- An object to represent a collection of Connections in a Graph.
	@param	- 
				- 
	@funct	-
			getNodes	- Return the INTEGER value for the amount of Nodes in this Graph
			addConn		- Add a new Connection to the Graph
			listConns	- Prints all Connections in this Graph
'''
class Graph:
	def __init__(self,n):
		self.nodes = n
		self.weight = 0
		self.maxWeight = -1
		self.connections = []
		self.shortPathTree = shortPathTree()
		
	def setup(self):
		self.shortPathTree.setup(self.nodes)

	def addCon(self,con):
		self.connections.append(con)
		self.weight += int(con.edgeWeight())

	def listConns(self):
		for i in range(len(self.connections)):
			print('Connection %r:\t' % i)
			print(self.connections[i].toString())
	
	def getNodes(self):
		return(self.nodes)

	def getWeight(self):
		return(self.weight)

	def calcMaxWeight(self):
		total = [];
		for con in self.connections:
			total.append(con.edgeWeight())
		
		self.maxWeight = max(total)

	def getMaxWeight(self):
		if self.maxWeight == -1:
			self.calcMaxWeight()
		return(self.maxWeight)

	def getOther(self,n2,wt):
		print(	'\nChecking for the pair Connection to:\n'
				'Node: %r\n'
				'Weight: %r\n' % (n2,wt))
		i = 0
		for z in range(len(self.connections)):
			print('Checking [%s]' % self.connections[i].toString())
			if int(self.connections[i].nodeFrom()) == int(n2):
				if int(self.connections[i].edgeWeight()) == int(wt):
					print('\'TO\' MATCH FOUND')
					return(self.connections[i])

			if int(self.connections[i].nodeTo()) == int(n2):
				if int(self.connections[i].edgeWeight()) == int(wt):
					print('\'FROM\' MATCH FOUND')
					return(self.connections[i])

			print('No match')
			i += 1
		return(int(-1))


#################################
#			FUNCTIONS			#
#################################

'''	@descr	- Check to see if a connection is already in a list
	@retrn	- BOOLEAN [integer].  '-1' means that the connection is a duplicate
'''
def isNewConn(newCon,ary = []):
	for i in range(len(ary)):
		if ((int(newCon.nodeFrom()) == int(ary[i].nodeTo()) and int(newCon.edgeWeight()) == int(ary[i].edgeWeight())) or
			(int(newCon.nodeTo()) == int(ary[i].nodeTo()) and int(newCon.edgeWeight()) == int(ary[i].edgeWeight())) or
			(int(newCon.nodeFrom()) == int(ary[i].nodeFrom()) and int(newCon.edgeWeight()) == int(ary[i].edgeWeight()))):
				print('Duplicate found')
				print('%s == %s' % (newCon.toString(),ary[i].toString()))
				return(int(-1))
		else:
			print('%s != %s' % (newCon.toString(),ary[i].toString()))
			
	return(int(0))

'''	@descr	- Check to see if a connection is already in a list
	@retrn	- BOOLEAN [integer].  '-1' means that the connection is a duplicate
'''
def isNewNode(newNd,ary = []):
	for i in range(len(ary)):
		if (newNd == ary[i]):
				print('Duplicate found')
				print('Node %r == Node %r' % (newNd,ary[i]))
				return(int(-1))
		else:
			print('Node %r != Node %r' % (newNd,ary[i]))
			
	return(int(0))

'''	@descr	- Check to see if the Shortest Path Tree can be improved
	@retrn	- None
'''
def calcPaths(spt,ary = []):
	pass

'''	@descr	- Reads a '.csv' file and creates a 'Graph' object based on the contents.
	@param	-
		fileName 	- The STRING name of the name of the input '.csv' file.
'''
def compileGraph(fileName):				#EXAMINE LECTURE 5 - PG. 58
	out = open(fileName + '.csv','r')
	fileFormat = out.readline().rstrip()
	nodes = int(out.readline())

	graph = Graph(nodes)
	graph.setup()

	for line in out.readlines():
		u = line.split(',')[0]
		v = line.split(',')[1]
		w = line.rstrip().split(',')[2]
		
		graph.addCon(Connection(u,v,w))

	out.close()
	#graph.listConns() #Before sorting
	graph.connections.sort(key=attrgetter('node1','node2'))
	#graph.listConns() #After sorting

	return(graph)


'''	@descr	- Returns the amount of Nodes in a '.csv' file
	@param	-
		fileName	- The STRING name of the name of the input '.csv' file.
	@retrn	- The number of nodes in the file
'''
def getFileNodeCount(fileName):
	out = open(fileName + '.csv','r')
	fileFormat = out.readline().rstrip()
	nodes = int(out.readline())
	out.close()

	return(nodes)

'''	@descr 		- Prints all connections in a '.csv' file
	@param -
		fileName 	- The STRING name of the name of the input '.csv' file.
'''
def getFileData(fileName):
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

'''	@descr 		- Generates a '.csv' file based in input values.
	@param -
		fileName 	- The STRING name to assign to the generated file
		nodeMin 	- 
		nodeMax 	- 
		conns 		- 
		wt 			- 
'''
def generateFile(fileName,nodeMin,nodeMax,conns,wt):
	random.seed()
	nodes = random.randint(nodeMin,nodeMax)
	out = open(fileName + '.csv','w')
	out.write('s\n%r\n' % nodes)

	for x in range(conns):
		u = random.randint(0,nodes)
		v = random.randint(0,nodes)
		w = random.randint(1,wt)
		out.write('%r,%r,%r\n' % (u,v,w))

	out.close()

'''	@descr	- Read in data to create a new random data file.
	@retrn	- STRING name of the newly generated file.
'''
def customFile():
	nodeMin = -1
	print('Please enter the following information to generate your test file...\n\n')
	fileName = input('Name of custom file:\n>>')
	while nodeMin <= 0:
		nodeMin = input('Minimum Nodes:\n>>')
	nodeMax = input('Maximum Nodes:\n>>')
	connections = input('Connection Count:\n>>')
	wtMax = input('Maximum Path Weight:\n>>')
	
	generateFile(fileName,int(nodeMin),int(nodeMax),int(connections),int(wtMax))

	return(fileName)

'''	@descr	- Read in data to create a new random data file.
	@param 	-
		g 	- A Graph object
		r 	- The 'root' node
'''
def dijkstra(g,r):
	known = 0
	connected = []
	nFr = []									# Array to maintain 'awareness'
	nFr.append(r)
	#nTo = 1
	#nFr = 1
	nWt = 1
	newConn = 0
	
	g.shortPathTree.update('kwn',0,1)

	print('\n**********************************************************\n')
	print(	'Calculating Shortest Path Spanning Tree.\n'
			'There are %r Nodes in this Graph.\n'
			'Max Graph Weight is: %r.\n'
			'Total Graph weight is: %r.\n' % (g.getNodes(),g.getMaxWeight(),g.getWeight()))
	
	print('Default Tree:')
	g.shortPathTree.listTree(r)
	
	#while known != 1:
	while known < 1:
		print('STARTING MAIN LOOP')
		for i in range(len(g.connections)):						# For every connection
			print('STARTING CONNECTIONS LOOP')
			#duplicate = 0
			for j in range(len(nFr)):							# For every adjacent Node 
				print('STARTING KNOWN NODES LOOP')
				for k in range(g.getMaxWeight()):
					print('STARTING WEIGHT LOOP')
					duplicate = 0
					newConn = g.getOther(nFr[j],nWt)

					if newConn != int(-1):							# if newConnection is a Point in the Graph
						if isNewConn(newConn,connected) == int(-1):	# If newConnection has already been added
							duplicate = 1
							nWt += 1

						if duplicate == 0:							# if newConnection has not already been added
							connected.append(newConn)
							nFr.append(newConn.nodeTo())
							nWt += 1

					else:											# newConnection is invalid
						if nWt < g.getMaxWeight():
							nWt += 1
					calcPaths(g.shortPathTree,connected)
				nWt = 1
			print('\n---')
			for con in connected:
				print(con.toString()) 							# Should report back '1, 4, 2, 3' after first run
			print('---\n')
			#calcPaths(g.shortPathTree,connected)

		known += 1














	#stage = 1
	#while known < 10:
	# while len(nFr) < 12:
	# 	for i in range(len(g.connections)):						# For every Connection
	# 		for j in range(len(nFr)):							# For all added points
	# 			newConn = g.getOther(nFr[j],nWt)				# Check for a connection with the search terms
	# 			duplicate = 0

	# 			if newConn != int(-1):							# if newConn IS a point
	# 				if isNewConn(newConn,connected) == int(-1):	# if newCon is in fact NOT NEW
	# 						duplicate = 1						# Set duplicate check
					
	# 				if duplicate != 1:							# If it is a new node
	# 					connected.append(newConn)				# Append it to the list
	# 					nFr.append(int(newConn.nodeTo()))		# Add the nodeTo to the list of known Nodes
	# 			else:
	# 				nWt += 1									# Increment search weight
	# 		# END FOR
		# END FOR

		#if isNewConn(newConn,connected) != int(-1):
		#	print('Adding node %s to awareness range' % newConn.nodeTo())
		#	nFr.append(int(newConn.nodeTo()))
		#else:
		#	print('Connection already known')
		
	#	connected.sort(key=attrgetter('weight'))	# Sort connected[] by weight

	#	known += 1									# 

		#Check for finalised tree
		#for i in g.shortPathTree.known:
		#	if g.shortPathTree.known[i] == 1:		# If the Connection is fixed
		#		pass
		#	else:									# If there is an indefinite Connection
		#		print("Search begins again!")
		#		nWt = 1
		#		break								# Search again
			
			#known = 1								# Set known to '1'.  Tree complete
	# END WHILE

	#connected.clear()
	print('\n\nPrinting Connections found:\n')
	for con in connected:
		print(con.toString())

	for i in nFr:
		print(i)
