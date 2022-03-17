class Error(Exception):
    """Base class for other exceptions"""
    pass

class EmptyListError(Error):
    """Raised when the column is empty"""
    pass