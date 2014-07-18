'''
The story is a a series of nested dicts and arrays.
Its probably not the cleanest solution, but it works for small game.

The story object works like this:

story = {
	'message': "The message to display to the user",

	'options': [
		'option1',
		'option2'
	],

	# branches off of this message
	'branches': [
		{
			... story object for option 1 ...
		},
		{
			... story object for option 2 ...
		}
	]

}

By: Jon Arbaugh
Tufts 2017
'''

programCompleteStory = {
	'message': 'You\'re program works!! Good thing too because the next assingment has already\n' +
	'been released...',
}

vagueBugStory = {
	'message': 'You\'re program ran, but you seem to have a very very vague bug that you\'ll\n' +
	'probably never find...',

	'options': [
		'I am determined. Debug.',
		'Continue to smash face into desk.'
	],

	'branches': [
		None,
		programCompleteStory
	]
}
vagueBugStory['branches'][0] = vagueBugStory

syntaxErrorStory = {
	'message': 'SYNTAX ERROR: Its C so you have no idea what this syntax error is about.',

	'options': [
		'Debug this error',
		'Smash face into desk repeatedly'
	],

	'branches': [
		vagueBugStory,
		None
	]
}
syntaxErrorStory['branches'][1] = syntaxErrorStory

compileDecision = [
	{
		# Decides no
		'message': 'Ah a poor decision... You continue to work and now you\'ve come to\n' +
		'a point where you must compile.',

		'options': [
			'Compile'
		],

		'branches': [
			syntaxErrorStory
		]
	},
	# Decides yes
	syntaxErrorStory
]

hasAPartner = [
	{
		# Read over the spec
		'message': 'It\'s the evening and you\'ve just arrived at Halligan.\n' +
		'The walk down was relaxing, but now it\'s time for business. You and your\n' +
		'partner grab machines in 118 and get to work. You\'ve both read the spec and\n' +
		'things are going great!\n\n' + 
		'You and you\'re partner layout a plan and get to work. Making sure to write clean\n' +
		'code. After a few minutes you get to a good stopping point.\n' + 
		'Should you try to compile before continuing?',

		'options': [
			'Nope I prefer to live life on the edge',
			'Yeah I\'ll give it shot. After all, test early, test often!'
		],

		'branches': compileDecision
	},
	{
		# Did not read over the spec of course
		'message': 'It\'s the evening and you\'ve just arrived at Halligan.\n' +
		'The walk down was relaxing, but now it\'s time for business. You and your\n' +
		'partner grab machines in the TA room (for immediate access) and get to work.\n' +
		'Neither you or your partner read the spec, but that\'s okay.\n' +
		'Guessing what the spec said is more fun anyway.\n\n' + 
		'You and you\'re partner layout a plan and get to work. Making sure to write clean\n' +
		'code and few short obvious tests. After a few minutes you get to a good stopping point.\n' + 
		'Should you try to compile before continuing?',

		'options': [
			'Nope I prefer to live life on the edge',
			'Yeah I\'ll give it shot. After all, test early, test often!'
		],

		'branches': compileDecision
	}
]

story = {
	'message': 'Wow! What a great Comp40 lecture!! Professor mentioned a new\n' +
	'assignment today. Should you look for a partner?',

	'options': [
		'Hmm alright I\'ll be responsible',
		'How bout or nah'
	],

	'branches': [
		{
			# Found a partner
			'message': 'Things are looking good so far. You have a partner and you have\n' +
			'plans to meetup tonight and work. Read over the spec in advance?',

			'options': [
				'Sure I wouldn\'t want to be unprepared',
				'Nope definitely not'
			],

			'branches': hasAPartner
		},
		{
			# Did not look for a partner yet
			'message': 'Its been two days and you haven\'t found a partner\n' +
			'Luckily there are plenty of other people just like you and your last\n' +
			'minute post to the Comp40 page netted you a partner. You\'ll be meeting up with\n' +
			'them tonight. Should you read over the spec before hand?',

			'options': [
				'Sure I wouldn\'t want to be unprepared',
				'Nope definitely not'
			],

			'branches': hasAPartner
		}
	]
}