def self_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type:'+str(type(x)))
    if x>=0:
        return x
    else:
        return -x