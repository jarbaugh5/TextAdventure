'''
This is the main file for the comp 40 text adventure.

Run this file to experience Comp 40 in its full glory.

By: Jon Arbaugh
Tufts 2017
'''

from story import *
from runner import runner


'''
	Load the steps and pass them off the game runner
'''
def main():
	runner(story)

if __name__ == '__main__':
	main()