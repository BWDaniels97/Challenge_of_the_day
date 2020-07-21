'''
Define a class named Rectangle, which can be constructed by a length and width.

 

The Rectangle class needs to have a method that can compute area.

 

Finally, write a unit test to test this method.

'''


class rectangle:

    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def findarea(self):
        return self.length * self.width


