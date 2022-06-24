def main(a):
    """
    If the number is positive, increase it to 1, else decrease it to 2. If it is 0, assign 10.
    Args:
        a: integer
    Returns:
        a: integer
    """
    s=""

    if a>0:
        s=a+1

    if a==0:
        s=10

    else:
        s=a-2
    
    return s

print(main(-2))
