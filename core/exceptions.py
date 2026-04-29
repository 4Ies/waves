class StorageException(Exception):
    """
    Basic exception coming from the storage manager
    """
    pass

class IncorrectSearchCall(StorageException):
    """
    Command search called on a non-existing song over song db
    """
    pass

class SongNotFound(StorageException):
    """
    Searched song found no match inside the database
    """
    pass