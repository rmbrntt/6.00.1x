__author__ = 'ryan@barnett.io'
class Queue(object):

    def __init__(self):
        self.stack = []
        self.popped = 'element'

    def insert(self, element):
        self.stack.append(element)

    def remove(self):
        if self.stack == []:
            raise ValueError
        else:
            self.popped = self.stack[0]
            self.stack.remove(self.stack[0])
            return self.popped

q1 = Queue()
q2 = Queue()
q1.insert(17)
q2.insert(20)
q1.remove()
q2.remove()
