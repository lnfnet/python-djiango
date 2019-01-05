class A(object):

    def __init__(self, a):
        self.a = a
        print 'init A...'
       
class B(A):
 
    def __init__(self, a):
        super(B, self).__init__(a)
        print 'init B...'
class C(A):
 
    def __init__(self, a):
        super(C, self).__init__(a)
        print 'init C...'

class D(B, C):
  
    def __init__(self, a):
        super(D, self).__init__(a)
        print 'init D...'
