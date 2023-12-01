class InvalidPathException(Exception):
	'''Raise when the path inputted by the user isn't valid'''
	def __init__(self, message='Incorrect Path, Please enter a valid path to an image of a maze.\n'):
		self.message = message
		super().__init__(self.message)


class NoArgumentError(Exception):
	'''Raise when the user doesn't specify a path as an argument'''
	def __init__(self, message='Please provide a path to an image of a maze.\n'):
		self.message = message
		super().__init__(self.message)


class InvalidMazeFormatException(Exception):
	'''Raise when the maze doesn't follow the format I've accounted for'''
	def __init__(self, message='Incorrect maze format.'):
		self.message = message
		super().__init__(self.message)
