#!/usr/bin/python3


def pascal_triangle(n):
    """ returns pascal triangle
    """
    if n <= 0:
        return []

    Ptriangle = []

    for i in range(n):
        # first element
        my_List = [1]
        if i == 0:
            Ptriangle.append(my_List)
            continue

        k = i - 1
        for j in range(len(Ptriangle[k])): 
            if j + 1 == len(Ptriangle[k]):
                # last element
                my_List.append(1)
                break
            # Add two previous values to get current next value
            nextVal = Ptriangle[k][j] + Ptriangle[k][j + 1]
            my_List.append(nextVal)
        Ptriangle.append(my_List)

    return Ptriangle
