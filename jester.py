from crawler import Crawler
import hashlib


class Jester:

    data = ''

    def __init__(self, filename):
        if filename:
            self.load(filename)

    def load(self, filename):
        print(filename)
        with open(filename, 'rb') as f:
            self.data = f.read()

    def set(self, data):
        self.data = data.encode()

    @property
    def md5(self):
        return hashlib.md5(self.data).hexdigest()

    @property
    def sha1(self, ):
        return hashlib.sha1(self.data).hexdigest()


if __name__ == '__main__':
    pass