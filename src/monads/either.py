# -*- coding: utf-8 -*-



""" 
   simple implementation of either monad
"""
class Either(object):
    def __init__(self):
        raise NotImplementedError( "Should have implemented this" )
    def isLeft(self): return False
    def left(self):
        raise NotImplementedError( "No value present" )
    def isRight(self): return False
    def right(self):
        raise NotImplementedError( "No value present" )

class LeftProjection(Either):
    def __init__(self, value):
        self.value = value

    #overrides
    def isLeft(self): return True
    def left(self): return self.value;

class RightProjection(Either):
    def __init__(self, value):
        self.value = value

    #overrides
    def isRight(self): return True
    def right(self): return self.value;

def Left(value): return LeftProjection(value)
def Right(value): return RightProjection(value)
