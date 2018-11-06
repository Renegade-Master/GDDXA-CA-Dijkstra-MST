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
	print('************************************************************\n')

	valid = False
	root = -GraphTools.math.inf

	while(not valid):
		try:
			GraphTools.listDir('testFiles\\')
		except:
			print('ERROR: Could not access os module.\nIt is safe to ignore this warning.\n')
		try:
			fileName = input('Please enter the name of the test file that you wish to use:\n>>')
			graph = GraphTools.compileGraph('testFiles\\%s' % fileName)
			valid = True
		except:
			print('No such file: %s.csv' % fileName)
			valid = False

	valid = False
	while((not valid) or ((root < 1) or (root > graph.getNodes()))):
		try:
			root = int(input('Please enter a number between 1 - %s to be the Starting Node:\n>>' % graph.getNodes()))
			valid = True
		except:
			print('\n\nERROR: Invalid input.\n')
			valid = False

	GraphTools.Dijkstra(graph,root)
	graph.shortPathTree.listTree()

__main__()
