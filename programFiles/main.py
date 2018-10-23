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

	#fileName = input('Please enter the name of the test file that you wish to use:\n>>')
	fileName = 'test'
	graph = GraphTools.compileGraph('testFiles\\%s' % fileName)

	#graph.listConns()
	#graph.shortPathTree.debugTree()

	GraphTools.Dijkstra(graph)

__main__()
