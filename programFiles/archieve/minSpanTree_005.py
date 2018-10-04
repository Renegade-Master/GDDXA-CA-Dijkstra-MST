#
#	@author			Ciaran Bent [K00221230]
#	@creationDate	18/09/2018
#	@description	'Statistics, Algorithms, and AI' Python implementation of 
#					'Dijkstra's Minimum Spanning Tree' algorithm
#	@version		1.2.1

import GraphTools
#import scratchPad

from collections import deque

def createGraph(fileName):
	GraphTools.printGraphData(fileName)

#def dijkstra(graph,root):


def main():
	nodes = 0

	usrInp = input('Do you want to generate your own randomised file? Y/N:\n>>')

	if usrInp == 'y' or usrInp == 'Y':
		createGraph(GraphTools.customFile())

	else:
		fileName = input('Please enter the name of the test file that you wish to use:\n>>')
		createGraph(fileName)

main()