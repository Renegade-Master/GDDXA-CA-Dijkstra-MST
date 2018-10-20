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

class shortPathTree:
	def __init__(self):
		self.vertex = []
		self.known = []
		self.distance = []
		self.via = []

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
			pass
		elif sel == 'dst':
			pass
		elif sel == 'via':
			pass
		else:
			print('Invalid entry for function: shortPathTree::update()')
		
		print('Table Update Complete')

	def listTree(self,st):
		i = 0
		print('Starting Node: %r' % st)
		print('\nNODE \t TOTAL DIST \t VIA')
		for vtx in self.vertex:
			if i == (st - 1):
				print('%r \t N/A \t\t SELF' % self.vertex[i])

			else:
				print('%r \t %r \t\t %r' % (self.vertex[i],self.distance[i],self.via[i]))
			i += 1
		i = 0

class Graph:
	def __init__(self,n):
		self.nodes = n
		self.weight = 0
		self.connections = []
		self.shortPathTree = shortPathTree()
		
	def setup(self):
		self.shortPathTree.setup(self.nodes)
		# for i in range(self.nodes):
		# 	lnklst = []
		# 	self.connections.append(lnklst)
		# 	self.connections[i].append(lnklst)

	def addCon(self,con):
		self.connections.append(con)
		self.weight += int(con.edgeWeight())

	def listConns(self):
		for i in range(len(self.connections)):
			print('Connection %r connects\n'
				'\tNode %r to Node %r '
				'with a weight of %r\n' % (i,self.connections[i].nodeFrom(),self.connections[i].nodeTo(),self.connections[i].edgeWeight()))
	
	def getNodes(self):
		return(self.nodes)

	def getWeight(self):
		return(self.weight)

	def getOther(self,n2,wt):
		i = 0
		j = 0
		for z in range(len(connections)):
			if self.connections[i].nodeFrom() == n2:
				if self.connections[i].edgeWeight() == wt:
					print(self.connections[i].nodeTo())

			elif self.connections[i].nodeTo() == n2:
				if self.connections[i].edgeWeight() == wt:
					print(self.connections[i].nodeFrom())
		
		print('Match not found')