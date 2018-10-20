#
#	@author			Ciaran Bent [K00221230]
#	@creationDate	18/09/2018
#	@description	'Statistics, Algorithms, and AI' Python implementation of 
#					'Dijkstra's Minimum Spanning Tree' algorithm
#	@version		1.3.0
#	@deadline		12/10/2018

import GraphTools
#import scratchPad

#def dijkstra(graph,root):


def main():
	nodes = 0

	print('**********************************************************')
	print('Welcome to \'Dijkstra\'s Minimum Spanning Tree\' Algorithm.')
	print('**********************************************************\n\n')
	usrInp = input('Do you want to generate your own randomised file? Y/N:\n>>')

	if usrInp == 'y' or usrInp == 'Y':
		GraphTools.createGraph(GraphTools.customFile())
		main()

	else:
		fileName = input('Please enter the name of the test file that you wish to use:\n>>')
		#GraphTools.createGraph(fileName)
		print('\n\nIf you would like, you can choose a starting Node for the Algorithm.  Otherwise one will be selected randomly.')
		startNode = input('\nEnter a number between 1 - %r to select a starting Node.  Type any other character to randomise.\n>>' % GraphTools.getFileNodeCount(fileName))

		#if isinstance(int(startNode),int):
		#try:
		if startNode >= 1 and startNode <= int(GraphTools).getFileNodeCount(fileName):
			#startNode = input('\nEnter a number between 1 - %r to select a starting Node.  Type any other character to randomise.\n>>' % GraphTools.getFileNodeCount(fileName))
			print('You selected: %r.' % startNode)

		#except:
			print('A Starting Node was selected at random.')

main()