def main(a,b,c):
    """
    Find how many negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    s=""

    if a<0 and b<0 and c<0:
        s=3

    elif (a>0 and b<0 and c<0) or (a<0 and b>0 and c<0) or (a<0 and b<0 and c>0):
        s=2

    elif (a>0 and b>0 and c<0) or (a>0 and b<0 and c>0) or (a<0 and b>0 and c>0):
        s=1

    else:
        s=0
    
    return s

print(main(-5,-2,2))
