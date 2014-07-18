'''
The runner takes in a story object and runs it

By: Jon Arbaugh
Tufts 2017
'''

def runner(story):
	if 'message' in story and 'branches' in story:
		done = False
		while not done:
			response = raw_input(story.get('message'))

			if response in story.get('branches').keys():
				done = True
				runner(story.get('branches').get(response))
			else:
				print 'That is not a valid input.'
				print 'Valid inputs include:'
				for key in story.branches.keys():
					print key
	
	elif 'message' in story:
		print story.get('message')