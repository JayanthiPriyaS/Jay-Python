a=10
def show():
    '''
    a=500
    print globals()
    print 50*'-'
    print locals()
    '''
    print a
    global a
    a=50
    
    #print globals()
    print 50*'-'
    #print locals()
    print a
    
