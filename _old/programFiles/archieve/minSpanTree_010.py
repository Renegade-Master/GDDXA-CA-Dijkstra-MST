'''	@author			Ciaran Bent [K00221230]
	@creationDate	18/09/2018
	@description	'Statistics, Algorithms, and AI' Python implementation of 
					'Dijkstra's Minimum Spanning Tree' algorithm
	@version		1.3.1
	@deadline		12/10/2018
'''
import GraphTools
#import scratchPad

#def dijkstra(graph,root):


def main():
	print('**********************************************************')
	print('Welcome to \'Dijkstra\'s Minimum Spanning Tree\' Algorithm.')
	print('**********************************************************\n\n')
	usrInp = input('Do you want to generate your own randomised file? Y/N:\n>>')

	if usrInp == 'y' or usrInp == 'Y':
		print('You have created a file called \'%s.csv\' in the local directory.\n\n' % GraphTools.customFile())
		main()

	else:
		fileName = input('Please enter the name of the test file that you wish to use:\n>>')
		#graph = GraphTools.createGraph(fileName)
		#GraphTools.printGraphData(fileName)
		GraphTools.compileGraph(fileName)


main()