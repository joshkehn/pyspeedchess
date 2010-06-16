# Python chess speed clock
# 06/15/2010
#
# Joshua Kehn	<Josh.Kehn@gmail.com>

import sys
import time

def getInput():
	input = sys.stdin.readline()
	return input


input = ""
turn = "player1"
players = ['player1', 'player2']

while input is not "e":
	input = None
	start = time.time()	
	elap = 0
	while input is None or elap < 5:
		elap = time.time() - start
		input = checkChar()
	
	if(elap >= 5):
		print "Too long. Switch."
		continue
	
	print "Move took ", elap, " seconds"
	
