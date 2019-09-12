from abc import ABC, abstractmethod


class InValidOperationError(Exception):
    pass


class Stream(ABC):  # an abstract class, is a half baked cookie
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InValidOperationError('Stream is already opened')
        self.opened = True

    def close(self):
        if not self.opened:
            raise InValidOperationError('Stream is already closed')
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print('Reading data from a file')


class NetworkStream(Stream):
    def read(self):
        print('Reading data from a Network Stream')


class MemoryStream(Stream):
    def read(self):
        print('Reading data from a memory stream')


stream = MemoryStream()
stream.open()
