import os
from crawler import Crawler
from jester import Jester

class Scanner:

    excluded_path = []
    included_types = []
    data = None

    def __init__(self, data):
        self.data = data
        pass

    def _split(self, line):
        if isinstance(line, list):
            return line
        else:
            if ',' in line:
                return line.split(',')
            elif ';' in line:
                return line.split(';')

    def set_types(self, types):
        self.included_types = self._split(types)

    def path_exclude(self, paths):
        self.excluded_path = self._split(paths)

    def save(self, digest):
        pass

    def check_file(self, digest):
        pass

    def check_dir(self, digest):
        pass

    def go(self, path, mode='check'):

        for file in Crawler(path, self.excluded_path).walk():
            splitfile = os.path.splitext(file)
            separator = os.sep

            full_file = file.path + separator + file.name

            if file.type == 'file':
                if len(self.included_types) > 0 and splitfile not in self.included_types:
                    digest = {'file': full_file, 'md5': '', 'sha1': ''}
                else:
                    with Jester as j:
                        digest = { 'file' : full_file, 'md5': j.md5, 'sha1': j.sha1 }
                if digest['md5']:
                    if mode == 'save':
                        self.save(digest)
                    else:
                        if not self.check_file(digest):
                            #TODO: changed file notification
                            pass
            else:
                if not self.check_dir(digest):
                    # TODO: directory changed notification
                    pass


if __name__ == '__main__':
    pass
