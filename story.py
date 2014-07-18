'''
The story is a a series of nested dicts and arrays.
Its probably not the cleanest solution, but it works for small game.

The story object works like this:

story = {
	'message': "The message to display to the user",

	# branches off of this message
	# keys are the acceptable responses to the aformentioned message
	# values are the story object associated with each answer
	'branches': {
		'answer': {
			... story object ...
		}
	}

}

By: Jon Arbaugh
Tufts 2017
'''

story = {
	'message': 'Wow! What a great Comp40 lecture!! Professor mentioned a new\n' +
	'assignment today. Should you look for a partner?',

	'options': [
		'Hmm alright I\'ll be responsible',
		'How bout or nah'
	],

	'branches': [
		{
			'message': 'You chose the yes option!'
		},
		{
			'message': 'You chose the no option!'
		}
	]
}