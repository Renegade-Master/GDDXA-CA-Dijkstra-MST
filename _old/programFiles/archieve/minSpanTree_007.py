#
#	@author			Ciaran Bent [K00221230]
#	@creationDate	18/09/2018
#	@description	'Statistics, Algorithms, and AI' Python implementation of 
#					'Dijkstra's Minimum Spanning Tree' algorithm
#	@version		1.3.0
#	@deadline		12/10/2018

import GraphTools
#import scratchPad

#from collections import deque

#def dijkstra(graph,root):


def main():
	nodes = 0

	print('Welcome to \'Dijkstra\'s Minimum Spanning Tree\' Algorithm.\n\n')
	usrInp = input('Do you want to generate your own randomised file? Y/N:\n>>')

	if usrInp == 'y' or usrInp == 'Y':
		GraphTools.createGraph(GraphTools.customFile())

	else:
		fileName = input('Please enter the name of the test file that you wish to use:\n>>')
		GraphTools.createGraph(fileName)

main()