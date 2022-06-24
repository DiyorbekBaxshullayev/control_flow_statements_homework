def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    s=""

    if (a%10)%2==1:
        s="two-digit odd number"

    elif (a%10)%2==0:
        s="two-digit even number"

    elif (a%100)%2==1:
        s="three-digit odd number"

    elif (a%100)%2==0:
        s="three-digit even number"

    
    
    return s

print(main(3))
