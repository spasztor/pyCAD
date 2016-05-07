#!/usr/bin/python
import uuid

class Point:
    def __init__(self):
        self.x_val = 0
        self.y_val = 0
        self.handle = uuid.uuid4()
