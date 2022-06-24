def main(a):
    """
    If the number is positive, increase it to 1, else leave unchanged.
    Args:
        a: integer
    Returns:
        a: a increased by 1 if positive, else unchanged.
    """
    s=""

    if a>=0:
        s=a+1

    else:
        s=a
    
    return s

print(main(-5))

