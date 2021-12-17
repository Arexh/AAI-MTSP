'''
Holds all the node objects and is used for
creation of chromosomes by jumbling their sequence
'''
from node import *


class RouteManager:
    destinationNodes = []

    @classmethod
    def addNode(cls, db):
        cls.destinationNodes.append(db)

    @classmethod
    def getNode(cls, index):
        return cls.destinationNodes[index]

    @classmethod
    def numberOfNodes(cls):
        return len(cls.destinationNodes)
