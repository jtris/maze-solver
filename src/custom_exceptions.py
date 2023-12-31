class InvalidPathException(Exception):
    '''Raise when the path inputted by the user isn't valid'''
    def __init__(self, message='\nIncorrect Path, Please enter a valid path to an image of a maze.\n'):
        self.message = message
        super().__init__(self.message)


class NoArgumentError(Exception):
    '''Raise when the user doesn't specify a path as an argument'''
    def __init__(self, message='\nPlease provide a path to an image of a maze.\n'):
        self.message = message
        super().__init__(self.message)


class InvalidMazeFormatError(Exception):
    '''Raise when the maze doesn't follow the format I've accounted for'''
    def __init__(self, message='\nIncorrect maze format.\n'):
        self.message = message
        super().__init__(self.message)


class InvalidImageFormatError(Exception):
    '''Raise when the supplied image is either of a format OpenCV can't read or it isn't an image'''
    def __init__(self, message='\nInvalid image. Try a different file-type and make sure it is an image.\n'):
        self.message = message
        super().__init__(self.message)
