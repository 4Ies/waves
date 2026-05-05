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

class AlbumNotFound(StorageException):
    """
    Searched album found no match inside the database
    """
    print("Exception: album not found")
    pass

class SongNotFound(StorageException):
    """
    Searched song found no match inside the database
    """
    print("Exception: song not found")
    pass

class TranscriptionError(Exception):
    """
    Transcription function encountered an error
    """
    print("Exception: transcription of text encountered an error")
    pass

class IsolationException(Exception):
    """
    Error occurred in isolating vocals
    """
    print("Exception: vocals not generated due to error in isolator")
    pass