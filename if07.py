def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    s=""

    if a>0 and a%2==0:
        s="positive even number"

    elif a>0 and a%2==1:
        s="positive odd number"

    elif a<0 and a%2==0:
        s="negative even number"

    elif a<0 and a%2==1:
        s="negative odd number"

    elif a==0:
        s="the number is zero"
    
    return s

print(main(4))
