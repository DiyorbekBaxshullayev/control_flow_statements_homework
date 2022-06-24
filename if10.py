def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    s=""

    if temp<=0:
        s="Freezing"

    elif 1<=temp<=10:
        s="Very Cold"

    elif 11<=temp<=20:
        s="Cold"

    elif 21<=temp<=30:
        s="Normal"

    elif 31<=temp<=40:
        s="Hot"

    elif temp>=40:
        s="Very Hot"
    
    return s

print(main(30))
