#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 06:31:05 2019

@author: schirmer
"""

import enum
from collections import namedtuple

class Player(enum.Enum):
    black = 1
    white = 2
    
    @property
    def other(self):
        return Player.black if self == Player.white else Player.white
    
class Point(namedtuple('Point', 'row col')):
    def neighbors(self):
        return [
                Point(self.row - 1, self.col),
                Point(self.row + 1, self.col),
                Point(self.row, self.col - 1),
                Point(self.row, self.col + 1),
                ]