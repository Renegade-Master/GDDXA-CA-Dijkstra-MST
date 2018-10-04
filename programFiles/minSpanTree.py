'''	@author			Ciaran Bent [K00221230]
	@creationDate	18/09/2018
	@description	'Statistics, Algorithms, and AI' Python implementation of 
					'Dijkstra's Minimum Spanning Tree' algorithm
	@version		1.3.3
	@deadline		12/10/2018
'''
import GraphTools

def main():
	graph = []
	root = 0

	print('**********************************************************')
	print('Welcome to \'Dijkstra\'s Minimum Spanning Tree\' Algorithm.')
	print('**********************************************************\n\n')
	usrInp = input('Do you want to generate your own randomised file? Y/N:\n>>')

	if usrInp == 'y' or usrInp == 'Y':
		print('You have created a file called \'%s.csv\' in the local directory.\n\n' % GraphTools.customFile())
		main()

	else:
		fileName = input('Please enter the name of the test file that you wish to use:\n>>')
		graph = GraphTools.compileGraph(fileName)

		print('\nThere are %r Nodes in this Graph.  The connections are as follows:\n' % GraphTools.getGraphNodeCount(graph))
		graph.sort()
		GraphTools.getGraphData(graph)
		
main()
