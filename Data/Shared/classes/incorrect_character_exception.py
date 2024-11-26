"""Used to express incorrect character exceptions"""
class IncorrectCharacterException(Exception):
    """Used to express incorrect character exceptions"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
