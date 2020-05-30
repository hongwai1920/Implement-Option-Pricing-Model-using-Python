def finite_difference(f, e, second_order = False):
    '''
    inputs:
    ==========
    
    f: function (lambda function)
    e: error
    second_order: order of finite difference method
    
    
    returns:
    =========
    
    if second_order is False, then it returns first-order finite difference approximation
    Otherwise, it returns second-order finite difference approximation
    '''
    
    if second_order:
        return (f(e) - 2*f(0) + f(-e)) / e**2
    return (f(e) - f(0)) / e