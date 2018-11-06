'''	@author			Ciaran Bent [K00221230]
	@creationDate	20/10/2018
	@description	'Statistics, Algorithms, and AI' Python implementation of 
					'Dijkstra's Minimum Spanning Tree' algorithm
	@version		1.0.0
	@deadline		31/10/2018
'''

import GraphTools

def __main__():
	print('************************************************************')
	print('* Welcome to \'Dijkstra\'s Minimum Spanning Tree\' Algorithm. *')
	print('************************************************************\n\n')

	valid = False
	root = -GraphTools.math.inf

	while(not valid):
		try:
			fileName = input('Please enter the name of the test file that you wish to use:\n>>')
			#fileName = 'test'
			graph = GraphTools.compileGraph('testFiles\\%s' % fileName)
			valid = True
		except:
			print('No such file')
			valid = False

	valid = False
	while((not valid) or ((root < 1) or (root > graph.getNodes()))):
		try:
			root = int(input('Please enter a number between 1 - %s to be the Starting Node:\n>>' % graph.getNodes()))
			valid = True
		except:
			print('\n\nERROR: Invalid input.\n')
			valid = False

	#graph.listConns()
	#graph.shortPathTree.debugTree()

	GraphTools.Dijkstra(graph,root)
	graph.shortPathTree.listTree()

__main__()
