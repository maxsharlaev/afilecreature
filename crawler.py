import os
import hashlib
#import sqlite3

#class liter:
#    def __init__(self, dbfile):
#        pass


class FileItem:
    def __init__(self, item, level, path=''):
        self.name = item.name
        self.level = level
        self.type = 'file' if not item.is_dir() else 'dir'
        self.path = path


class Crawler:
    def __init__(self, path, level_max = 0):
        self.level_max = level_max
        self.path = path

    @staticmethod
    def item_get(item, level, path=''):
        return FileItem(item, level, path)

    def skip(self, patterns):
        pass

    def walk(self, level=0, path='', level_max=0):

        path = path or self.path
        level_max = level_max or self.level_max

        for item in os.scandir(path):

            if item.name.startswith('.') or item.name.startswith('$'):
                continue

            if item.is_dir():

                yield self.item_get(item, level, path)

                if level_max == 0 or level < level_max:
                    for dir_item in self.walk(level+1, path + '/' + item.name):
                        yield dir_item
            else:

                yield self.item_get(item, level, path)


if __name__ == '__main__':
    pass
