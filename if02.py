def main(a):
    """
    If the number is positive, increase it to 1, else decrease it to 2.
    Args:
        a: integer
    Returns:
        a: a increased by 1 if positive, else decreased by 2.
    """
    s=""

    if a>=0:
        s=a+1

    else:
        s=a-2
    
    return s

print(main(6))
