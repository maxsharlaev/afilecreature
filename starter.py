from argparse import ArgumentParser
from scanner import Scanner
from saver import Saver

class Starter:

    def __init__(self):
        parser = ArgumentParser(description='Command line process')
        parser.add_argument('--key')
        parser.add_argument('--val')

    def backup(self, config):
        with Saver(config) as sv:
            sv.go()
        pass
    def deploy(self, config):

    def scan(self, path):
        with Scanner(path) as sc:
            sc.go()
