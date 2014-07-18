'''
The runner takes in a story object and runs it

By: Jon Arbaugh
Tufts 2017
'''

def printOptions(options):
	print 'Options:\n'
	for index, val in enumerate(options):
		print str(index + 1) + ') ' + str(val) + '\n'

def printInputError(options):
	print 'That is not a valid input. Input must be an integer.'
	print 'Valid inputs include:'
	printOptions(options)

def runner(story):
	if 'message' in story and 'options' in story and 'branches' in story:
		done = False
		while not done:
			print story.get('message') + '\n'
			printOptions(story.get('options'))

			response = raw_input()
			try:
				response = int(response)

				if response > 0 and response <= len(story.get('branches')):
					done = True
					runner(story.get('branches')[response - 1])
				else:
					printInputError(story.get('options'))
			except ValueError:
				printInputError(story.get('options'))
	
	elif 'message' in story:
		print story.get('message')